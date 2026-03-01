class Cliente:
    total_gastado=0 #lo que ha gastado el cliente en todos sus alquileres juntos
    gastado_premium=0 #lo que lleva gastado desde que es premium(500€) y se empieza a contar y a hacer descuento de 15€ cada 100€
    total_ahorrado=0  #total ahorrado gracias a der 'premium'
    premium = False

    def __init__(self, dni, nombre_completo, edad, carnets):
        self.dni = dni
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.carnets = carnets

    @classmethod
    def Alta_Cliente(cls, dni, nombre_completo, edad, carnets):
        return cls(dni, nombre_completo, edad, *carnets)
