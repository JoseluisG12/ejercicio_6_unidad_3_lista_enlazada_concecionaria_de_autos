from Clase_vehiculo_usado import Vehivulo_usado
from Clase_Vehiculo_nuevo import Vehiculo_nuevo
import json
class Menu:
    __switcher = None

    def __init__(self)->None:
        self.__switcher = {1:self.op1,
                           2:self.op2,
                           3:self.op3,
                           4:self.op4,
                           5:self.op5,
                           6:self.op6,
                           66:self.op66
                           }

    def run(self,Mvehiculos,encoder):
        band = True
        while band:
            b = int(input("""
Menu Principal:
1- insertar un vehiculo en una posicion indicada
2- agregar un vehiculo a la coleccion
3- mostrar el tipo de objeto almacenado en una posisicion
4- buscar vehiculo usado por patente y actualizar el precio base y dar el importe de venta 
5- mostrar vehiculo disponible mas economico
6- mostrar todos los autos disponibles
0-
\n"""))
            func = self.__switcher.get(b)
            if func:
                func(Mvehiculos,encoder)
            else:
                print("Saliendo...")
                band = False

    def op1(self,Mvehiculos,encoder):
        posicion = int(input("ingrese la posicion a insertar el vehiculo\n"))
        Mvehiculos.insertarVehiculo(posicion)
    def op2(self,Mvehiculos,encoder):
        print("agregar un vehiculo a la lista")
        vehiculo = Mvehiculos.crearunvehiculo()
        Mvehiculos.agregarvehiculo(vehiculo)

    def op3(self,Mvehiculos,encoder):
        posicion = int(input("ingrese la posicion del obejeto a mostrar\n")) + 1
        Mvehiculos.mostrarobjeto(posicion)

    def op4(self,Mvehiculos,encoder):
        patente = input("ingrese la pantente del vehiculo a actulalizar el precio\n")
        Mvehiculos.actualizarprecio(patente)

    def op5(self,Mvehiculos,encoder):
        vehiculo = Mvehiculos.vehiculomaseconomico()
        print("vehiculo mas economico:")
        Mvehiculos.mostrarVehiculo(vehiculo)

    def op6(self,Mvehiculos,encoder):
        Mvehiculos.autosdisonibles()





    def op66(self,Mvehiculos,encoder):
        for dato in Mvehiculos:
            print(f"dato del {dato.getmarca()} precio {dato.getprecio()},")
