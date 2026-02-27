from clases.vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras,
                 tipo_moto, cilindrada, carnet_requerido):

        super().__init__(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras)

        self.tipo_moto = tipo_moto
        self.cilindrada = cilindrada
        self.carnet_requerido = carnet_requerido

    @classmethod
    def Alta_Moto(cls, dicc):
        return cls(dicc['matricula'], dicc['marca'], dicc['modelo'], dicc['anyo'], dicc['color'], dicc['kilometros'], dicc['tipo_combustible'],
                   dicc['consumo'], dicc['caballos'], dicc['autonomia'], dicc['precio_dia'], dicc['estado'], dicc['extras'], dicc['tipo_moto'],
                   dicc['cilindrada'], dicc['carnet_requerido'])