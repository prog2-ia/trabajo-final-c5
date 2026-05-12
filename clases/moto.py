from clases.vehiculo import Vehiculo

#Vehiculo de dos ruedas con descuento
class Moto(Vehiculo):
    def __init__(self, matricula: str, marca: str, modelo: str, anyo: int, color: str, kilometros: float, tipo_combustible: str, consumo: float, caballos: int, autonomia: float, precio_dia: float, estado: str, extras: str,
                 tipo_moto: str, cilindrada: int, carnet_requerido: str) -> None:

        super().__init__(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras)

        self.tipo_moto = tipo_moto
        self.cilindrada = cilindrada
        self.carnet_requerido = carnet_requerido

    def calcular_tarifa(self, dias):
        #tienen un descuento del 10% sobre el precio base
        return (self.precio_dia * dias) * 0.9

    #Instancia la clase a partir de un diccionario JSON
    @classmethod
    def alta_moto(cls, dicc):
        return cls(**dicc)