from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.auth_token import decode_token, encode_token, Annotated
from app.core.config import get_db

import app.crud.auth_validacion as crud
import app.schemas.auth_schemas as schemas

app = APIRouter()

@app.post("/login")
def login(user_data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = crud.login_user(db, user_data.username, user_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    token = encode_token({"username": user.User_Name})
    #return {"access_token": token, "token_type": "bearer"}
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "User_Id": user.User_Id,
            "User_Names": user.User_Names,
            "Usertype_Id": user.Usertype_Id
        }
    }
