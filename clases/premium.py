from cliente import Cliente

#A partir de 500€ gastados.
class Premium(Cliente):
    def __init__(self, dni, nombre_completo, edad, carnets):

        super().__init__(dni, nombre_completo, edad, carnets)

        #Cada 100€ gastados son 15€ de descuento
        self.descueto_acumulado = 0

    @classmethod
    def Alta_Premium(cls, dicc):
        return cls(dicc['dni'], dicc['nombre_completo'], dicc['edad'], dicc['carnets'])