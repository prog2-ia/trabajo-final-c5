class EdadMinimaException(Exception):
    #Excepcion personalizada para cuando un cliente no alcanza la edad minima
    def __init__(self, edad, mensaje="La edad es menor a la permitida (18)"):
        self.edad = edad
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    def __str__(self):
        return f"{self.mensaje} - Edad introducida: {self.edad}"

class DniInvalidoException(Exception):
    #Excepción para cuando el DNI/NIE introducido no es valido
    def __init__(self, dni, mensaje='El DNI/NIE introducido no es válido'):
        self.dni = dni
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    def __str__(self):
        return f'{self.mensaje}: {self.dni}'

class MatriculaInvalidaException(Exception):
    #Excepción para cuando la matricula no tiene un formato que sea válido
    def __init__(self, matricula, mensaje='El formato de la matrícula no es válido'):
        self.matricula = matricula
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    def __str__(self):
        return f'{self.mensaje}: {self.matricula}'