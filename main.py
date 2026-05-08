import os
from funciones import *
from menu import *
from clases.cliente import Cliente
from clases.casual import Casual
from clases.coche import Coche
from clases.furgoneta import Furgoneta
from clases.moto import Moto
from clases.empresa import Empresa


def inicio(lista_usuarios: list, lista_vehiculos: list) -> None:
    respuesta = ''
    print()
    print('Bienvenido al sistema')
    print(('-------------------------------------------'))

    while respuesta != 'cliente' and respuesta != 'empresa':
        print('¿Como quiere acceder?')
        respuesta = input('cliente/empresa: ').strip().lower()

        if respuesta == 'cliente':
            usuario = input('Introduce tu DNI/NIE: ').strip()

            if not verificar_id(usuario):
                print('ERROR: DNI/NIE no válido.')
                respuesta = ''
                continue

            cliente_actual = next((c for c in lista_usuarios if c.dni == usuario), None)

            if not cliente_actual:
                print('Usuario no encontrado. Procediendo a dar de alta.')
                cliente_actual = alta_usuario(usuario, lista_usuarios)

            menu_cliente(cliente_actual, lista_vehiculos)

        elif respuesta == 'empresa':
            cif = input('Introduce el CIF de la empresa (ej: B12345674): ').strip()

            if not validar_cif(cif):
                print('ERROR: CIF de empresa no válido.')
                respuesta = ''
                continue

            menu_empresa(lista_vehiculos)

        else:
            print()
            print('ERROR: Acceso Invalido')


if __name__ == '__main__':
    # Cargamos datos JSON y los convertimos en objetos
    lista_usuarios_dict = cargar_datos_json('clientes.json')
    lista_usuarios = []
    for u in lista_usuarios_dict:
        # Recuperamos propiedades internas si existen
        cliente = Casual.alta_casual(u)
        if '_premium' in u: cliente._premium = u['_premium']
        if '_total_gastado' in u: cliente._total_gastado = u['_total_gastado']
        if '_gastado_premium' in u: cliente._gastado_premium = u['_gastado_premium']
        lista_usuarios.append(cliente)

    lista_vehiculos_dict = cargar_datos_json('vehiculos.json')
    lista_vehiculos = []
    for v in lista_vehiculos_dict:
        if 'tipo_coche' in v:
            lista_vehiculos.append(Coche.alta_coche(v))
        elif 'tipo_furgoneta' in v:
            lista_vehiculos.append(Furgoneta.alta_furgoneta(v))
        elif 'tipo_moto' in v:
            lista_vehiculos.append(Moto.alta_moto(v))

    lista_empresas_dict = cargar_datos_json('empresas.json')
    lista_empresas = [Empresa.crear_empresa(e) for e in lista_empresas_dict]

    inicio(lista_usuarios, lista_vehiculos)