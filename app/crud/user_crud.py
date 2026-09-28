from sqlalchemy.orm import Session
from app.models.user_model import Usuarios
from app.models.user_type_model import UserType
from app.models.user_status_model import UserStatus
from app.schemas.user_schemas import UserCreate, UserUpdate
from fastapi import HTTPException, status


def get_usuarios(db: Session):
    return db.query(Usuarios).all()


def get_usuario(db: Session, user_id: int):
    return db.query(Usuarios).filter(Usuarios.User_Id == user_id).first()


def get_usuario_por_username(db: Session, username: str):
    return db.query(Usuarios).filter(Usuarios.User_Name == username).first()

def crear_usuario(db: Session, user: UserCreate):
    # Verificar si ya existe un usuario con el mismo nombre de usuario
    existing_user = get_usuario_por_username(db, user.User_Name)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El nombre de usuario ya está registrado"
        )

    # Crear el usuario normalmente
    db_usuario = Usuarios(**user.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def actualizar_usuario(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(Usuarios).filter(Usuarios.User_Id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    # Verificar si el nuevo nombre de usuario ya está en uso por otro usuario
    existing_user = db.query(Usuarios).filter(
        Usuarios.User_Name == user.User_Name,
        Usuarios.User_Id != user_id
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El nombre de usuario ya está registrado por otro usuario"
        )

    # Actualizar los datos
    db_user.User_Id = user.User_Id
    db_user.User_Names = user.User_Names
    db_user.User_Mail = user.User_Mail
    db_user.User_Phone = user.User_Phone
    db_user.User_Name = user.User_Name
    db_user.User_Password = user.User_Password
    db_user.Usertype_Id = user.Usertype_Id
    db_user.Userstatus_Id = user.Userstatus_Id

    db.commit()
    db.refresh(db_user)
    return db_user




def get_tipos(db):
    tipos = db.query(UserType).all()
    return [{"value": t.Usertype_Id, "label": t.Usertype_Description} for t in tipos]

def get_estados(db: Session):
    tipos = db.query(UserStatus).all()
    return [{"value": t.Userstatus_Id, "label": t.Userstatus_Description} for t in tipos]
