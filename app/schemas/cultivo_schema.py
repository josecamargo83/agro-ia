from pydantic import BaseModel
from typing import Optional


class CultivoBase(BaseModel):
    Cultivo_Nombre: str
    Cultivo_Descripcion: Optional[str] = None

    Cultivo_PHMinimo: Optional[float] = None
    Cultivo_PHMaximo: Optional[float] = None

    Cultivo_HumedadMinima: Optional[float] = None
    Cultivo_HumedadMaxima: Optional[float] = None

    Cultivo_TemperaturaMinima: Optional[float] = None
    Cultivo_TemperaturaMaxima: Optional[float] = None


class CultivoCreate(CultivoBase):
    pass


class CultivoUpdate(BaseModel):
    Cultivo_Nombre: Optional[str] = None
    Cultivo_Descripcion: Optional[str] = None

    Cultivo_PHMinimo: Optional[float] = None
    Cultivo_PHMaximo: Optional[float] = None

    Cultivo_HumedadMinima: Optional[float] = None
    Cultivo_HumedadMaxima: Optional[float] = None

    Cultivo_TemperaturaMinima: Optional[float] = None
    Cultivo_TemperaturaMaxima: Optional[float] = None


class CultivoResponse(CultivoBase):
    Cultivo_Id: int

    class Config:
        from_attributes = True