from sqlalchemy.orm import Session
from app.models.user_model import Usuarios
import app.schemas
from app.schemas.user_schemas import UserUpdate

def login_user(db: Session, username: str, password: str):
    usuario = db.query(Usuarios).filter(Usuarios.User_Name  == username, Usuarios.User_Password == password).first()
    return usuario

def user_by_username(db: Session, username: str):
    return db.query(Usuarios).filter(Usuarios.User_Name == username).first()