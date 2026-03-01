from clases.cliente import Cliente
from clases.coche import Coche

class Presupuesto:
    def __init__(self, cliente, vehiculo, dias):
        self.vehiculo = vehiculo
        self.cliente = cliente
        self.dias = dias
        if self.poder_alquilar():
            self.precio_total = self.calcular_presupuesto()
            self.mostrar_presupuesto()

    def poder_alquilar(self):
        tipo_vehiculo = type(self.vehiculo).__name__

        if self.vehiculo.estado != 'Disponible':
            print(f'No está disponible para alquilar. Estado: {self.vehiculo.estado} ')

        elif self.cliente.edad < 18:
            print(f'Para poder alquilar hay que tener más de 18 años')

        elif self.vehiculo.carnet_requerido not in self.cliente.carnets:
            print(f'No se puede alquilar {tipo_vehiculo} sin el carnet {self.vehiculo.carnet_requerido}')

        elif self.dias < 1:
            print(f'Mínimo un día para poder alquilar')

        else:
            return True

    def calcular_presupuesto(self):
        precio_total = self.vehiculo.precio_dia * self.dias * (1.3 if self.cliente.edad < 25 else 1)  #Un 30% más si el cliente tiene menos de 25 años
        return precio_total

    def mostrar_presupuesto(self):
        print('-----------PRESUPUESTO-----------')
        print(f'Nombre completo: {self.cliente.nombre_completo}')
        print(f'DNI/NIE: {self.cliente.dni}')
        print(f'Datos del vehículo: {self.vehiculo.marca} {self.vehiculo.modelo} / {self.vehiculo.matricula}')
        print(f'--------------------------------\nEl precio total es de: {self.precio_total}')

#prueba
cliente1 = Cliente('Y12345678Z', 'Carlos O', 18, ['AM','A1','A2', 'B'])
coche1 = Coche('2623CDJ', 'Ford', 'Focus', 2002, 'gris', 360000, \
               'diesel', 6, 100, 800, 25, 'Disponible', \
               False,'hatchback', 5, 4, 350, 'B')
presupuesto1 = Presupuesto(cliente1, coche1, 3)
