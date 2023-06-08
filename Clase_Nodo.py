from Clase_Vehiculo import  Vehiculo
class Nodo:
    __viehiculo: Vehiculo
    __siguiente: object

    def __init__(self, Vehiculo)-> None:
        self.__viehiculo = Vehiculo
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__viehiculo