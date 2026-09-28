from pydantic import BaseModel
from typing import Optional


# --- Submodelos (para relaciones) ---
class UserTypeBase(BaseModel):
    Usertype_Id: int
    Usertype_Description: str

    class Config:
        orm_mode = True


class UserStatusBase(BaseModel):
    Userstatus_Id: int
    Userstatus_Description: str

    class Config:
        orm_mode = True


# --- Modelos principales ---
class UserBase(BaseModel):
    User_Id: int
    User_Names: str
    User_Mail: str
    User_Phone: Optional[str] = None
    User_Name: str
    User_Password: str
    Usertype_Id: Optional[int] = None
    Userstatus_Id: Optional[int] = None

    # Relaciones (para mostrar el nombre del tipo y estado)
    tipo: Optional[UserTypeBase] = None
    estado: Optional[UserStatusBase] = None

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    User_Id: int
    User_Names: str
    User_Mail: str
    User_Phone: Optional[str] = None
    User_Name: str
    User_Password: str
    Usertype_Id: Optional[int] = None
    Userstatus_Id: Optional[int] = None


class UserUpdate(BaseModel):
    User_Id: int
    User_Names: Optional[str] = None
    User_Mail: Optional[str] = None
    User_Phone: Optional[str] = None
    User_Name: Optional[str] = None
    User_Password: Optional[str] = None
    Usertype_Id: Optional[int] = None
    Userstatus_Id: Optional[int] = None
