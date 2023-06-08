import datetime
from Clase_Vehiculo import Vehiculo
class Vehivulo_usado(Vehiculo):
    __patente : str
    __año : int
    __kilometraje : int

    def __init__(self,modelo,cantidad,color,precio,marca,patente,año,kilometraje)->None:
        Vehiculo.__init__(self,modelo,cantidad,color,precio,marca)
        self.__patente = patente
        self.__año = int(año)
        self.__kilometraje = int(kilometraje)

    def importeventa(self):
        años = int(((datetime.datetime.now().year) - self.__año))
        porcentaje_antiguedat = años * (1 / 100)
        precio_base = super().getprecio() - porcentaje_antiguedat
        importe = precio_base * (1 - 0.01 * años)
        if self.__kilometraje > 100000:
            importe -= 0.02 * precio_base
        return round(importe, 1)

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                modelo=super().getmodelo(),
                cantidad_puertas=super().getpuertas(),
                color=super().getcolor(),
                precio_base=super().getprecio(),
                marca=super().getmarca(),
                patente=self.__patente,
                anio=self.__año,
                kilometraje=self.__kilometraje

            )
        )
        return d

    def getpatente(self):
        return self.__patente

    def getaño(self):
        return self.__año

    def getkilometraje(self):
        return self.__kilometraje

