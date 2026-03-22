from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos,
                 autonomia, precio_dia, estado, extras):
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
        self.__precio_dia = precio_dia #privado para no modificarlo directamente
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
    def calcular_tarifa(self, dias):
        #esto es para que las clases hijas implementen su propio metodo de calcular tarifa
        pass

    def __str__(self):
        return f'{self.marca} {self.modelo} [{self.matricula}] - {self.precio_dia}€/día'