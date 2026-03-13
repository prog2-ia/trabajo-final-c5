import funciones as fn
import menu

import json

from clases.casual import Casual

def inicio():
    respuesta = ''
    lista_usuarios = []

    print()
    print('Bienvenido al sistema'.center(25))
    print(('-'*25))

    while respuesta != 'cliente' and respuesta != 'empresa':

        print('¿Como quiere acceder?'.center(25))
        respuesta = input('cliente/empresa: ')

        if respuesta == 'cliente':
            usuario = input('Introduce tu DNI/NIE: ')
            if usuario in lista_usuarios:
                menu.manu_cliente()
            else funciones.alta_usuario()

        elif respuesta == 'empresa':
            menu.menu_empresa()

        else:
            print()
            print('ERROR: Acceso Invalido')


if __name__ == '__main__':
    inicio()