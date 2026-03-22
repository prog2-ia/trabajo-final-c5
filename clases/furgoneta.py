from clases.vehiculo import Vehiculo

class Furgoneta(Vehiculo):
    def __init__(self, matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras,
                 tipo_furgoneta, capacidad_carga, carnet_requerido):

        super().__init__(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras)
        self.tipo_furgoneta = tipo_furgoneta
        self.capacidad_carga = capacidad_carga
        self.carnet_requerido = carnet_requerido

    def calcular_tarifa(self, dias):
        #tiene un cargo extra por ser furgoneta, ya que necesitan más mantenimiento...
        return (self.precio_dia * dias) + 10

    @classmethod
    def alta_furgoneta(cls, dicc):
        return cls(**dicc)