from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.cultivo_model import Cultivo
from app.schemas.cultivo_schema import (
    CultivoCreate,
    CultivoUpdate
)


def get_cultivos(db: Session):
    return db.query(Cultivo).all()


def get_cultivo(db: Session, cultivo_id: int):
    return db.query(Cultivo).filter(
        Cultivo.Cultivo_Id == cultivo_id
    ).first()


def crear_cultivo(db: Session, cultivo: CultivoCreate):

    existente = db.query(Cultivo).filter(
        Cultivo.Cultivo_Nombre == cultivo.Cultivo_Nombre
    ).first()

    if existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El cultivo ya existe"
        )

    db_cultivo = Cultivo(
        **cultivo.model_dump()
    )

    db.add(db_cultivo)
    db.commit()
    db.refresh(db_cultivo)

    return db_cultivo


def actualizar_cultivo(
    db: Session,
    cultivo_id: int,
    cultivo: CultivoUpdate
):

    db_cultivo = get_cultivo(db, cultivo_id)

    if not db_cultivo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cultivo no encontrado"
        )

    datos = cultivo.model_dump(exclude_unset=True)

    for campo, valor in datos.items():
        setattr(db_cultivo, campo, valor)

    db.commit()
    db.refresh(db_cultivo)

    return db_cultivo