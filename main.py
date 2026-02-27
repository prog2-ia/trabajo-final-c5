class Empresa:
    def __init__(self, cif, nombre, lista_sucursales):
        self.cif = cif
        self.nombre = nombre
        self.lista_sucursales = lista_sucursales

    @classmethod
    def crear_empresa(cls, diccionario):
        return cls(diccionario['cif'], diccionario['nombre'], diccionario['lista_sucursales'])

    def __str__(self):
        return f'{self.nombre} {self.lista_sucursales}'

    def __repr__(self):
        return (f'{type(self)}')

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