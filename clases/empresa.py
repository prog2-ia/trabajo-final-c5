#Empresa que gestiona sucursales
class Empresa:
    def __init__(self, cif: str, nombre: str, lista_sucursales: list) -> None:
        self.cif = cif
        self.nombre = nombre
        self.lista_sucursales = lista_sucursales

    #Permite indexar la empresa para obtener sus sucursales
    def __getitem__(self, index):
        return self.lista_sucursales[index]

    #Instancia la clase a partir de un diccionario JSON
    @classmethod
    def crear_empresa(cls, diccionario):
        return cls(diccionario['cif'], diccionario['nombre'], diccionario['lista_sucursales'])

    def __str__(self):
        return f'{self.nombre} {self.lista_sucursales}'

    def __repr__(self):
        return (f'{type(self)}')