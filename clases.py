'''Clases:

- Vehiculo
    - Coche
    - Moto
    - Furgoneta

- Cliente
    - Premium
    - Casual

- Reserva
- Factura

- Empresa
'''


class Vehiculo:
    def __init__(self, matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras):
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
        self.precio_dia = precio_dia
        self.estado = estado
        self.extras = extras


class Coche(Vehiculo):
    def __init__(self, matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras,
                 tipo_coche, plazas, puertas, capacidad_maletero):

        super().__init__(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras)

        self.tipo_coche = tipo_coche
        self.plazas = plazas
        self.puertas = puertas
        self.capacidad_maletero = capacidad_maletero

    @classmethod
    def Alta_Coche(cls, dicc):
        return cls(dicc['matricula'], dicc['marca'], dicc['modelo'], dicc['anyo'], dicc['color'], dicc['kilometros'], dicc['tipo_combustible'],
                   dicc['consumo'], dicc['caballos'], dicc['autonomia'], dicc['precio_dia'],dicc['estado'], dicc['extras'], dicc['tipo_coche'],
                   dicc['plazas'], dicc['puertas'], dicc['capacidad_maletero'])


class Moto(Vehiculo):
    def __init__(self, matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras,
                 tipo_moto, cilindrada, carnet_requerido):

        super().__init__(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras)

        self.tipo_moto = tipo_moto
        self.cilindrada = cilindrada
        self.carnet_requerido = carnet_requerido

    @classmethod
    def Alta_Moto(cls, dicc):
        return cls(dicc['matricula'], dicc['marca'], dicc['modelo'], dicc['anyo'], dicc['color'], dicc['kilometros'], dicc['tipo_combustible'],
                   dicc['consumo'], dicc['caballos'], dicc['autonomia'], dicc['precio_dia'], dicc['estado'], dicc['extras'], dicc['tipo_moto'],
                   dicc['cilindrada'], dicc['carnet_requerido'])


class Furgoneta(Vehiculo):
    def __init__(self, matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras,
                 tipo_furgoneta, capacidad_carga, carnet_requerido):

        super().__init__(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras)
        self.tipo_furgoneta = tipo_furgoneta
        self.capacidad_carga = capacidad_carga
        self.carnet_requerido = carnet_requerido

    @classmethod
    def Alta_Furgoneta(cls, dicc):
        return cls(dicc['matricula'], dicc['marca'], dicc['modelo'], dicc['anyo'], dicc['color'], dicc['kilometros'], dicc['tipo_combustible'],
                   dicc['consumo'], dicc['caballos'], dicc['autonomia'], dicc['precio_dia'], dicc['estado'], dicc['extras'], dicc['tipo_furgoneta'],
                   dicc['capacidad_carga'], dicc['carnet_requerido'])


class Cliente:
    def __init__(self, dni, nombre_completo, edad, carnets):
        self.dni = dni
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.carnets = carnets


class Casual(Cliente):
    def __init__(self, dni, nombre_completo, edad, carnets):

        super().__init__(dni, nombre_completo, edad, carnets)

    @classmethod
    def Alta_Casual(cls, dicc):
        return cls(dicc['dni'], dicc['nombre_completo'], dicc['edad'], dicc['carnets'])

#Apartir de 500€ gastados.
class Premium(Cliente):
    def __init__(self, dni, nombre_completo, edad, carnets):

        super().__init__(dni, nombre_completo, edad, carnets)

        #Cada 100€ gastados son 15€ de descuento
        self.descueto_acumulado = 0

    @classmethod
    def Alta_Premium(cls, dicc):
        return cls(dicc['dni'], dicc['nombre_completo'], dicc['edad'], dicc['carnets']

class Alquiler:
    def __init__(self, cliente, vehiculo, precio):
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.precio = precio

        if vehiculo.estado != 'disponible':
            raise Exception('Vehiculo no disponible')

        vehiculo.estado = 'alquilado'

    