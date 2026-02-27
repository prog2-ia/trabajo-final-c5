from cliente import Cliente

class Casual(Cliente):
    def __init__(self, dni, nombre_completo, edad, carnets):

        super().__init__(dni, nombre_completo, edad, carnets)

    @classmethod
    def Alta_Casual(cls, dicc):
        return cls(dicc['dni'], dicc['nombre_completo'], dicc['edad'], dicc['carnets'])