from clases.cliente import Cliente
from clases.coche import Coche

class Presupuesto:
    def __init__(self, vehiculo, cliente, dias):
        self.vehiculo = vehiculo
        self.cliente = cliente
        self.dias = dias
        self.poder_alquilar()
        self.precio_total = self.calcular_presupuesto()
        self.mostrar_presupuesto()


    def poder_alquilar(self):
        tipo_vehiculo = type(self.vehiculo).__name__

        if self.vehiculo.estado != 'Disponible':
            raise Exception(f'No está disponible para alquilar. Estado: {self.vehiculo.estado} ')

        if self.cliente.edad < 18:
            raise Exception(f'Para poder alquilar hay que tener más de 18 años')

        if self.vehiculo.carnet_requerido not in self.cliente.carnets:
            raise Exception(f'No se puede alquilar {tipo_vehiculo} sin el carnet {self.vehiculo.carnet_requerido}')

        if self.dias < 1:
            raise Exception(f'Mínimo un día para poder alquilar')

    def calcular_presupuesto(self):
        precio_total = self.vehiculo.precio_dia * self.dias * (1.3 if self.cliente.edad < 25 else 1)
        return precio_total

    def mostrar_presupuesto(self):
        print(f' El precio total (sin descuento) es de: {self.precio_total}')

#prueba
cliente1 = Cliente('Y12345678Z', 'Carlos O', 18, ['AM','A1','A2','B'])
coche1 = Coche('2623CDJ', 'Ford', 'Focus', 2002, 'gris', 360000, 'diesel', 6, 100, 800, 25, 'Disponible', False,'hatchback', 5, 4, 350, 'B')
presupuesto1 = Presupuesto(coche1, cliente1,5)
