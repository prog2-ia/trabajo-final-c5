from clases.furgoneta import Furgoneta
from clases.coche import Coche
from clases.moto import Moto
from clases.vehiculo import Vehiculo


def alta_vehiculo():
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

        return Coche(matricula, marca, modelo, anyo, color, kilometros, tipo_combustible, consumo, caballos, autonomia, precio_dia, estado, extras,
                     tipo_coche, plazas, puertas, capacidad_maletero)

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