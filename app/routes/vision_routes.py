from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
import os
import shutil

from sqlalchemy.orm import Session

from app.services.yolo_service import analizar_imagen

from app.core.auth_token import decode_token
from app.core.config import get_db

import app.crud.deteccion_vision_crud as crud
import app.schemas.deteccion_vision_schema as schemas


app = APIRouter()


@app.get(
    "/list",
    response_model=list[schemas.DeteccionVisionResponse]
)
def list_detecciones(
    db: Session = Depends(get_db)
):
    return crud.get_detecciones(db=db)


@app.get(
    "/{deteccion_id}",
    response_model=schemas.DeteccionVisionResponse
)
def get_deteccion(
    deteccion_id: int,
    db: Session = Depends(get_db)
):

    deteccion = crud.get_deteccion(
        db=db,
        deteccion_id=deteccion_id
    )

    if deteccion is None:
        raise HTTPException(
            status_code=404,
            detail="Detección no encontrada"
        )

    return deteccion


@app.post(
    "/create",
    response_model=schemas.DeteccionVisionResponse
)
def create_deteccion(
    deteccion: schemas.DeteccionVisionCreate,
    db: Session = Depends(get_db)
):

    return crud.crear_deteccion(
        db=db,
        deteccion=deteccion
    )


@app.post(
    "/analizar"
)
def analizar_vision(
    archivo: UploadFile = File(...),
    lote_id: int | None = Form(None),
    db: Session = Depends(get_db)
):

    # ========================================================
    # VALIDAR EXTENSIÓN
    # ========================================================

    extensiones_permitidas = [
        ".jpg",
        ".jpeg",
        ".png"
    ]

    extension = os.path.splitext(
        archivo.filename
    )[1].lower()

    if extension not in extensiones_permitidas:
        raise HTTPException(
            status_code=400,
            detail="Solo se permiten imágenes JPG, JPEG o PNG"
        )

    # ========================================================
    # CREAR CARPETA DE IMÁGENES
    # ========================================================

    carpeta = "uploads/vision"

    os.makedirs(
        carpeta,
        exist_ok=True
    )

    # ========================================================
    # GUARDAR IMAGEN
    # ========================================================

    archivo_path = os.path.join(
        carpeta,
        archivo.filename
    )

    with open(archivo_path, "wb") as buffer:

        shutil.copyfileobj(
            archivo.file,
            buffer
        )

    # ========================================================
    # EJECUTAR YOLO
    # ========================================================

    detecciones = analizar_imagen(
        archivo_path
    )

    # ========================================================
    # GUARDAR DETECCIONES EN BASE DE DATOS
    # ========================================================

    detecciones_guardadas = []

    for deteccion in detecciones:

        nueva_deteccion = schemas.DeteccionVisionCreate(
            Lote_Id=lote_id,
            Deteccion_Archivo=archivo.filename,
            Deteccion_Clase=deteccion["clase"],
            Deteccion_Confianza=deteccion["confianza"],
            Deteccion_XMin=deteccion["x_min"],
            Deteccion_YMin=deteccion["y_min"],
            Deteccion_XMax=deteccion["x_max"],
            Deteccion_YMax=deteccion["y_max"]
        )

        deteccion_guardada = crud.crear_deteccion(
            db=db,
            deteccion=nueva_deteccion
        )

        detecciones_guardadas.append(
            deteccion_guardada
        )

    # ========================================================
    # RESPUESTA
    # ========================================================

    return {
        "archivo": archivo.filename,
        "cantidad_detecciones": len(detecciones_guardadas),
        "detecciones": [
            {
                "id": deteccion.Deteccion_Id,
                "clase": deteccion.Deteccion_Clase,
                "confianza": float(
                    deteccion.Deteccion_Confianza
                ),
                "x_min": deteccion.Deteccion_XMin,
                "y_min": deteccion.Deteccion_YMin,
                "x_max": deteccion.Deteccion_XMax,
                "y_max": deteccion.Deteccion_YMax
            }
            for deteccion in detecciones_guardadas
        ]
    }
