from clases.cliente import Cliente

#esta clase no se usa

#Cliente normal sin beneficios extra
class Casual(Cliente):
    def __init__(self, dni, nombre_completo, edad, carnets, direccion=''):

        super().__init__(dni, nombre_completo, edad, carnets, direccion)

    #Instancia la clase a partir de un diccionario JSON
    @classmethod
    def alta_casual(cls, dicc):
        return cls(dicc.get('dni'), dicc.get('nombre_completo'), dicc.get('edad'), dicc.get('carnets'), dicc.get('direccion', ''))