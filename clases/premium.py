from clases.cliente import Cliente

#esta clase no se usa

#A partir de 500€ gastados.
#Cliente con descuentos exclusivos
class Premium(Cliente):
    def __init__(self, dni, nombre_completo, edad, carnets, direccion=''):

        super().__init__(dni, nombre_completo, edad, carnets, direccion)

        #Cada 100€ gastados son 15€ de descuento
        self.descueto_acumulado = 0

    #Instancia la clase a partir de un diccionario JSON
    @classmethod
    def Alta_Premium(cls, dicc):
        return cls(dicc.get('dni'), dicc.get('nombre_completo'), dicc.get('edad'), dicc.get('carnets'), dicc.get('direccion', ''))