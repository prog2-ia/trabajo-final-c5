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
    datos = open('clientes.json', 'r', encoding='utf-8')
    lista_usuarios = json.load(datos)
    datos.close()
    print()
    print('Bienvenido al sistema')
    print(('-------------------------------------------'))

    while respuesta != 'cliente' and respuesta != 'empresa':
        print('¿Como quiere acceder?')
        respuesta = input('cliente/empresa: ')

        if respuesta == 'cliente':
            usuario = input('Introduce tu DNI/NIE: ')

            from funciones import verificar_id
            if not verificar_id(usuario):
                print('ERROR: DNI/NIE no válido.')
                respuesta = ''
                continue

            if usuario not in lista_usuarios:
                cliente_actual = alta_usuario(usuario)
                lista_usuarios.append(usuario)
                datos = open('clientes.json', 'w', encoding='utf-8')
                json.dump(lista_usuarios, datos, indent=4, ensure_ascii=False)
                datos.close()

            else:
                from clases.cliente import Cliente
                # Creamos un cliente temporal porque el json original solo guardaba strings
                cliente_actual = Cliente(usuario, 'Cliente Habitual', 30, ['B'])

            menu_cliente(cliente_actual)

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

    lista_usuarios = []
    datos_usuarios=open('clientes.json', 'r', encoding='utf-8')
    for usuario in datos_usuarios:
        lista_usuarios.append(Casual.alta_casual(usuario))

    lista_vehiculos = []
    datos_vehiculos = open('vehiculos.json', 'r', encoding='utf-8')
    for vehiculo in datos_vehiculos:
        if 'tipo_coche' in vehiculo:
            lista_vehiculos.append(Coche.alta_coche(vehiculo))
        elif 'tipo_furgoneta' in vehiculo:
            lista_vehiculos.append(Furgoneta.alta_furgoneta(vehiculo))
        elif 'tipo_moto' in vehiculo:
            lista_vehiculos.append(Moto.alta_moto(vehiculo))

    lista_empresas = []
    datos_empresas=open('empresas.json', 'r', encoding='utf-8')
    for empresa in lista_empresas:
        lista_empresas.append(Empresa.crear_empresa(empresa))

    inicio()