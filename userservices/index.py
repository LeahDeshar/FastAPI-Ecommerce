from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import UserProfileUpdate, UserProfileResponse
from user import fetch_user_profile, modify_user_profile
from core.config import get_db
from core.auth import get_current_user

router = APIRouter()

@router.get("/profile", response_model=UserProfileResponse)
def get_user_profile(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    db_user = fetch_user_profile(db, current_user["id"])
    if not db_user:
        raise HTTPException(status_code=404, detail="User profile not found")
    return db_user

@router.patch("/profile", response_model=UserProfileResponse)
def update_user_profile(user_update: UserProfileUpdate, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    db_user = modify_user_profile(db, current_user["id"], user_update.dict())
    if not db_user:
        raise HTTPException(status_code=404, detail="User profile not found")
    return db_user
