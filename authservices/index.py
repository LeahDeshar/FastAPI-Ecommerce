from fastapi import FastAPI, APIRouter, Request, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr
from fastapi import FastAPI, Depends, HTTPException
from passlib.context import CryptContext
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
from database import engine, Base, get_db
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
import models, schemas
from fastapi.middleware import Middleware
from typing import List
from functools import wraps
Base.metadata.create_all(bind=engine)

app = FastAPI()
router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Request: Method -> {request.method} URL -> {request.url} -----------")
    response = await call_next(request)
    return response



@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    if "Authorization" in request.headers:
        auth_header = request.headers.get("Authorization")
        token = auth_header.split(" ")[1] if auth_header.startswith("Bearer ") else None
        if token:
            try:
                payload = verify_access_token(token)
                db = next(get_db())
                user = db.query(models.User).filter(models.User.email == payload.get("sub")).first()
                if not user:
                    return JSONResponse(status_code=401, content={"detail": "Invalid user"})
                request.state.user = user  # Assign the User object
            except HTTPException as e:
                return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
        else:
            return JSONResponse(status_code=401, content={"detail": "Invalid or missing token"})
    return await call_next(request)


def role_required(roles: list):
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            current_user: models.User = request.state.user
            print(f"current user {current_user.role.value}--------")
            if str(current_user.role.value) not in roles: 
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Not enough permissions",
                )
            return await func(request, *args, **kwargs)
        return wrapper
    return decorator

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "role": data.get("role")})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_access_token(token)
    user = db.query(models.User).filter(models.User.email == payload.get("sub")).first()
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user    


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


@router.post("/register", response_model=schemas.RegisterResponse,status_code=status.HTTP_201_CREATED)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already taken")
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = hash_password(user.password)
    
    db_user = models.User(
        username=user.username,
        email=user.email,
        password=hashed_password,
        role=user.role,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    user_response = schemas.UserResponse.from_orm(db_user)
    return schemas.RegisterResponse(
        data=user_response,
        message="Registered successfully"
    )


@router.post("/login", response_model=schemas.UserResponse)
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    if not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
   
   
    access_token = create_access_token(data={"sub": db_user.email, "role": db_user.role.value})
  
   
    return JSONResponse(content={"access_token": access_token, "token_type": "bearer","role": db_user.role.value})

@router.get("/current-user", response_model=schemas.UserResponse)
def get_current_user_endpoint(current_user: models.User = Depends(get_current_user)):
    return schemas.UserResponse.from_orm(current_user)



@router.get("/admin", dependencies=[Depends(get_current_user)])
@role_required(["admin"])
async def admin_route(request: Request):
    return {"message": "Welcome, Admin!"}


@router.get("/dashboard", dependencies=[Depends(get_current_user)])
@role_required(["admin","user"])
async def dashboard_route(request: Request):
    return {"message": "Welcome to your dashboard!"}



@router.get("/test", dependencies=[Depends(get_current_user)])
@role_required(["user"])
async def dashboard_route(request: Request):
    return {"message": "Welcome to your test controller!"}

@router.get("/public")
async def public_route():
    return {"message": "This is a public route"}


@router.get("/user/{user_id}", response_model=schemas.UserResponse)
@role_required(["user","admin"])
def get_user(user_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return schemas.UserResponse.from_orm(user)


@router.delete("/user/delete", response_model=dict)
@role_required(["user","admin"])
def delete_user(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    user = db.query(models.User).filter(models.User.id == current_user.id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"message": "User account deleted successfully"}

app.include_router(router, prefix="/api/v1/auth")