from sqlalchemy import Column, Integer, String
from app.core.config import Base

class UserType(Base):
    __tablename__ = "user_type"

    Usertype_Id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Usertype_Description = Column(String(25), nullable=False)
