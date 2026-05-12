from clases.vehiculo import Vehiculo

#Vehiculo de carga pesada
class Furgoneta(Vehiculo):
    def __init__(self, matricula: str, marca: str, modelo: str, anyo: int, color: str, kilometros: float, tipo_combustible: str, consumo: float, caballos: int, autonomia: float, precio_dia: float, estado: str, extras: str,
                 tipo_furgoneta: str, capacidad_carga: str, carnet_requerido: str) -> None:

        super().__init__(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras)
        self.tipo_furgoneta = tipo_furgoneta
        self.capacidad_carga = capacidad_carga
        self.carnet_requerido = carnet_requerido

    def calcular_tarifa(self, dias):
        #tiene un cargo extra por ser furgoneta, ya que necesitan más mantenimiento...
        return (self.precio_dia * dias) + 10

    #Instancia la clase a partir de un diccionario JSON
    @classmethod
    def alta_furgoneta(cls, dicc):
        return cls(**dicc)