from abc import ABC, abstractmethod


class Vehiculo(ABC):
    def __init__(self, matricula: str, marca: str, modelo: str, anyo: int, color: str, kilometros: float,
                 tipo_combustible: str, consumo: float, caballos: int,
                 autonomia: float, precio_dia: float, estado: str, extras: str) -> None:
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.anyo = anyo
        self.color = color
        self.kilometros = kilometros
        self.tipo_combustible = tipo_combustible
        self.consumo = consumo
        self.caballos = caballos
        self.autonomia = autonomia
        self.__precio_dia = float(precio_dia)  # privado para no modificarlo directamente
        self.estado = estado
        self.extras = extras

    @property
    def precio_dia(self):
        return self.__precio_dia

    @precio_dia.setter
    def precio_dia(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio_dia = float(nuevo_precio)
        else:
            print('El precio debe ser positivo')

    @abstractmethod
    def calcular_tarifa(self, dias: int) -> float:
        # esto es para que las clases hijas implementen su propio metodo de calcular tarifa
        pass

    def __bool__(self) -> bool:
        if self.estado == 'Disponible':
            return True
        else:
            return False

    def __lt__(self, other) -> bool:
        if isinstance(other, Vehiculo):
            return self.precio_dia < other.precio_dia
        return NotImplemented

    def __gt__(self, other) -> bool:
        if isinstance(other, Vehiculo):
            return self.precio_dia > other.precio_dia
        return NotImplemented

    def __str__(self) -> str:
        return f'{self.marca} {self.modelo} [{self.matricula}] - {self.precio_dia}€/día'