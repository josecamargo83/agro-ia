from sqlalchemy import Column, Integer, String, Text, Numeric
from app.core.config import Base


class Cultivo(Base):
    __tablename__ = "cultivos"

    Cultivo_Id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    Cultivo_Nombre = Column(String(100), nullable=False, unique=True)
    Cultivo_Descripcion = Column(Text, nullable=True)

    Cultivo_PHMinimo = Column(Numeric(5, 2), nullable=True)
    Cultivo_PHMaximo = Column(Numeric(5, 2), nullable=True)

    Cultivo_HumedadMinima = Column(Numeric(5, 2), nullable=True)
    Cultivo_HumedadMaxima = Column(Numeric(5, 2), nullable=True)

    Cultivo_TemperaturaMinima = Column(Numeric(5, 2), nullable=True)
    Cultivo_TemperaturaMaxima = Column(Numeric(5, 2), nullable=True)