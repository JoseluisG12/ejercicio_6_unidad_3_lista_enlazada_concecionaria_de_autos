from Clase_Vehiculo import Vehiculo
class Vehiculo_nuevo(Vehiculo):
    __version : str

    def __init__(self,modelo,cantidad,color,precio,marca,version)->None:
        Vehiculo.__init__(self,modelo,cantidad,color,precio,marca)
        self.__version = version

    def importeventa(self):
        precio_base = super().getprecio()
        precio_base = precio_base + ((10 * precio_base)/100)
        if self.__version == 'full':
            precio_base = precio_base + ((2 * precio_base)/100)

        super().addprecio(precio_base)
        return precio_base

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                modelo=super().getmodelo(),
                cantidad_puertas=super().getpuertas(),
                color=super().getcolor(),
                precio_base=super().getprecio(),
                marca=super().getmarca(),
                version=self.__version,

            )
        )
        return d

    def getversion(self):
        return self.__version
