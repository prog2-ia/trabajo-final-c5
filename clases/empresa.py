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