class EdadMinimaException(Exception):
    #Excepcion personalizada para cuando un cliente no alcanza la edad minima
    def __init__(self, edad, mensaje="La edad es menor a la permitida (18)"):
        self.edad = edad
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    def __str__(self):
        return f"{self.mensaje} - Edad introducida: {self.edad}"