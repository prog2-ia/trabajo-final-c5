import json
import os

from clases.furgoneta import Furgoneta
from clases.coche import Coche
from clases.moto import Moto
from clases.casual import Casual
from clases.vehiculo import Vehiculo

'''
PARA EMPRESAS:
'''


def cargar_datos_json(nombre_archivo: str) -> list:
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []


def guardar_datos_json(nombre_archivo: str, datos: list) -> None:
    # Convertimos los objetos a diccionarios para poder guardarlos en JSON
    datos_dict = [obj.__dict__ if hasattr(obj, '__dict__') else obj for obj in datos]
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        json.dump(datos_dict, f, indent=4, ensure_ascii=False)


def alta_vehiculo() -> Vehiculo | None:
    lista_vehiculos_dict = cargar_datos_json('vehiculos.json')

    lista_vehiculos = []
    for v in lista_vehiculos_dict:
        if 'tipo_coche' in v:
            lista_vehiculos.append(Coche.alta_coche(v))
        elif 'tipo_furgoneta' in v:
            lista_vehiculos.append(Furgoneta.alta_furgoneta(v))
        elif 'tipo_moto' in v:
            lista_vehiculos.append(Moto.alta_moto(v))

    tip_veh = input('Ingrese el tipo de vehiculo (coche/moto/furgoneta): ').strip().lower()
    matricula = input('Introduce la matricula del vehiculo: ')
    marca = input('Introduce la marca del vehiculo: ')
    modelo = input('Introduce el modelo del vehiculo: ')
    try:
        anyo = int(input('Introduce el año del vehiculo: '))
        kilometros = float(input('Introduce los kilometros del vehiculo: '))
        consumo = float(input('Introduce el consumo del vehiculo: '))
        caballos = int(input('Introduce los caballos del vehiculo: '))
        autonomia = float(input('Introduce la autonomia del vehiculo: '))
        precio_dia = float(input('Introduce el precio por día del vehiculo: '))
    except ValueError:
        print('ERROR: Entrada de número inválida.')
        return None

    color = input('Introduce el color del vehiculo: ')
    tipo_combustible = input('Introduce el tipo combustible del vehiculo: ')
    estado = input('Introduce el estado del vehiculo: ')
    extras = input('Introduce los extras del vehiculo: ')

    v = None
    if tip_veh == 'coche':
        tipo_coche = input('Introduce el tipo de coche: ')
        try:
            plazas = int(input('Introduce el número de plazas del coche: '))
            puertas = int(input('Introduce el número de puertas del coche: '))
            capacidad_maletero = float(input('Introduce la capacidad del maletero del coche (litros): '))
        except ValueError:
            print('ERROR: Entrada de número inválida.')
            return None
        carnet_requerido = input('Introduce el carnet requerido para conducir el coche: ')

        v = Coche(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia,
                  precio_dia, estado, extras,
                  tipo_coche, plazas, puertas, capacidad_maletero, carnet_requerido)

    elif tip_veh == 'moto':
        tipo_moto = input('Introduce el tipo de moto: ')
        try:
            cilindrada = int(input('Introduce la cilindrada de la moto: '))
        except ValueError:
            print('ERROR: Entrada de número inválida.')
            return None
        carnet_requerido = input('Introduce el carnet requerido para conducir la moto: ')

        v = Moto(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia,
                 precio_dia, estado, extras,
                 tipo_moto, cilindrada, carnet_requerido)

    elif tip_veh == 'furgoneta':
        tipo_furgoneta = input('Introduce el tipo de furgoneta: ')
        capacidad_carga = input('Introduce la capacidad del carga de la furgoneta: ')
        carnet_requerido = input('Introduce el carnet requerido para conducir la furgoneta: ')

        v = Furgoneta(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos,
                      autonomia, precio_dia, estado, extras,
                      tipo_furgoneta, capacidad_carga, carnet_requerido)
    else:
        print('ERROR: El tipo de vehiculo no es valido')
        return None

    if v is not None:
        lista_vehiculos.append(v)
        guardar_datos_json('vehiculos.json', lista_vehiculos)
        return v


def exportar_vehiculos_txt(lista_vehiculos: list) -> None:
    try:
        with open('listado_vehiculos.txt', 'w', encoding='utf-8') as f:
            f.write('--- LISTADO DE VEHÍCULOS ---\n')
            for v in lista_vehiculos:
                f.write(f'{v}\n')
        print("Listado exportado correctamente a listado_vehiculos.txt")
    except Exception as e:
        print(f"Error al exportar: {e}")


def mostrar_vehiculos(lista_vehiculos: list) -> None:
    print('--- VEHÍCULOS DISPONIBLES ---')
    for v in lista_vehiculos:
        print(v)


def buscar_vehiculo_por_matricula(matricula: str) -> Vehiculo | None:
    lista_vehiculos_dict = cargar_datos_json('vehiculos.json')
    lista_vehiculos = []
    for v in lista_vehiculos_dict:
        if 'tipo_coche' in v:
            lista_vehiculos.append(Coche.alta_coche(v))
        elif 'tipo_furgoneta' in v:
            lista_vehiculos.append(Furgoneta.alta_furgoneta(v))
        elif 'tipo_moto' in v:
            lista_vehiculos.append(Moto.alta_moto(v))

    for v in lista_vehiculos:
        if hasattr(v, 'matricula') and v.matricula == matricula:
            return v
    return None


'''
PARA CLIENTES
'''


def alta_usuario(dni: str, lista_usuarios: list) -> Casual:
    nombre_completo = input('Introduce tu nombre completo: ')
    try:
        edad = int(input('Introduce tu edad: '))
    except ValueError:
        print("Edad no válida, se asigna 18 por defecto.")
        edad = 18
    carnets = input('Introduce los carnets que tienes separados por comas (ej:B,A2,...): ')
    lista_carnets = carnets.split(',')

    nuevo_cliente = Casual(dni, nombre_completo, edad, lista_carnets)
    lista_usuarios.append(nuevo_cliente)
    guardar_datos_json('clientes.json', lista_usuarios)

    return nuevo_cliente


def verificar_id(id_cliente: str) -> bool:
    # Verifica si un DNI o NIE es válido
    id_cliente = id_cliente.strip().upper().replace('-', '')

    if len(id_cliente) != 9:
        return False

    letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
    mapeo_nie = {'X': '0', 'Y': '1', 'Z': '2'}

    cuerpo_num = id_cliente[:-1]
    letra_final = id_cliente[-1]

    if cuerpo_num[0] in mapeo_nie:
        cuerpo_num = mapeo_nie[cuerpo_num[0]] + cuerpo_num[1:]

    if not cuerpo_num.isdigit():
        return False

    return letras[int(cuerpo_num) % 23] == letra_final


def validar_cif(cif: str) -> bool:
    # Valida un CIF de empresa
    cif = cif.upper().strip()

    if len(cif) != 9:
        return False

    tipo = cif[0]
    numeros = cif[1:8]
    control = cif[8]

    if not tipo.isalpha() or not numeros.isdigit():
        return False

    letras_validas = 'ABCDEFGHJKLMNPQRSUVW'
    if tipo not in letras_validas:
        return False

    pares = 0
    impares = 0

    for i in range(len(numeros)):
        num = int(numeros[i])
        if (i + 1) % 2 == 0:
            pares += num
        else:
            temp = num * 2
            impares += (temp // 10) + (temp % 10)

    suma = pares + impares
    digito_final = 10 - (suma % 10)
    if digito_final == 10:
        digito_final = 0

    letras_control = 'JABCDEFGHI'

    if tipo in 'ABEH':
        return str(digito_final) == control
    elif tipo in 'KPQS':
        return letras_control[digito_final] == control
    else:
        return (str(digito_final) == control) or (letras_control[digito_final] == control)