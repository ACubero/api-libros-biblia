from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

import pandas as pd
import json

def excel_a_json(archivo_excel, hoja_nombre, json_salida):
    # Leer el archivo Excel en un DataFrame de Pandas
    datos_excel = pd.read_excel(archivo_excel, sheet_name=hoja_nombre)
    
    # Convertir el DataFrame a un diccionario y luego a JSON
    datos_json = datos_excel.to_dict(orient='records')
    
    # Escribir el JSON a un archivo
    with open(json_salida, 'w') as archivo:
        json.dump(datos_json, archivo, indent=4)

# Nombre del archivo Excel de entrada
archivo_excel = './data/data.xlsx'

# Nombre de la hoja dentro del archivo Excel
hoja_nombre = 'Libros'

# Nombre del archivo JSON de salida
json_salida = './data/data.json'

# Llamar a la función para convertir el archivo Excel a JSON
excel_a_json(archivo_excel, hoja_nombre, json_salida)

print("Archivo JSON generado con éxito.")

def leer_json(ruta_json):
    with open(ruta_json, 'r') as archivo:
        datos_json = json.load(archivo)
    return datos_json

# Llamada a la función para leer el archivo JSON
contenido_json = leer_json(json_salida)
print(contenido_json)
app = FastAPI(debug=True)

@app.get("/")
def index():
    #return {"mensaje": "conectado"}
    return contenido_json

#@app.get("/libros/{id}")
#def detalleLibro(id: int):
#    return json[id]

#Para hacer un post
"""@app.post("/libros")
def insertarLibro(libro:Libro):
    return {"message":f"Libro {libro.titulo} insertado"}"""
    
