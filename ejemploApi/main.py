from typing import Union

from fastapi import FastAPI
from funciones import mostrarTexto
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/ejemplo")
def ejemplo_paquete():
    retorno = mostrarTexto()
    return {"mensaje" : retorno}