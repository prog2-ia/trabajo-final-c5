class Cliente:
    def __init__(self, dni, nombre_completo, edad, carnets):
        self.dni = dni
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.carnets = carnets

    @classmethod
    def Alta_Cliente(cls, dni, nombre_completo, edad, carnets):
        return cls(dni, nombre_completo, edad, *carnets) #no sé si es así para que acepte listas

    '''
    en la teoría aparece el operador de desempaquetado como:
    @classmethod
    def desde_secuencia(cls, secuencia):
        return cls(*secuencia)
        
    @classmethod
    def desde_secuencia_de_3(cls, secuencia):
        return cls(secuencia[0], secuencia[1], secuencia[2])
    '''
#cliente1 = Cliente('Y12345678Z', 'Carlos O', 18, ['AM','A1','A2','B'])
