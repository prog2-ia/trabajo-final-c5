class Alquiler:
    def __init__(self, cliente, vehiculo, precio):
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.precio = precio

        if vehiculo.estado != 'disponible':
            raise Exception('Vehiculo no disponible')

        vehiculo.estado = 'alquilado'