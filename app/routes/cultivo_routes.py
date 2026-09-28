from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.auth_token import decode_token
from app.core.config import get_db

import app.crud.cultivo_crud as crud
import app.schemas.cultivo_schema as schemas


app = APIRouter()


@app.get("/list", dependencies=[Depends(decode_token)])
def list_cultivos(db: Session = Depends(get_db)):
    return crud.get_cultivos(db=db)


@app.get(
    "/{cultivo_id}",
    dependencies=[Depends(decode_token)],
    response_model=schemas.CultivoResponse
)
def get_cultivo(
    cultivo_id: int,
    db: Session = Depends(get_db)
):

    cultivo = crud.get_cultivo(
        db=db,
        cultivo_id=cultivo_id
    )

    if cultivo is None:
        raise HTTPException(
            status_code=404,
            detail="Cultivo no encontrado"
        )

    return cultivo


@app.post(
    "/create",
    dependencies=[Depends(decode_token)],
    response_model=schemas.CultivoResponse
)
def create_cultivo(
    cultivo: schemas.CultivoCreate,
    db: Session = Depends(get_db)
):
    return crud.crear_cultivo(
        db=db,
        cultivo=cultivo
    )


@app.put(
    "/update/{cultivo_id}",
    dependencies=[Depends(decode_token)],
    response_model=schemas.CultivoResponse
)
def update_cultivo(
    cultivo_id: int,
    cultivo: schemas.CultivoUpdate,
    db: Session = Depends(get_db)
):
    return crud.actualizar_cultivo(
        db=db,
        cultivo_id=cultivo_id,
        cultivo=cultivo
    )