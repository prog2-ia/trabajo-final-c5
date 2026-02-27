from vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras,
                 tipo_coche, plazas, puertas, capacidad_maletero):

        super().__init__(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras)

        self.tipo_coche = tipo_coche
        self.plazas = plazas
        self.puertas = puertas
        self.capacidad_maletero = capacidad_maletero

    @classmethod
    def Alta_Coche(cls, dicc):
        return cls(dicc['matricula'], dicc['marca'], dicc['modelo'], dicc['anyo'], dicc['color'], dicc['kilometros'], dicc['tipo_combustible'],
                   dicc['consumo'], dicc['caballos'], dicc['autonomia'], dicc['precio_dia'],dicc['estado'], dicc['extras'], dicc['tipo_coche'],
                   dicc['plazas'], dicc['puertas'], dicc['capacidad_maletero'])