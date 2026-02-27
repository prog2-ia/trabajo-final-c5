class Alquiler:
    def __init__(self, cliente, vehiculo, precio):
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.precio = precio

        if vehiculo.estado != 'Disponible':
            raise Exception('Vehículo no disponible')

        vehiculo.estado = 'Alquilado'
