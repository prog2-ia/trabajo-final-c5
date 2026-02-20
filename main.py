class Empresa:
    def __init__(self, nombre, lista_vehiculos, lista_sucursales):
        self.nombre = nombre
        self.lista_vehiculos = lista_vehiculos
        self.lista_sucursales = lista_sucursales

    @classmethod
    def crear_empresa(cls, diccionario):
        return cls(diccionario['nombre'], diccionario['lista_vehiculos'], diccionario['sucursales'])

    def __str__(self):
        return f'{self.nombre} {self.lista_vehiculos} {self.lista_sucursales}'

    def __repr__(self):
        return (f'{type(self)}')

if __name__ == '__main__':
    empresa1 = Empresa('kratos',['a','b'], ['pp','papa'] )
    print(str(empresa1))