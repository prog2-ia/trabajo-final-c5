from abc import ABC, abstractmethod

#Clase base para todos los vehiculos
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
        self.__precio_dia = float(precio_dia)  #privado para no modificarlo directamente
        self.estado = estado
        self.extras = extras

    #Representacion formal para desarrollo
    def __repr__(self) -> str:
        return f"{type(self).__name__}(matricula='{self.matricula}', marca='{self.marca}', modelo='{self.modelo}')"

    #Metodo estatico de utilidad para formato de matricula
    @staticmethod
    def limpiar_matricula(matricula: str) -> str:
        return matricula.strip().upper()

    #Obtiene el precio por dia del vehiculo
    @property
    def precio_dia(self):
        return self.__precio_dia

    #Valida y establece el precio por dia
    @precio_dia.setter
    def precio_dia(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio_dia = float(nuevo_precio)
        else:
            raise ValueError('El precio debe ser positivo')

    #Metodo abstracto a implementar por los hijos
    @abstractmethod
    def calcular_tarifa(self, dias: int) -> float:
        #esto es para que las clases hijas implementen su propio metodo de calcular tarifa
        pass

    #Devuelve True si el vehiculo esta disponible
    def __bool__(self) -> bool:
        if self.estado == 'Disponible':
            return True
        else:
            return False

    #Compara si un vehiculo es mas barato que otro
    def __lt__(self, other) -> bool:
        if isinstance(other, Vehiculo):
            return self.precio_dia < other.precio_dia
        return NotImplemented

    #Compara si un vehiculo es mas caro que otro
    def __gt__(self, other) -> bool:
        if isinstance(other, Vehiculo):
            return self.precio_dia > other.precio_dia
        return NotImplemented

    #Representacion en texto del vehiculo
    def __str__(self) -> str:
        return f'{self.marca} {self.modelo} [{self.matricula}] - {self.precio_dia}€/día'