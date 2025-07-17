from pydantic import BaseModel, EmailStr
from typing import Optional

class Empleado(BaseModel):
    nombre: str
    correo: EmailStr
    edad: int
    salario: float

class EmpleadoOut(Empleado):
    id: int

class EmpleadoUpdate(BaseModel):
    nombre: Optional[str]
    correo: Optional[EmailStr]
    edad: Optional[int]
    salario: Optional[float]


