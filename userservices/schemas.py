from pydantic import BaseModel
from typing import Optional

class UserProfileUpdate(BaseModel):
    phone_number: Optional[str] = None
    address: Optional[str] = None

class UserProfileResponse(BaseModel):
    phone_number: str
    address: str

    class Config:
        orm_mode = True  
