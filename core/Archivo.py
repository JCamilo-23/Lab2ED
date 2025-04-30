from core.Funcion import Funcion
from core.Asiento import Asiento

from core.Funcion import Funcion

class Archivo:
    def __init__(self, ruta, salas_dict):
        self.ruta = ruta
        self.salas_dict = salas_dict
        self.funciones = []

    def cargar(self):
        self.funciones.clear()
        with open(self.ruta, encoding="utf-8") as f:
            for linea in f:
                if linea.strip().startswith("#") or not linea.strip():
                    continue
                sala_id, nombre, hora, imagen = linea.strip().split(";")
                sala = self.salas_dict.get(sala_id)
                if sala:
                    self.funciones.append(Funcion(sala, nombre, hora, True, imagen))

