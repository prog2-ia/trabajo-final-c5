from clases.cliente import Cliente
from clases.vehiculo import Vehiculo

#Calcula un coste estimado sin confirmar alquiler
class Presupuesto:
    def __init__(self, cliente: Cliente, vehiculo: Vehiculo, dias: int) -> None:
        self.vehiculo = vehiculo
        self.cliente = cliente
        self.dias = dias
        if self.poder_alquilar():
            self._precio = self.calcular_presupuesto()
            self._descuento = self.calcular_descuento()
            self._precio_final = self._precio - self._descuento
            self.mostrar_presupuesto()

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
        elif self.dias < 1 or self.dias > 100:
            print(f'Los días de alquiler deben ser entre 1 y 100')
            return False
        else:
            from funciones import vehiculo_disponible
            if not vehiculo_disponible(self.vehiculo.matricula):
                print(f'El vehículo {self.vehiculo.matricula} se encuentra alquilado en estas fechas.')
                return False
            return True

    def calcular_presupuesto(self) -> float: #calcula el presupuesto básico del alquiler
        tarifa_base = self.vehiculo.calcular_tarifa(self.dias)
        _precio = tarifa_base * (1.3 if self.cliente.edad < 25 else 1)  #Un 30% más si el cliente tiene menos de 25 años
        return _precio

    def __add__(self, other) -> float:
        #Sobrecarga del operador + para sumar el coste de dos presupuestos
        if isinstance(other, Presupuesto):
            return self._precio_final + other._precio_final
        return NotImplemented

    def __radd__(self, other) -> float:
        #Permite la suma inversa util para sum() con presupuestos
        if other == 0:
            return self._precio_final
        return self.__add__(other)

    def calcular_descuento(self) -> float: #calcula el descuento (simulado) sin cambiar los datos del cliente porque no se ha alquilado aún
        gastado_ahora = self.cliente.total_gastado + self._precio
        puntos = self.cliente.gastado_premium
        es_premium = self.cliente.premium

        if not es_premium and gastado_ahora >= 500:
            puntos = gastado_ahora - 500
            es_premium = True
        elif es_premium:
            puntos += self._precio

        descuento = 0
        if es_premium:
            descuento = puntos // 100 * 15

        return descuento

    def mostrar_presupuesto(self): #muestra el presupuesto con formato
        print('=======================================================')
        print('PRESUPUESTO ALQUILER')
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
        print(f'TOTAL ESTIMADO:  {self._precio_final} €')
        print('=======================================================')
        print()

