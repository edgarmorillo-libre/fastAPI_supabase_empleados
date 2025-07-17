
from fastapi import FastAPI, HTTPException
from database import supabase_request
from models import Empleado, EmpleadoOut, EmpleadoUpdate

app = FastAPI()

# ✅ Crear empleado
@app.post("/empleados", response_model=EmpleadoOut)
async def crear_empleado(empleado: Empleado):
    data = await supabase_request("POST", "empleados", data=[empleado.dict()])
    return data[0]

# 🔍 Obtener todos los empleados
@app.get("/empleados", response_model=list[EmpleadoOut])
async def listar_empleados():
    data = await supabase_request("GET", "empleados")
    return data

# 🔎 Obtener un empleado por ID
@app.get("/empleados/{id}", response_model=EmpleadoOut)
async def obtener_empleado(id: int):
    data = await supabase_request("GET", "empleados", params={"id": f"eq.{id}"})
    if not data:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return data[0]

# 🛠️ Actualizar empleado
@app.put("/empleados/{id}", response_model=EmpleadoOut)
async def actualizar_empleado(id: int, empleado: EmpleadoUpdate):
    data = await supabase_request("PATCH", f"empleados?id=eq.{id}", data=[empleado.dict(exclude_unset=True)])
    if not data:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return data[0]

# 🗑️ Eliminar empleado
@app.delete("/empleados/{id}")
async def eliminar_empleado(id: int):
    data = await supabase_request("DELETE", "empleados", params={"id": f"eq.{id}"})
    if not data:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return {"mensaje": "Empleado eliminado"}


