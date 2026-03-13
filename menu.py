from funciones import alta_vehiculo
import json

def menu_cliente():
    respuesta = ''

    print(('-'*25))

    while respuesta != '1' and respuesta != '2' and respuesta != '3':

        print('¿Que desea?'.center(25))
        print('1: Comparar presupuestos')
        print('2: Alquilar un vehiculo')
        print('3: Salir')

        respuesta = input('Acción: ')
        print()

        if respuesta == '1':
            pass

        elif respuesta == '2':
            pass

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
            pass

        elif respuesta == '3':
            pass

        elif respuesta == '4':
            pass

        elif respuesta == '5':
            print('Saliendo...')

        else:
            print('ERROR: Acción Invalida')