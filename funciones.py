import json

from clases.furgoneta import Furgoneta
from clases.coche import Coche
from clases.moto import Moto

from clases.casual import Casual

'''
PARA VEHICULOS:
'''

def alta_vehiculo():
    with open('vehiculos.json', 'r', encoding='utf-8') as vehiculos:
        lista_vehiculos = json.load(vehiculos)

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

        with open('vehiculos.json', 'w', encoding='utf-8') as vehiculos:
            json.dump(lista_vehiculos, vehiculos, indent=4, ensure_ascii=False)

        return Coche(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras,
                     tipo_coche, plazas, puertas, capacidad_maletero, carnet_requerido)

    elif tip_veh == 'moto':
        tipo_moto = input('Introduce el tipo de moto: ')
        cilindrada = input('Introduce la cilindrada de la moto: ')
        carnet_requerido = input('Introduce el carnet requerido para conducir la moto: ')

        return Moto(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras,
                    tipo_moto, cilindrada, carnet_requerido)

    elif tip_veh == 'furgoneta':
        tipo_furgoneta = input('Introduce el tipo de furgoneta: ')
        capacidad_carga = input('Introduce la capacidad del carga de la furgoneta: ')
        carnet_requerido = input('Introduce el carnet requerido para conducir la furgoneta: ')

        return Furgoneta(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras,
                         tipo_furgoneta, capacidad_carga, carnet_requerido)

    else:
        print('ERROR: El tipo de vehiculo no es valido')
        return None


def mostrar_vehiculos():
    with open('vehiculos.json', 'r', encoding='utf-8') as vehiculos:
        lista_vehiculos = json.load(vehiculos)

    print("--- FLOTA DE VEHÍCULOS ---")
    for i in lista_vehiculos:
        if "tipo_coche" in i:
            from clases.coche import Coche
            v = Coche.Alta_Coche(i)
        elif "tipo_furgoneta" in i:
            from clases.furgoneta import Furgoneta
            v = Furgoneta.Alta_Furgoneta(i)
        elif "tipo_moto" in i:
            from clases.moto import Moto
            v = Moto.Alta_Moto(i)
        else:
            continue

        print(v)


'''
PARA CLIENTES
'''

def alta_usuario(dni):
    nombre_completo = input('Introduce tu nombre completo: ')
    edad = input('Introduce tu edad: ')
    carnets = input('Introduce los carnets que tienes separados por comas: ')
    lista_carnets = carnets.split(', ')

    return Casual(dni, nombre_completo, edad, lista_carnets)



def verificar_id(id_cliente):
    id_cliente = id_cliente.strip()
    id_cliente = id_cliente.upper()
    id_cliente = id_cliente.replace("-", "")

    if len(id_cliente) != 9:
        return False

    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    mapeo_nie = {'X': '0', 'Y': '1', 'Z': '2'}

    cuerpo_num = id_cliente[:-1]
    letra_final = id_cliente[-1]

    if cuerpo_num[0] in mapeo_nie:
        cuerpo_num = mapeo_nie[cuerpo_num[0]] + cuerpo_num[1:]

    if not cuerpo_num.isdigit():
        return False

    return letras[int(cuerpo_num) % 23] == letra_final



def validar_cif(cif):
    cif.upper().strip()

    if len(cif) != 9:
        return False

    tipo = cif[0]
    numeros = cif[1:8]
    control = cif[8]

    if not tipo.isalpha() or not numeros.isdigit():
        return False

    letras_validas = "ABCDEFGHJKLMNPQRSUVW"
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

    letras_control = "JABCDEFGHI"

    if tipo in "ABEH":
        return str(digito_final) == control
    elif tipo in "KPQS":
        return letras_control[digito_final] == control
    else:
        return (str(digito_final) == control) or (letras_control[digito_final] == control)


'''
PARA EJEMPLO:
'''

def generar_y_guardar_flota_ejemplo():
    # 1. Definimos los datos crudos (Diccionarios)
    datos_ejemplo = [
        # 5 COCHES
        {"matricula": "1234ABC", "marca": "Seat", "modelo": "Ibiza", "anyo": "2020", "color": "Rojo",
         "kilometros": "15000", "tipo_combustible": "Gasolina", "consumo": "5.5", "caballos": "110", "autonomia": "800",
         "precio_dia": 40.0, "estado": "Disponible", "extras": "Aire", "tipo_coche": "Utilitario", "plazas": "5",
         "puertas": "5", "capacidad_maletero": "350", "carnet_requerido": "B"},
        {"matricula": "5678DEF", "marca": "Tesla", "modelo": "Model 3", "anyo": "2022", "color": "Blanco",
         "kilometros": "5000", "tipo_combustible": "Electrico", "consumo": "0", "caballos": "280", "autonomia": "500",
         "precio_dia": 90.0, "estado": "Disponible", "extras": "Autopilot", "tipo_coche": "Sedan", "plazas": "5",
         "puertas": "4", "capacidad_maletero": "425", "carnet_requerido": "B"},
        {"matricula": "9012GHI", "marca": "Toyota", "modelo": "Yaris", "anyo": "2021", "color": "Azul",
         "kilometros": "12000", "tipo_combustible": "Hibrido", "consumo": "3.9", "caballos": "116", "autonomia": "900",
         "precio_dia": 45.0, "estado": "Disponible", "extras": "Camara", "tipo_coche": "Compacto", "plazas": "5",
         "puertas": "5", "capacidad_maletero": "286", "carnet_requerido": "B"},
        {"matricula": "3456JKL", "marca": "BMW", "modelo": "Serie 1", "anyo": "2019", "color": "Negro",
         "kilometros": "45000", "tipo_combustible": "Diesel", "consumo": "4.8", "caballos": "150", "autonomia": "1000",
         "precio_dia": 65.0, "estado": "Disponible", "extras": "Cuero", "tipo_coche": "Premium", "plazas": "5",
         "puertas": "5", "capacidad_maletero": "380", "carnet_requerido": "B"},
        {"matricula": "7890MNP", "marca": "Audi", "modelo": "A3", "anyo": "2023", "color": "Gris", "kilometros": "1000",
         "tipo_combustible": "Gasolina", "consumo": "6.0", "caballos": "150", "autonomia": "850", "precio_dia": 75.0,
         "estado": "Disponible", "extras": "Techo", "tipo_coche": "Compacto", "plazas": "5", "puertas": "5",
         "capacidad_maletero": "380", "carnet_requerido": "B"},

        # 5 FURGONETAS
        {"matricula": "1111AAA", "marca": "Ford", "modelo": "Transit", "anyo": "2021", "color": "Blanco",
         "kilometros": "20000", "tipo_combustible": "Diesel", "consumo": "8.0", "caballos": "130", "autonomia": "900",
         "precio_dia": 80.0, "estado": "Disponible", "extras": "Puerta lateral", "tipo_furgoneta": "Carga",
         "capacidad_carga": "1000kg", "carnet_requerido": "B"},
        {"matricula": "2222BBB", "marca": "Mercedes", "modelo": "Vito", "anyo": "2022", "color": "Plata",
         "kilometros": "15000", "tipo_combustible": "Diesel", "consumo": "7.5", "caballos": "160", "autonomia": "950",
         "precio_dia": 100.0, "estado": "Disponible", "extras": "GPS", "tipo_furgoneta": "Mixta",
         "capacidad_carga": "800kg", "carnet_requerido": "B"},
        {"matricula": "3333CCC", "marca": "Renault", "modelo": "Kangoo", "anyo": "2020", "color": "Amarillo",
         "kilometros": "35000", "tipo_combustible": "Gasolina", "consumo": "6.5", "caballos": "95", "autonomia": "700",
         "precio_dia": 55.0, "estado": "Disponible", "extras": "Baca", "tipo_furgoneta": "Pequeña",
         "capacidad_carga": "500kg", "carnet_requerido": "B"},
        {"matricula": "4444DDD", "marca": "VW", "modelo": "Transporter", "anyo": "2018", "color": "Azul",
         "kilometros": "80000", "tipo_combustible": "Diesel", "consumo": "8.5", "caballos": "150", "autonomia": "850",
         "precio_dia": 85.0, "estado": "Disponible", "extras": "Gancho", "tipo_furgoneta": "Carga",
         "capacidad_carga": "1200kg", "carnet_requerido": "B"},
        {"matricula": "5555EEE", "marca": "Peugeot", "modelo": "Partner", "anyo": "2023", "color": "Blanco",
         "kilometros": "2000", "tipo_combustible": "Electrico", "consumo": "0", "caballos": "136", "autonomia": "280",
         "precio_dia": 70.0, "estado": "Disponible", "extras": "Sensores", "tipo_furgoneta": "Reparto",
         "capacidad_carga": "600kg", "carnet_requerido": "B"},

        # 5 MOTOS
        {"matricula": "0001KKK", "marca": "Honda", "modelo": "SH 125", "anyo": "2022", "color": "Negro",
         "kilometros": "2000", "tipo_combustible": "Gasolina", "consumo": "2.2", "caballos": "13", "autonomia": "300",
         "precio_dia": 25.0, "estado": "Disponible", "extras": "Baul", "tipo_moto": "Scooter", "cilindrada": "125",
         "carnet_requerido": "A1"},
        {"matricula": "0002LLL", "marca": "Yamaha", "modelo": "MT-07", "anyo": "2021", "color": "Cyan",
         "kilometros": "8000", "tipo_combustible": "Gasolina", "consumo": "4.2", "caballos": "74", "autonomia": "350",
         "precio_dia": 50.0, "estado": "Disponible", "extras": "Protector", "tipo_moto": "Naked", "cilindrada": "689",
         "carnet_requerido": "A2"},
        {"matricula": "0003MMM", "marca": "BMW", "modelo": "R 1250", "anyo": "2023", "color": "Blanco",
         "kilometros": "500", "tipo_combustible": "Gasolina", "consumo": "4.7", "caballos": "136", "autonomia": "450",
         "precio_dia": 120.0, "estado": "Disponible", "extras": "Puños", "tipo_moto": "Trail", "cilindrada": "1250",
         "carnet_requerido": "A"},
        {"matricula": "0004NNN", "marca": "Kawa", "modelo": "Z900", "anyo": "2022", "color": "Verde",
         "kilometros": "4000", "tipo_combustible": "Gasolina", "consumo": "5.2", "caballos": "125", "autonomia": "320",
         "precio_dia": 65.0, "estado": "Disponible", "extras": "Escape", "tipo_moto": "Sport", "cilindrada": "948",
         "carnet_requerido": "A"},
        {"matricula": "0005OOO", "marca": "Vespa", "modelo": "Primavera", "anyo": "2020", "color": "Rojo",
         "kilometros": "10000", "tipo_combustible": "Gasolina", "consumo": "2.5", "caballos": "11", "autonomia": "250",
         "precio_dia": 35.0, "estado": "Disponible", "extras": "Casco", "tipo_moto": "Clasica", "cilindrada": "125",
         "carnet_requerido": "A1"}
    ]

    objetos_flota = []

    # 2. Creamos los objetos (T03 y T04)
    # Identificamos el tipo por las llaves únicas de cada diccionario
    for d in datos_ejemplo:
        if "tipo_coche" in d:
            objetos_flota.append(Coche.Alta_Coche(d))
        elif "tipo_furgoneta" in d:
            objetos_flota.append(Furgoneta.Alta_Furgoneta(d))
        elif "tipo_moto" in d:
            objetos_flota.append(Moto.Alta_Moto(d))

    # 3. Preparamos para JSON (Convertimos objetos a diccionarios usando .__dict__)
    # El modelo de datos de Python (T07) nos permite acceder a los atributos así
    lista_para_json = [obj.__dict__ for obj in objetos_flota]

    # 4. Guardamos en el archivo
    with open('vehiculos.json', 'w', encoding='utf-8') as f:
        json.dump(lista_para_json, f, indent=4, ensure_ascii=False)

    print(f"Éxito: Se han creado {len(objetos_flota)} objetos y guardado en vehiculos.json")
