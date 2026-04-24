import json

from clases.furgoneta import Furgoneta
from clases.coche import Coche
from clases.moto import Moto

from clases.casual import Casual

'''
PARA EMPRESAS:
'''


def alta_vehiculo():
    vehiculos = open('vehiculos.json', 'r', encoding='utf-8')
    lista_vehiculos = json.load(vehiculos)
    vehiculos.close()

    tip_veh = input('Ingrese el tipo de vehiculo (coche/moto/furgoneta): ')
    matricula = input('Introduce la matricula del vehiculo: ')
    marca = input('Introduce la marca del vehiculo: ')
    modelo = input('Introduce el modelo del vehiculo: ')
    anyo = input('Introduce el año del vehiculo: ')
    color = input('Introduce el color del vehiculo: ')
    kilometros = input('Introduce los kilometros del vehiculo: ')
    tipo_combustible = input('Introduce el tipo combustible del vehiculo: ')
    consumo = input('Introduce el consumo del vehiculo: ')
    caballos = input('Introduce los caballos del vehiculo: ')
    autonomia = input('Introduce la autonomia del vehiculo: ')
    precio_dia = input('Introduce el precio por día del vehiculo: ')
    estado = input('Introduce el estado del vehiculo: ')
    extras = input('Introduce los extras del vehiculo: ')

    if tip_veh == 'coche':
        tipo_coche = input('Introduce el tipo de coche: ')
        plazas = input('Introduce el número de plazas del coche: ')
        puertas = input('Introduce el número de puestas del coche: ')
        capacidad_maletero = input('Introduce la capacidad del maletero del coche (litros): ')
        carnet_requerido = input('Introduce el carnet requerido para conducir el coche: ')

        lista_vehiculos.append(matricula)

        vehiculos = open('vehiculos.json', 'w', encoding='utf-8')
        json.dump(lista_vehiculos, vehiculos, indent=4, ensure_ascii=False)
        vehiculos.close()

        return Coche(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia,
                     precio_dia, estado, extras,
                     tipo_coche, plazas, puertas, capacidad_maletero, carnet_requerido)

    elif tip_veh == 'moto':
        tipo_moto = input('Introduce el tipo de moto: ')
        cilindrada = input('Introduce la cilindrada de la moto: ')
        carnet_requerido = input('Introduce el carnet requerido para conducir la moto: ')

        return Moto(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia,
                    precio_dia, estado, extras,
                    tipo_moto, cilindrada, carnet_requerido)

    elif tip_veh == 'furgoneta':
        tipo_furgoneta = input('Introduce el tipo de furgoneta: ')
        capacidad_carga = input('Introduce la capacidad del carga de la furgoneta: ')
        carnet_requerido = input('Introduce el carnet requerido para conducir la furgoneta: ')

        return Furgoneta(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos,
                         autonomia, precio_dia, estado, extras,
                         tipo_furgoneta, capacidad_carga, carnet_requerido)

    else:
        print('ERROR: El tipo de vehiculo no es valido')
        return None


def mostrar_vehiculos(lista_vehiculos):

    print('--- VEHÍCULOS DISPONIBLES ---')
    for i in lista_vehiculos:
        if 'tipo_coche' in i:
            from clases.coche import Coche
            v = Coche.alta_coche(i)
        elif 'tipo_furgoneta' in i:
            from clases.furgoneta import Furgoneta
            v = Furgoneta.alta_furgoneta(i)
        elif 'tipo_moto' in i:
            from clases.moto import Moto
            v = Moto.alta_moto(i)
        else:
            continue

        print(v)


def buscar_vehiculo_por_matricula(matricula):
    with open('vehiculos.json', 'r', encoding='utf-8') as vehiculos:
        lista_vehiculos = json.load(vehiculos)

    for i in lista_vehiculos:
        # A veces la lista tiene strings de matriculas sueltas por un bug en alta_vehiculo, así que chay que comprobar si es diccionario
        if isinstance(i, dict) and i.get('matricula') == matricula:
            if 'tipo_coche' in i:
                from clases.coche import Coche
                return Coche.alta_coche(i)
            elif 'tipo_furgoneta' in i:
                from clases.furgoneta import Furgoneta
                return Furgoneta.alta_furgoneta(i)
            elif 'tipo_moto' in i:
                from clases.moto import Moto
                return Moto.alta_moto(i)
    return None


'''
PARA CLIENTES
'''


def alta_usuario(dni,lista_usuarios):
    nombre_completo = input('Introduce tu nombre completo: ')
    edad = input('Introduce tu edad: ')
    carnets = input('Introduce los carnets que tienes separados por comas (ej:B,A2,...): ')
    lista_carnets = carnets.split(',')

    lista_usuarios.append(Casual.alta_casual({'dni': dni, 'nombre_completo': nombre_completo, 'edad': edad, 'carnets': lista_carnets}))

    with open('clientes.json', 'w', encoding='utf-8') as clientes:
        json.dump(lista_usuarios, clientes, indent=4, ensure_ascii=False)

    return


def verificar_id(id_cliente):
    # Verifica si un DNI o NIE es válido

    id_cliente = id_cliente.strip()
    id_cliente = id_cliente.upper()
    id_cliente = id_cliente.replace('-', '')

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


def validar_cif(cif):
    # Valida un CIF de empresa

    cif.upper().strip()

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