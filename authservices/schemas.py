from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum
from datetime import datetime

class RoleEnum(str, Enum):
    user = "user"
    admin = "admin"

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
    
class ProfileResponse(BaseModel):
    first_name: str
    last_name: str

    class Config:
        orm_mode = True
        from_attributes = True
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: RoleEnum = RoleEnum.user  

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    role: RoleEnum

    class Config:
        orm_mode = True 
        from_attributes = True
        
        
class RegisterResponse(BaseModel):
    data: UserResponse
    message: str
    
    
