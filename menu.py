from funciones import alta_vehiculo, mostrar_vehiculos, exportar_vehiculos_txt
from clases.cliente import Cliente

def menu_cliente(cliente_actual: Cliente, lista_vehiculos: list) -> None:
    respuesta = ''
    print(('-' * 25))

    while respuesta != '1' and respuesta != '2' and respuesta != '3':
        print('¿Que desea?'.center(25))
        print('1: Comparar presupuestos')
        print('2: Alquilar un vehiculo')
        print('3: Salir')

        respuesta = input('Acción: ')
        print()

        if respuesta == '1' or respuesta == '2':
            mostrar_vehiculos(lista_vehiculos)
            print()
            matricula = input('Introduce la matrícula del vehículo a elegir: ')
            try:
                dias = int(input('¿Cuántos días? (min 1): '))
            except ValueError:
                print('Error: Se debe introducir un número entero.')
                respuesta = ''
                continue

            from funciones import buscar_vehiculo_por_matricula
            vehiculo_obj = buscar_vehiculo_por_matricula(matricula)

            if vehiculo_obj:
                if respuesta == '1':
                    from clases.presupuesto import Presupuesto
                    Presupuesto(cliente_actual, vehiculo_obj, dias)
                elif respuesta == '2':
                    from clases.alquiler import Alquiler
                    Alquiler(cliente_actual, vehiculo_obj, dias)
            else:
                print('Vehículo no encontrado o matrícula incorrecta.')

            # Resetear respuesta para seguir en el menú
            respuesta = ''

        elif respuesta == '3':
            print('Saliendo...')
        else:
            print('ERROR: Acción Invalida')


def menu_empresa(lista_vehiculos: list) -> None:
    respuesta = ''
    print(('-' * 25))

    while respuesta != '1' and respuesta != '2' and respuesta != '3' and respuesta != '4' and respuesta != '5' and respuesta != '6':
        print('¿Que desea?'.center(25))
        print('1: Dar de alta un vehiculo')
        print('2: Dar de baja un vehiculo (No implementado)')
        print('3: Modificar datos de un vehiculo (No impl.)')
        print('4: Mostrar datos de un vehiculo (No impl.)')
        print('5: Exportar listado de vehículos a TXT')
        print('6: Salir')

        respuesta = input('Acción: ')
        print()

        if respuesta == '1':
            v = alta_vehiculo()
            if v:
                lista_vehiculos.append(v)
            respuesta = ''
        elif respuesta in ['2', '3', '4']:
            respuesta = ''
        elif respuesta == '5':
            exportar_vehiculos_txt(lista_vehiculos)
            respuesta = ''
        elif respuesta == '6':
            print('Saliendo...')
        else:
            print('ERROR: Acción Invalida')