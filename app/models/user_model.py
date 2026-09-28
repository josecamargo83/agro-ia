from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, Text
from app.core.config import Base

class Usuarios(Base):
    __tablename__ = "user"  

    User_Id = Column(Integer, primary_key=True, index=True)
    User_Names = Column(String(20), nullable=False)
    User_Mail = Column(String(20), nullable=False)
    User_Phone = Column(String(20), nullable=True)
    User_Name = Column(String(20), nullable=False, unique=True, index=True)  # login
    User_Password = Column(String(20), nullable=False)

    Usertype_Id = Column(Integer, ForeignKey("user_type.Usertype_Id"))
    Userstatus_Id = Column(Integer, ForeignKey("user_status.Userstatus_Id"))