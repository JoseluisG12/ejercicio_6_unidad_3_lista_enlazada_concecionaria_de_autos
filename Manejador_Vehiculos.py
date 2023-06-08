from zope.interface import Interface
from zope.interface import implementer
from  abc import ABC, abstractmethod
from Clase_Nodo import Nodo
import unittest
import json
from Clase_vehiculo_usado import Vehivulo_usado
from Clase_Vehiculo_nuevo import Vehiculo_nuevo
"""la interfaz Icoleccion puede insertar un elemento
el la lista en una poscicion indicada siempre y cuando
este dentro de los limites de ella ta,puede agregar un
elemento al finala de la lista y mostrar un elemento 
segun una posicion especifica los metodos a utilizar son
insertarElemento ()
agregarElemento ()
mostrarElemento ()
"""
class IColeccion (Interface):
    @abstractmethod
    def insertarVehiculo (self,posicion):
        pass

    @abstractmethod
    def agregarvehiculo (self):
        pass

    @abstractmethod
    def mostrarVehiculo (self):
        pass

@implementer(IColeccion)
class Lista_vehiculos:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self)-> None:
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def __iter__(self):
        return self

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            vehiculos=[vehiculo.toJSON() for vehiculo in self.Lista_vehiculos()]
        )
        return d

    def cargaarchivo(self,encoder):
        vehiculos_json = encoder.leerJSONArchivo('vehiculos.json')
        for vehiculo_json in vehiculos_json["Lista_vehiculos"]:
            if vehiculo_json["__class__"] == "Vehiculo_usado":
                vehiculo = Vehivulo_usado(vehiculo_json["__atributos__"]["modelo"],
                                          vehiculo_json["__atributos__"]["cantidad_puertas"],
                                          vehiculo_json["__atributos__"]["color"],
                                          vehiculo_json["__atributos__"]["precio_base"],
                                          vehiculo_json["__atributos__"]["marca"],
                                          vehiculo_json["__atributos__"]["patente"],
                                          vehiculo_json["__atributos__"]["anio"],
                                          vehiculo_json["__atributos__"]["kilometraje"])
                self.agregarvehiculo(vehiculo)
            elif vehiculo_json["__class__"] == "Vehiculo_nuevo":
                vehiculo = Vehiculo_nuevo(vehiculo_json["__atributos__"]["modelo"],
                                          vehiculo_json["__atributos__"]["cantidad_puertas"],
                                          vehiculo_json["__atributos__"]["color"],
                                          vehiculo_json["__atributos__"]["precio_base"],
                                          vehiculo_json["__atributos__"]["marca"],
                                          vehiculo_json["__atributos__"]["version"])
                self.agregarvehiculo(vehiculo)

    def agregarvehiculo(self, vehiculo):
        nodo = Nodo(vehiculo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def insertarVehiculo(self,posicion):
        print("""ingrese el nuevo vehiculo a insertar """)
        modelo = input("ingrese el modelo del vehiculo\n")
        puertas  = int(input("ingrese la cantidad depuertas del vehiculo\n"))
        color = input("ingrese el color del vehiculo\n")
        precio = float(input("ingrese el precio base del vehiculo\n"))
        marca = input("ingrese la marca del vehiculo\n")
        dato = input("si el auto es nuevo ingrese (N) en caso de ser usado ingrese (U)\n)")
        if dato == 'U':
            patente = input("ingrese la patente\n")
            año = input("ingrese el año de fabrica del vehiculo\n")
            kilometraje = int(input("ingrese el kilometraje del vehiculo\n"))
            vehiculo = Vehivulo_usado(modelo,puertas,color,precio,marca,patente,año,kilometraje)
        elif dato == 'N':
            version = input("ingrese la version del vehiculo\n")
            vehiculo = Vehiculo_nuevo(modelo,puertas,color,precio,marca,version)
        nuevo_nodo = Nodo(vehiculo)

        if posicion == 1:#consultar porque no ingresa al primero hasta ingresar otro elemento y porque pierda cantidad de objetos al ingresar otro
            nuevo_nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nuevo_nodo
            self.__actual=nuevo_nodo
            self.__tope+=1
        else:
            nodo_anterior = self.__comienzo
            try:
                for i in range(posicion - 2):
                    nodo_anterior = nodo_anterior.getSiguiente()
                nuevo_nodo.setSiguiente(nodo_anterior.getSiguiente())
                nodo_anterior.setSiguiente(nuevo_nodo)
                self.__tope += 1
            except:
                print("Error la posicion se sale del rango de la lista")
    def insertarVehiculoposicion(self,posicion,vehiculo):
        nuevo_nodo = Nodo(vehiculo)

        if posicion == 1:#consultar porque no ingresa al primero hasta ingresar otro elemento y porque pierda cantidad de objetos al ingresar otro
            nuevo_nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nuevo_nodo
            self.__actual=nuevo_nodo
            self.__tope+=1
        else:
            nodo_anterior = self.__comienzo
            try:
                for i in range(posicion - 2):
                    nodo_anterior = nodo_anterior.getSiguiente()
                nuevo_nodo.setSiguiente(nodo_anterior.getSiguiente())
                nodo_anterior.setSiguiente(nuevo_nodo)
                self.__tope += 1
            except:
                print("Error la posicion se sale del rango de la lista")

    def crearunvehiculo(self):
        modelo = input("ingrese el modelo del vehiculo\n")
        puertas = int(input("ingrese la cantidad depuertas del vehiculo\n"))
        color = input("ingrese el color del vehiculo\n")
        precio = float(input("ingrese el precio base del vehiculo\n"))
        marca = input("ingrese la marca del vehiculo\n")
        dato = input("si el auto es nuevo ingrese (N) en caso de ser usado ingrese (U)\n)")
        if dato == 'U':
            patente = input("ingrese la patente\n")
            año = input("ingrese el año de fabrica del vehiculo\n")
            kilometraje = int(input("ingrese el kilometraje del vehiculo\n"))
            vehiculo = Vehivulo_usado(modelo, puertas, color, precio, marca, patente, año, kilometraje)
        elif dato == 'N':
            version = input("ingrese la version del vehiculo\n")
            vehiculo = Vehiculo_nuevo(modelo, puertas, color, precio, marca, version)
        return vehiculo

    def mostrarobjeto(self,posicion):

        aux = self.__comienzo
        contador = self.__tope
        encontrado = False
        if posicion == contador:
            print(type(self.__actual.getDato()))
            encontrado = True
        else:

            aux = aux.getSiguiente()
            while (not encontrado and aux != None and (posicion < self.__tope and posicion > 0) ):
                if posicion == contador:
                    encontrado = True
                else:
                    aux = aux.getSiguiente()
                    contador -= 1
            if encontrado:
                print(type(aux.getDato()))
                return contador
            else:
                print("no se encntro un objeto en la posicion indicada")


    def actualizarprecio(self,patente):

        aux = self.__comienzo
        contador = self.__tope
        encontrado = False
        while (not encontrado and aux != None):

            if isinstance(aux.getDato(), Vehivulo_usado):
                if aux.getDato().getpatente() == patente:
                    precio = float(input("ingrese el nuevo precio del vehiculo\n"))
                    aux.getDato().addprecio(precio)
                    print(f"el importe de venta del vehiculo es: ${aux.getDato().importeventa()}")
                    encontrado = True
                else:

                    aux = aux.getSiguiente()
                    while (not encontrado and aux != None):

                        if aux.getDato().getpatente() == patente:
                            encontrado = True
                        else:
                            aux = aux.getSiguiente()
                            contador -= 1
                    if encontrado:
                        precio = float(input("ingrese el nuevo precio del vehiculo\n"))
                        aux.getDato().addprecio(precio)
                        print(f"el importe de venta del vehiculo es: ${aux.getDato().importeventa()}")
                    else:
                        print(f"no se encntro el vehiculo con la patente{patente}")
            else:
                aux = aux.getSiguiente()
                contador -= 1

    def vehiculomaseconomico(self):
        min = 10000000000
        aux = self.__comienzo
        for i in range(self.__tope):
            if aux.getDato().importeventa() < min:
                min = aux.getDato().importeventa()
                minaux = aux.getDato()
                aux = aux.getSiguiente()
            else:
                aux = aux.getSiguiente()
        return minaux

    def mostrarVehiculo(self,vehiculo):
        if isinstance(vehiculo, Vehivulo_usado):
            print(f"""
        tipo usado
        modelo:{vehiculo.getmodelo()}
        cantidad de puertas: {vehiculo.getpuertas()}
        color:{vehiculo.getcolor()}
        marca: {vehiculo.getmarca()}
        patente: {vehiculo.getpatente()}
        año:{vehiculo.getaño()}
        kilometraje:{vehiculo.getkilometraje()}KM
        precio:${vehiculo.importeventa()}""")
        elif isinstance(vehiculo, Vehiculo_nuevo):
            print(f"""
        tipo nuevo
        modelo:{vehiculo.getmodelo()}
        cantidad de puertas: {vehiculo.getpuertas()}
        marca: {vehiculo.getmarca()}
        color:{vehiculo.getcolor()}
        precio:${vehiculo.importeventa()}
        version {vehiculo.getversion()}""")

    def autosdisonibles(self):
        aux = self.__comienzo

        for i in range(self.__tope):
            print(f"""
modelo:{aux.getDato().getmodelo()}
cantidad de puertas:{aux.getDato().getpuertas()} 
importe de venta:{aux.getDato().importeventa()}""")
            aux = aux.getSiguiente()

    def testinsercioninicio(self):
        vehiculo = Vehiculo_nuevo('fiat',4,'negro',500000,'ford','full')
        self.agregarvehiculo(vehiculo)
        aux = self.__comienzo
        for i in range(self.__tope):
            self.mostrarVehiculo(aux.getDato())

    def testinsercioniniciomedia(self,vehiculo):
        self.insertarVehiculoposicion(4,vehiculo)



    def testinsercioniniciofinal(self,vehivulo):
        self.insertarVehiculoposicion(9,vehivulo)
        aux = self.__comienzo


    def testverificaprecio(self,patente):
        aux = self.__comienzo
        contador = self.__tope
        encontrado = False
        while (not encontrado and aux != None):

            if isinstance(aux.getDato(), Vehivulo_usado):
                if aux.getDato().getpatente() == patente:
                    print(f"el nuevo importe para el test es : ${aux.getDato().importeventa()}")
                    encontrado = True
                else:

                    aux = aux.getSiguiente()
                    while (not encontrado and aux != None):
                        print("entra")
                        if aux.getDato().getpatente() == patente:
                            encontrado = True
                        else:
                            aux = aux.getSiguiente()
                            contador -= 1
                    if encontrado:
                        print(f"el nuevo importe para el test es : ${aux.getDato().importeventa()}")
                    else:
                        print(f"no se encntro el vehiculo con la patente{patente}")
            else:
                aux = aux.getSiguiente()
                contador -= 1

    def pruebatest(self):
        Mvehiculos = Lista_vehiculos()
        print("______test insertar vehiculo al inicio____")
        vehiculo = Vehiculo_nuevo('fiat', 4, 'negro', 500000, 'ford', 'full')
        Mvehiculos.agregarvehiculo(vehiculo)

        aux = self.__comienzo
        for i in range(self.__tope):
            self.mostrarVehiculo(aux.getDato())
        print("______test insertar vehiculo al medio____")
        self.testinsercioniniciomedia()
        print("______test insertar vehiculo al final____")
        self.testinsercioniniciofinal()
        print("______________agregar_un_vehiculo___________")
        vehiculo = Vehiculo_nuevo('hailux', 4, 'blaca', 4000000, 'toyota', 'full')
        self.agregarvehiculo(vehiculo)
        aux = self.__comienzo
        for i in range(self.__tope):
            self.mostrarVehiculo(aux.getDato())
        print("__________mostrar_objeto_por_posicion_y_comprara_inidice")
        posicion = 3
        indice = self.mostrarobjeto(posicion)
        if posicion == indice:
            print("poscicion ", posicion)
            print("indicie ", indice)
        print("_____buscar vehiculo usado por patente y actualizar el precio base y dar el importe de venta_________")
        patente = "AB128CD"
        self.actualizarprecio(patente)
        self.testverificaprecio(patente)

















