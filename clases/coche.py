from clases.vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras,
                 tipo_coche, plazas, puertas, capacidad_maletero, carnet_requerido):

        super().__init__(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras)

        self.tipo_coche = tipo_coche
        self.plazas = plazas
        self.puertas = puertas
        self.capacidad_maletero = capacidad_maletero
        self.carnet_requerido = carnet_requerido

    def calcular_tarifa(self, dias):
        # Polimorfismo: tarifa plana para coches
        return self.precio_dia * dias

    @classmethod
    def alta_coche(cls, dicc):
        return cls(**dicc)