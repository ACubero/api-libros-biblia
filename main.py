from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

libro = {}

class Libro(BaseModel):
    id: int
    titulo: str
    escritor: str
    capitulos: Optional[int]

def crearLibro(id,titulo,escritor,capitulos):
    libro[id] = {"id":id,"titulo":titulo,"escritor":escritor,"capitulos":capitulos}

crearLibro(1,"Genesis","Moises",67)
crearLibro(2,"Exodo","Moises",43)
crearLibro(3,"Levitico","Moises",21)
print(libro)
app = FastAPI(debug=True)

@app.get("/")
def index():
    return {"mensaje": "conectado"}
    #return libro

@app.get("/libros/{id}")
def detalleLibro(id: int):
    return libro[id]

#Para hacer un post
"""@app.post("/libros")
def insertarLibro(libro:Libro):
    return {"message":f"Libro {libro.titulo} insertado"}"""
    
