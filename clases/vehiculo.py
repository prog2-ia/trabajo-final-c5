class Vehiculo:
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
        self.precio_dia = float(precio_dia)
        self.estado = estado
        self.extras = extras


    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.precio_dia}€/día"