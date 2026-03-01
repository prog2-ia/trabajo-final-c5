from clases.cliente import Cliente
from clases.coche import Coche
from random import randint

class Alquiler:
    numero_referencia = 12345

    def __init__(self, cliente, vehiculo, dias, descuento = 0):
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.dias = dias
        self.descuento = descuento
        if self.poder_alquilar():
            self.crear_referencia()
            self.precio_total = self.calcular_presupuesto()
            self.sumar_gastado_cliente()
            self.comprobar_premium()
            self.descuento_premium()
            self.mostrar_alquiler()

    #alguna función es reciclada de 'presupuesto.py'
    #habría que ponerlo en 'funciones.py' para usarlas en varias clases pero todavía no por si acaso
    def poder_alquilar(self):
        tipo_vehiculo = type(self.vehiculo).__name__

        if self.vehiculo.estado != 'Disponible':
            print(f'No está disponible para alquilar. Estado: {self.vehiculo.estado} ')

        elif self.cliente.edad < 18:
            print(f'Para poder alquilar hay que tener más de 18 años')

        elif self.vehiculo.carnet_requerido not in self.cliente.carnets:
            print(f'No se puede alquilar {tipo_vehiculo} sin el carnet {self.vehiculo.carnet_requerido}')

        elif self.dias < 1:
            print(f'El mínimo es un día para poder alquilar')

        else:
            return True

    def crear_referencia(self):  #para que vaya cambiando la referencia según se vayan alquilando
        type(self).numero_referencia += 1

    def calcular_presupuesto(self):
        precio_total = self.vehiculo.precio_dia * self.dias * (1.3 if self.cliente.edad < 25 else 1)
        return precio_total

    def sumar_gastado_cliente(self): #registrar lo que va gastando el cliente
        self.cliente.total_gastado += self.precio_total
        self.cliente.gastado_premium += self.precio_total

    def comprobar_premium(self):
        if not self.cliente.premium and self.cliente.total_gastado >= 500:
            self.cliente.gastado_premium = self.cliente.total_gastado - 500
            self.cliente.premium = True

    def descuento_premium(self):
        if self.cliente.premium:
            self.descuento  += self.cliente.gastado_premium // 100 * 15
            self.cliente.gastado_premium -= (self.cliente.gastado_premium // 100 ) * 100
            self.cliente.total_ahorrado += self.descuento

    def mostrar_alquiler(self):
        print('-----------ALQUILER-----------')
        print(f'Número de referencia del alquiler: {self.numero_referencia}')
        print(f'Nombre completo: {self.cliente.nombre_completo}')
        print(f'DNI/NIE: {self.cliente.dni}')
        print(f'Datos del vehículo: {self.vehiculo.marca} {self.vehiculo.modelo} / {self.vehiculo.matricula}')
        print(f'Precio total sin descuento: {self.precio_total}')
        print('-------------------------------')
        print(f'Precio total con descuento: {self.precio_total - self.descuento}')
        print()

#pruebas
cliente1 = Cliente('Y12345678Z', 'Carlos O', 18, ['AM','A1','A2', 'B'])
cliente2 = Cliente('Y12345678Z', 'Carlos O', 18, ['AM','A1','A2', 'B'])
coche1 = Coche('2623CDJ', 'Ford', 'Focus', 2002, 'gris', 360000, \
               'diesel', 6, 100, 800, 25, 'Disponible', \
               False,'hatchback', 5, 4, 350, 'B')
print('cliente1:')
alquiler1 = Alquiler(cliente1, coche1, 1)
print(f'Cliente1 gastado: {cliente1.total_gastado}')
print(f'Cliente1 gastado_premium: {cliente1.gastado_premium}') #gastado_premium es el saldo a partir de 500 que le va quedando para ir acumulando y haciendo descuentos de 100 en 100
print(f'Cliente1 es premium?: {cliente1.premium}')
print(f'Total ahorrado: {cliente1.total_ahorrado}')
print()

print('cliente2:')
alquiler2 = Alquiler(cliente2, coche1, 2)
print(f'Cliente2 gastado: {cliente2.total_gastado}')
print(f'Cliente2 gastado_premium: {cliente2.gastado_premium}')
print(f'Cliente2 es premium?: {cliente2.premium}')
print(f'Total ahorrado: {cliente2.total_ahorrado}')
print()

print('cliente1:')
alquiler3 = Alquiler(cliente1, coche1, 20)
print(f'Cliente1 gastado: {cliente1.total_gastado}')
print(f'Cliente1 gastado_premium: {cliente1.gastado_premium}')
print(f'Cliente1 es premium?: {cliente1.premium}')
print(f'Total ahorrado: {cliente1.total_ahorrado}')
print()

print('cliente2:')
alquiler4 = Alquiler(cliente2, coche1, 5)
print(f'Cliente2 gastado: {cliente2.total_gastado}')
print(f'Cliente2 gastado_premium: {cliente2.gastado_premium}')
print(f'Cliente2 es premium?: {cliente2.premium}')
print(f'Total ahorrado: {cliente2.total_ahorrado}')
print()

print('cliente1:')
alquiler5 = Alquiler(cliente1, coche1, 15)
print(f'Cliente1 gastado: {cliente1.total_gastado}')
print(f'Cliente1 gastado_premium: {cliente1.gastado_premium}')
print(f'Cliente1 es premium?: {cliente1.premium}')
print(f'Total ahorrado: {cliente1.total_ahorrado}')
