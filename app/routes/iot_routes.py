from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth_token import decode_token
from app.core.config import get_db

import app.crud.configuracion_iot_crud as crud
import app.schemas.configuracion_iot_schema as schemas


app = APIRouter()


@app.get(
    "/configuracion", response_model=schemas.ConfiguracionIOTResponse
)
def get_configuracion(
    db: Session = Depends(get_db)
):
    return crud.get_configuracion(db=db)


@app.put(
    "/configuracion",
    response_model=schemas.ConfiguracionIOTResponse
)
def update_configuracion(
    configuracion: schemas.ConfiguracionIOTUpdate,
    db: Session = Depends(get_db)
):
    return crud.actualizar_configuracion(
        db=db,
        configuracion=configuracion
    )