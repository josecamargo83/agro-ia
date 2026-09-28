from sqlalchemy import Column, Integer, String
from app.core.config import Base

class UserStatus(Base):
    __tablename__ = "user_status"

    Userstatus_Id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Userstatus_Description = Column(String(25), nullable=False)
