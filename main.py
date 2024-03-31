from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


class Libro(BaseModel):
    id: int
    titulo: str
    escritor: str
    capitulos: Optional[int]

libro = {}

def crearLibro(libro,id,titulo,escritor,capitulos):
    libro[id] = {
        "titulo": titulo,
        "escritor": escritor,
        "capitulos": capitulos
    }
    return libro

crearLibro(libro,1,"Genesis","Moises",67)
crearLibro(libro,2,"Exodo","Moises",43)
crearLibro(libro,3,"Levitico","Moises",21)
crearLibro(libro,4,"Deuteronomio","Moises",23)
print(libro)
app = FastAPI(debug=True)

@app.get("/")
def index():
    #return {"mensaje": "conectado"}
    return libro

@app.get("/libros/{id}")
def detalleLibro(id: int):
    return libro[id]

#Para hacer un post
"""@app.post("/libros")
def insertarLibro(libro:Libro):
    return {"message":f"Libro {libro.titulo} insertado"}"""
    
