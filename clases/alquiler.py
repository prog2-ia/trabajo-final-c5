from clases.cliente import Cliente
from clases.coche import Coche
from random import randint

class Alquiler:
    numero_referencia = 12345 #numero de referencia para identificar cada alquiler

    def __init__(self, cliente, vehiculo, dias):
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.dias = dias
        if self.poder_alquilar():
            self.crear_referencia()
            self._precio = self.calcular_presupuesto()
            self.sumar_gastado_cliente()
            self._precio_final = self.preciofinal()
            self.mostrar_alquiler()

    def poder_alquilar(self): #comprueba si se puede alquilar el vehiculo
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

    def crear_referencia(self): #crea la referencia del alquiler
        type(self).numero_referencia += 1

    def calcular_presupuesto(self): #calcula el presupuesto básico del alquiler
        _precio = self.vehiculo.precio_dia * self.dias * (1.3 if self.cliente.edad < 25 else 1)
        return _precio

    def sumar_gastado_cliente(self): #suma el gasto al cliente y comprueba si es premium para calcular el descuento
        ya_era_premium = self.cliente._premium
        self.cliente._total_gastado += self._precio
        self.cliente.comprobar_premium()
        if ya_era_premium: #si ya era premium, se le suma el gasto a su saldo premium para llevar la cuenta de cuanto lleva gastado
            self.cliente._gastado_premium += self._precio
        self._descuento = self.cliente.descuento_premium()
        return self._descuento

    def preciofinal(self): #calcula el precio final del alquiler
        _precio_final = self._precio - self._descuento
        return _precio_final

    def mostrar_alquiler(self): #muestra la factura con todos los datos del alquiler
        print('=======================================================')
        print(f'FACTURA ALQUILER {self.numero_referencia}')
        print('-------------------------------------------------------')
        print('DATOS DEL CLIENTE:')
        print(f'Nombre y apellidos:   {self.cliente.nombre_completo}')
        print(f'DNI:   {self.cliente.dni}')
        print('-------------------------------------------------------')
        print('DATOS DEL VEHÍCULO:')
        print(f'Marca:   {self.vehiculo.marca}')
        print(f'Modelo:   {self.vehiculo.modelo}')
        print(f'Matrícula:   {self.vehiculo.matricula}')
        print(f'Días:   {self.dias}')
        print('-------------------------------------------------------')
        print('RESUMEN')
        print(f'Subtotal:   {self._precio} €')
        print(f'Descuento:     -{self._descuento} €')
        print('-------------------------------------------------------')
        print(f'TOTAL:  {self._precio_final} €')
        print('=======================================================')
        print()

#pruebas
if __name__ == '__main__':
    cliente1 = Cliente('Y12345678Z', 'Carlos O', 18, ['AM', 'A1', 'A2', 'B'])
    coche_prueba = Coche('2623CDJ', 'Ford', 'Focus', 2002, 'gris', 360000, 'diesel', 6, 100, 800, 25, 'Disponible',
    False, 'hatchback', 5, 4, 350, 'B')

    print('ALQUILER 1')
    Alquiler(cliente1, coche_prueba, 3)
    print(f'Total gastado: {cliente1._total_gastado} €  ')
    print(f'Saldo premium: {cliente1._gastado_premium} €')
    print(f'Total ahorrado: {cliente1._total_ahorrado} €\n')
    print()

    print('ALQUILER 2')
    Alquiler(cliente1, coche_prueba, 10)
    print(f'Total gastado: {cliente1._total_gastado} €')
    print(f'Saldo premium: {cliente1._gastado_premium} €')
    print(f'Total ahorrado: {cliente1._total_ahorrado} €\n')
    print()

    print('ALQUILER 3')
    Alquiler(cliente1, coche_prueba, 10)
    print(f'Total gastado: {cliente1._total_gastado} €')
    print(f'Saldo premium: {cliente1._gastado_premium} €')
    print(f'Total ahorrado: {cliente1._total_ahorrado} €')
    print()

    print('ALQUILER 4')
    Alquiler(cliente1, coche_prueba, 5)
    print(f'Total gastado: {cliente1._total_gastado} €')
    print(f'Saldo premium: {cliente1._gastado_premium} €')
    print(f'Total ahorrado: {cliente1._total_ahorrado} €')
    print()