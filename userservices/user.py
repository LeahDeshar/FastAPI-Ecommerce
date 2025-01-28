from sqlalchemy.orm import Session
from models import UserProfile

def get_user_profile(db: Session, user_id: int):
    return db.query(UserProfile).filter(UserProfile.user_id == user_id).first()

def update_user_profile(db: Session, user_id: int, user_update: dict):
    db_user = db.query(UserProfile).filter(UserProfile.user_id == user_id).first()
    if db_user:
        for key, value in user_update.items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user
