
from fastapi import FastAPI, HTTPException
from database import supabase_request
from models import Empleado, EmpleadoOut, EmpleadoUpdate
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir peticiones desde el frontend en localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #http://localhost:3000 O ["*"] si quieres permitir todos
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos: GET, POST, PUT, DELETE...
    allow_headers=["*"],  # Permite todos los headers
)

# ✅ Crear empleado
@app.post("/empleados", response_model=EmpleadoOut)
async def crear_empleado(empleado: Empleado):
    data = await supabase_request("POST", "empleados", data=[empleado.dict()])
    print("===Respuesta cruda de supabase:====", data)
    if not data:
        raise HTTPException(status_code=500, detail="Supabase no devolvió datos del nuevo empleado")
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


