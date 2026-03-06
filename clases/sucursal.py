from clases.empresa import Empresa

class Sucursal(Empresa):
    def __init__(self, cod_sucursal, empresa, ubicacion):
        super().__init__(empresa)
        self.cod_sucursal = cod_sucursal
        self.ubicacion = ubicacion

    @classmethod
    def crear_sucursal(cls, diccionario):
        return cls(diccionario['cod_sucursal'], diccionario['empresa'], diccionario['ubicacion'])

if __name__ == '__main__':
    empresa1 = Empresa('kratos',['a','b'], ['pp','papa'] )
    print(str(empresa1))