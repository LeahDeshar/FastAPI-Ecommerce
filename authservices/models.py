from sqlalchemy import Column, Integer, String,Boolean,DateTime,ForeignKey,Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import enum 
class RoleEnum(enum.Enum):
    user = "user"
    admin = "admin"
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    # role = Column(String, default="user")
    role = Column(Enum(RoleEnum), default=RoleEnum.user)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    profile = relationship("Profile", back_populates="user", uselist=False)


