from fastapi import APIRouter, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from app.core.auth_token import decode_token, Annotated
from app.core.config import SessionLocal, engine, get_db

from app.models.user_model import Base

import app.crud.user_crud as crud
import app.schemas.user_schemas as schemas

app = APIRouter()

@app.get("/list", dependencies=[Depends(decode_token)])
def list_users(db: Session = Depends(get_db)):
    users = crud.get_usuarios(db=db)
    return users

@app.get("/userId/{user_id}", dependencies=[Depends(decode_token)], response_model=schemas.UserBase)
def id_user(user_id: int, db: Session = Depends(get_db)):
    users = crud.get_usuario(db=db, user_id=user_id)
    if users is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return users

@app.post("/create", dependencies=[Depends(decode_token)], response_model=schemas.UserCreate)
def user_create(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.crear_usuario(db=db, user=user)

@app.put("/update/{user_id}", dependencies=[Depends(decode_token)], response_model=schemas.UserBase)
def user_update(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    users = crud.actualizar_usuario(db=db, user_id=user_id, user=user)
    if users is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return users

@app.get("/types", dependencies=[Depends(decode_token)])
def list_user_types(db: Session = Depends(get_db)):
    tipos = crud.get_tipos(db)
    return tipos


@app.get("/statuses", dependencies=[Depends(decode_token)])
def list_user_statuses(db: Session = Depends(get_db)):
    estados = crud.get_estados(db)
    return estados
