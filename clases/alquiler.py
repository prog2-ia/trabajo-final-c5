from clases.cliente import Cliente
from clases.vehiculo import Vehiculo
from random import randint


# Gestiona un alquiler finalizado y crea su factura
class Alquiler:
    numero_referencia = 12345  # numero de referencia para identificar cada alquiler

    def __init__(self, cliente: Cliente, vehiculo: Vehiculo, dias: int) -> None:
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.dias = dias
        if self.poder_alquilar():
            self.crear_referencia()
            self.precio_base = self.calcular_presupuesto()
            self.sumar_gastado_cliente()
            self.precio_a_pagar = self.preciofinal()
            self.mostrar_alquiler()

            # Guardar en el historial
            from funciones import guardar_historial_json
            guardar_historial_json(self)

    def poder_alquilar(self):  # comprueba si se puede alquilar el vehiculo
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
        elif self.dias < 1 or self.dias > 100:
            print(f'Los días de alquiler deben ser entre 1 y 100')
            return False
        else:
            from funciones import vehiculo_disponible
            if not vehiculo_disponible(self.vehiculo.matricula):
                print(f'El vehículo {self.vehiculo.matricula} se encuentra alquilado en estas fechas.')
                return False
            return True

    def crear_referencia(self):  # crea la referencia del alquiler
        type(self).numero_referencia += 1

    def calcular_presupuesto(self) -> float:  # calcula el presupuesto básico del alquiler
        # Calculamos la tarifa dependiendo del vehiculo
        tarifa_base = self.vehiculo.calcular_tarifa(self.dias)

        # Los menores de 25 pagan mas
        if self.cliente.edad < 25:
            precio_base = tarifa_base * 1.3
        else:
            precio_base = tarifa_base

        return precio_base

    def sumar_gastado_cliente(
            self) -> float:  # suma el gasto al cliente y comprueba si es premium para calcular el descuento
        ya_era_premium = self.cliente.premium
        self.cliente.total_gastado += self.precio_base
        self.cliente.comprobar_premium()
        if ya_era_premium:  # si ya era premium, se le suma el gasto a su saldo premium para llevar la cuenta de cuanto lleva gastado
            self.cliente.gastado_premium += self.precio_base
        self.descuento_aplicado = self.cliente.descuento_premium()
        return self.descuento_aplicado

    def preciofinal(self):  # calcula el precio final del alquiler
        precio_a_pagar = self.precio_base - self.descuento_aplicado
        return precio_a_pagar

    def mostrar_alquiler(self):  # muestra la factura con todos los datos del alquiler
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