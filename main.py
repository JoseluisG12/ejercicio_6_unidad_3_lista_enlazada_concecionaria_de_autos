import json
from ObjectEncoder import ObjectEncoder
from Manejador_Vehiculos import Lista_vehiculos
from Clase_Vehiculo_nuevo import Vehiculo_nuevo
from Clase_vehiculo_usado import Vehivulo_usado
from Clase_Menu import Menu
import unittest
from Clase_Nodo import Nodo


class TestListaVehiculos(unittest.TestCase):
    def setUp(self):
        Mvehiculos = Lista_vehiculos()
        encoder = ObjectEncoder()
        Mvehiculos.cargaarchivo(encoder)
        self.lista = Mvehiculos
    def setUp2(self):
        self.vehiculo = Vehivulo_usado('fiat', 4, 'negro', 500000, 'ford', "AB126CD",2018,25000)
    def test_insertar_final(self):
        #______test insertar vehiculo al final___
        vehiculo = Vehiculo_nuevo('fiat', 4, 'negro', 500000, 'ford', 'full')
        self.lista.testinsercioniniciofinal(vehiculo)
        self.assertIn(vehiculo, self.lista)

    def test_inserta_medio(self):
        #______test insertar vehiculo al medio____
        vehiculo = Vehiculo_nuevo('fiat', 4, 'negro', 500000, 'ford', 'full')
        self.lista.testinsercioniniciomedia(vehiculo)
        self.assertIn(vehiculo, self.lista)

    def test_insertar_vehiculo(self):
        #______test insertar vehiculo al inicio____
        vehiculo = Vehiculo_nuevo('fiat', 4, 'negro', 500000, 'ford', 'full')
        self.lista.insertarVehiculoposicion(1, vehiculo)
        self.assertIn(vehiculo, self.lista)

    def test_agregar_vehiculo(self):
        vehiculo = Vehiculo_nuevo('fiat', 4, 'negro', 500000, 'ford', 'full')
        self.lista.agregarvehiculo(vehiculo)
        self.assertIn(vehiculo, self.lista)

    def test_verificar_objeto_en_posicicon(self):
        posicion = 2
        self.assertTrue(posicion == self.lista.mostrarobjeto(posicion))

    def test_precio_venta(self):
        self.vehiculo = Vehivulo_usado('fiat', 4, 'negro', 500000, 'ford', "AB126CD", 2018, 25000)
        patente = 'AB126CD'
        self.lista.actualizarprecio(patente)
        self.assertEquals(self.vehiculo.getprecio(),500000.0)


if __name__ == '__main__':
    b = input("desea hacer el test ingrese y ingrese n si no desea no hacer el test")
    if b == 'y':
        unittest.main()
    else:
        Mvehiculos = Lista_vehiculos()
        encoder = ObjectEncoder()
        Mvehiculos.cargaarchivo(encoder)
        menu = Menu()
        menu.run(Mvehiculos, encoder)
        lista = Mvehiculos.toJSON()
        encoder.guardarJSONArchivo(lista, 'vehiculos.json')
        print('Datos guardados.')
        print(lista)