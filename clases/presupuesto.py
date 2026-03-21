from clases.cliente import Cliente
from clases.coche import Coche

class Presupuesto:
    def __init__(self, cliente, vehiculo, dias):
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
        elif self.dias < 1:
            print(f'Mínimo un día para poder alquilar')
            return False
        else:
            return True

    def calcular_presupuesto(self): #calcula el presupuesto básico del alquiler
        _precio = self.vehiculo.precio_dia * self.dias * (1.3 if self.cliente.edad < 25 else 1)  #Un 30% más si el cliente tiene menos de 25 años
        return _precio

    def calcular_descuento(self): #calcula el descuento (simulado) sin cambiar los datos del cliente porque no se ha alquilado aún
        gastado_ahora = self.cliente._total_gastado + self._precio
        puntos = self.cliente._gastado_premium
        es_premium = self.cliente._premium

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

#pruebas
if __name__ == '__main__':
    cliente1 = Cliente('Y12345678Z', 'Carlos O', 18, ['AM', 'A1', 'A2', 'B'])
    coche_prueba = Coche('2623CDJ', 'Ford', 'Focus', 2002, 'gris', 360000, 'diesel', 6, 100, 800, 25, 'Disponible',
    False, 'hatchback', 5, 4, 350, 'B')

    print('Presupuesto 1')
    Presupuesto(cliente1, coche_prueba, 10) #un presupuesto no suma gasto
    print()

    print('Presupuesto 2')
    Presupuesto(cliente1, coche_prueba, 20)
    print()
