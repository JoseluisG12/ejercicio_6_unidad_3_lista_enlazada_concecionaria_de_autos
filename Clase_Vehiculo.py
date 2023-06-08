
import json
from pathlib import Path
class Vehiculo:
    __modelo : str
    __cantidad_puertas : int
    __color : str
    __precio_base : float
    __marca : str

    def __init__(self,modelo,cantidad,color,precio,marca)->None:
        self.__modelo = modelo
        self.__cantidad_puertas = cantidad
        self.__color = color
        self.__precio_base = float(precio)
        self.__marca = marca

    def getprecio(self):
        return self.__precio_base

    def addprecio(self,precio):
        self.__precio_base = precio

    def getmarca(self):
        return self.__marca

    def getmodelo(self):
        return self.__modelo

    def getpuertas(self):
        return self.__cantidad_puertas

    def getcolor(self):
        return self.__color








