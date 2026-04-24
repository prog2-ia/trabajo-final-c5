from clases.casual import Casual
from clases.empresa import Empresa
from clases.coche import Coche
from clases.furgoneta import Furgoneta
from clases.moto import Moto

from funciones import *
from menu import *
import json


def inicio():
    respuesta = ''
    print()
    print('Bienvenido al sistema')
    print(('-------------------------------------------'))

    while respuesta != 'cliente' and respuesta != 'empresa':
        print('¿Como quiere acceder?')
        respuesta = input('cliente/empresa: ')

        if respuesta == 'cliente':
            usuario=''
            while not verificar_id(usuario):
                usuario = input('Introduce tu DNI/NIE: ')

                if not verificar_id(usuario):
                    print('ERROR: DNI/NIE no válido.')

                else:
                    if usuario not in lista_usuarios:
                        alta_usuario(usuario,lista_usuarios)

                    else:

                    menu_cliente(usuario,lista_vehiculos)

        elif respuesta == 'empresa':
            cif = input('Introduce el CIF de la empresa (ej: B12345674): ')

            from funciones import validar_cif
            if not validar_cif(cif):
                print('ERROR: CIF de empresa no válido.')
                respuesta = ''
                continue

            menu_empresa()

        else:
            print()
            print('ERROR: Acceso Invalido')


if __name__ == '__main__':

    datos_usuarios=open('clientes.json', 'r', encoding='utf-8')
    lista_usuarios=json.load(datos_usuarios)
    for usuario in datos_usuarios:
        lista_usuarios.append(Casual.alta_casual(usuario))

    datos_vehiculos = open('vehiculos.json', 'r', encoding='utf-8')
    lista_vehiculos=json.load(datos_vehiculos)
    for vehiculo in datos_vehiculos:
        if 'tipo_coche' in vehiculo:
            lista_vehiculos.append(Coche.alta_coche(vehiculo))
        elif 'tipo_furgoneta' in vehiculo:
            lista_vehiculos.append(Furgoneta.alta_furgoneta(vehiculo))
        elif 'tipo_moto' in vehiculo:
            lista_vehiculos.append(Moto.alta_moto(vehiculo))
    print(lista_vehiculos)

    datos_empresas=open('empresas.json', 'r', encoding='utf-8')
    lista_empresas=json.load(datos_empresas)
    for empresa in lista_empresas:
        lista_empresas.append(Empresa.crear_empresa(empresa))

    inicio()