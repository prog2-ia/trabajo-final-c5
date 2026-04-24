from clases.cliente import Cliente

#esta clase no se usa

class Casual(Cliente):
    def __init__(self, dni, nombre_completo, edad, carnets):

        super().__init__(dni, nombre_completo, edad, carnets)

    @classmethod
    def alta_casual(cls, dicc):
        return cls(dicc['dni'], dicc['nombre_completo'], dicc['edad'], dicc['carnets'])