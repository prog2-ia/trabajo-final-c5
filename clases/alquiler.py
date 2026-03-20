from clases.cliente import Cliente
from clases.coche import Coche
from random import randint

class Alquiler:
    numero_referencia = 12345

    def __init__(self, cliente, vehiculo, dias):
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.dias = dias
        if self.poder_alquilar():
            self.crear_referencia()
            self._precio = self.calcular_presupuesto()
            self.sumar_gastado_cliente()

    def poder_alquilar(self):
        tipo_vehiculo = type(self.vehiculo).__name__

        if self.vehiculo.estado != 'Disponible':
            print(f'No está disponible para alquilar. Estado: {self.vehiculo.estado} ')
            return False
        elif self.cliente.edad < 18:
            print(f'Para poder alquilar hay que tener más de 18 años')
            return False
        elif self.vehiculo.carnet_requerido not in self.cliente.carnets:
            print(f'No se puede alquilar {tipo_vehiculo} sin el carnet {self.vehiculo.carnet_requerido}')
            return False
        elif self.dias < 1:
            print(f'El mínimo es un día para poder alquilar')
            return False
        else:
            return True

    def crear_referencia(self):
        type(self).numero_referencia += 1

    def calcular_presupuesto(self):
        _precio = self.vehiculo.precio_dia * self.dias * (1.3 if self.cliente.edad < 25 else 1)
        return _precio

    def sumar_gastado_cliente(self):
        self._total_gastado += self._precio
        if self.cliente.premium:
            self.cliente._gastado_premium += self._precio

    def preciofinal(self):
        _precio_final = self._precio - cliente._descuento


    def mostrar_alquiler(self):
        print('-----------ALQUILER-----------')
        print(f'Número de referencia del alquiler: {self.numero_referencia}')
        print(f'Nombre completo: {self.cliente.nombre_completo}')
        print(f'DNI/NIE: {self.cliente.dni}')
        print(f'Datos del vehículo: {self.vehiculo.marca} {self.vehiculo.modelo} / {self.vehiculo.matricula}')
        print(f'Precio total sin descuento: {self._precio_final}')
        print('-------------------------------')
        print(f'Precio total con descuento: {self._precio_final}')
        print()

#pruebas
cliente1 = Cliente('Y12345678Z', 'Carlos O', 18, ['AM','A1','A2', 'B'] )
cliente2 = Cliente('Y12345678Z', 'Carlos O', 18, ['AM','A1','A2', 'B'])
coche1 = Coche('2623CDJ', 'Ford', 'Focus', 2002, 'gris', 360000,
               'diesel', 6, 100, 800, 25, 'Disponible',
               False,'hatchback', 5, 4, 350, 'B')
print('cliente1:')
alquiler1 = Alquiler(cliente1, coche1, 1)
print(f'Cliente1 gastado: {cliente1._total_gastado}')
print(f'Cliente1 gastado_premium: {cliente1._gastado_premium}') #gastado_premium es el saldo a partir de 500 que le va quedando para ir acumulando y haciendo descuentos de 100 en 100
print(f'Cliente1 es premium?: {cliente1._premium}')
print(f'Total ahorrado: {cliente1._total_ahorrado}')
print()

print('cliente2:')
alquiler2 = Alquiler(cliente2, coche1, 2)
print(f'Cliente2 gastado: {cliente2._total_gastado}')
print(f'Cliente2 gastado_premium: {cliente2._gastado_premium}')
print(f'Cliente2 es premium?: {cliente2._premium}')
print(f'Total ahorrado: {cliente2._total_ahorrado}')
print()

print('cliente1:')
alquiler3 = Alquiler(cliente1, coche1, 10)
print(f'Cliente1 gastado: {cliente1._total_gastado}')
print(f'Cliente1 gastado_premium: {cliente1._gastado_premium}')
print(f'Cliente1 es premium?: {cliente1._premium}')
print(f'Total ahorrado: {cliente1._total_ahorrado}')
print()

print('cliente2:')
alquiler4 = Alquiler(cliente2, coche1, 10)
print(f'Cliente2 gastado: {cliente2._total_gastado}')
print(f'Cliente2 gastado_premium: {cliente2._gastado_premium}')
print(f'Cliente2 es premium?: {cliente2._premium}')
print(f'Total ahorrado: {cliente2._total_ahorrado}')
print()

print('cliente1:')
alquiler5 = Alquiler(cliente1, coche1, 10)
print(f'Cliente1 gastado: {cliente1._total_gastado}')
print(f'Cliente1 gastado_premium: {cliente1._gastado_premium}')
print(f'Cliente1 es premium?: {cliente1._premium}')
print(f'Total ahorrado: {cliente1._total_ahorrado}')
