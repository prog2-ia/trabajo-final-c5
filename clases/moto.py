from clases.vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras,
                 tipo_moto, cilindrada, carnet_requerido):

        super().__init__(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras)

        self.tipo_moto = tipo_moto
        self.cilindrada = cilindrada
        self.carnet_requerido = carnet_requerido

    def calcular_tarifa(self, dias):
        #tienen un descuento del 10% sobre el precio base
        return (self.precio_dia * dias) * 0.9

    @classmethod
    def alta_moto(cls, dicc):
        return cls(**dicc)