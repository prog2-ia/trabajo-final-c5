from funciones import alta_vehiculo, mostrar_vehiculos
import json


def menu_cliente(cliente_actual):
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
            mostrar_vehiculos()
            print()
            matricula = input('Introduce la matrícula del vehículo a elegir: ')
            dias = int(input('¿Cuántos días? (min 1): '))

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


def menu_empresa():
    respuesta = ''

    print(('-' * 25))

    while respuesta != '1' and respuesta != '2' and respuesta != '3' and respuesta != '4' and respuesta != '5':

        print('¿Que desea?'.center(25))
        print('1: Dar de alta un vehiculo')
        print('2: Dar de baja un vehiculo')
        print('3: Modificar datos de un vehiculo')
        print('4: Mostrar datos de un vehiculo')
        print('5: Salir')

        respuesta = input('Acción: ')
        print()

        if respuesta == '1':
            alta_vehiculo()

        elif respuesta == '2':
            menu_empresa()

        elif respuesta == '3':
            menu_empresa()

        elif respuesta == '4':
            menu_empresa()

        elif respuesta == '5':
            print('Saliendo...')

        else:
            print('ERROR: Acción Invalida')