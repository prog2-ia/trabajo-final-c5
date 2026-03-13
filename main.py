import menu
from funciones import *
from menu import *

import json



def inicio():
    respuesta = ''

    with open('datos.json', 'r', encoding='utf-8') as datos:
        lista_usuarios = json.load(datos)

    print()
    print('Bienvenido al sistema'.center(25))
    print(('-'*25))

    while respuesta != 'cliente' and respuesta != 'empresa':

        print('¿Como quiere acceder?'.center(25))
        respuesta = input('cliente/empresa: ')

        if respuesta == 'cliente':
            usuario = input('Introduce tu DNI/NIE: ')
            if usuario not in lista_usuarios:
                alta_usuario(usuario)
                lista_usuarios.append(usuario)

                with open('datos.json', 'w', encoding='utf-8') as datos:
                    json.dump(lista_usuarios, datos, indent=4, ensure_ascii=False)

            menu_cliente()

        elif respuesta == 'empresa':
            menu_empresa()

        else:
            print()
            print('ERROR: Acceso Invalido')


if __name__ == '__main__':
    inicio()