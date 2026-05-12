from clases.vehiculo import Vehiculo

#Vehiculo de cuatro ruedas con maletero
class Coche(Vehiculo):
    def __init__(self, matricula: str, marca: str, modelo: str, anyo: int, color: str, kilometros: float, tipo_combustible: str, consumo: float, caballos: int, autonomia: float, precio_dia: float, estado: str, extras: str,
                 tipo_coche: str, plazas: int, puertas: int, capacidad_maletero: float, carnet_requerido: str) -> None:

        super().__init__(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras)

        self.tipo_coche = tipo_coche
        self.plazas = plazas
        self.puertas = puertas
        self.capacidad_maletero = capacidad_maletero
        self.carnet_requerido = carnet_requerido

    def calcular_tarifa(self, dias):
        #Tarifa plana para coches
        return self.precio_dia * dias

    #Instancia la clase a partir de un diccionario JSON
    @classmethod
    def alta_coche(cls, dicc):
        return cls(**dicc)