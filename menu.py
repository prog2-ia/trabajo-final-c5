from funciones import alta_vehiculo, mostrar_vehiculos, guardar_datos_json
from clases.cliente import Cliente


def menu_cliente(cliente_actual: Cliente, lista_vehiculos: list) -> None:
    respuesta = ''
    print(('-' * 25))

    while respuesta not in ['1', '2', '3', '4']:
        print('¿Que desea?'.center(25))
        print('1: Comparar presupuestos')
        print('2: Alquilar un vehiculo')
        print('3: Modificar mis datos / Añadir Carnet')
        print('4: Volver al menú principal')

        respuesta = input('Acción: ').strip()
        print()

        if respuesta == '1' or respuesta == '2':
            # Mostramos todos los vehiculos primero
            mostrar_vehiculos(lista_vehiculos)
            print()
            matricula = input('Introduce la matrícula del vehículo a elegir: ').strip().upper()
            from funciones import validar_matricula
            from excepciones import MatriculaInvalidaException
            try:
                validar_matricula(matricula)
            except MatriculaInvalidaException as e:
                print(f'ERROR: {e}')
                respuesta = ''
                continue

            try:
                dias = int(input('¿Cuántos días? (min 1): '))
            except ValueError:
                print('Error: Se debe introducir un número entero.')
                respuesta = ''
                continue

            from funciones import buscar_vehiculo_por_matricula
            vehiculo_obj = buscar_vehiculo_por_matricula(matricula)

            if vehiculo_obj:
                if respuesta == '1':
                    from clases.presupuesto import Presupuesto
                    Presupuesto(cliente_actual, vehiculo_obj, dias)
                elif respuesta == '2':
                    from clases.alquiler import Alquiler
                    Alquiler(cliente_actual, vehiculo_obj, dias)
            else:
                print('Vehículo no encontrado o matrícula incorrecta.')

            # Resetear respuesta para seguir en el menú
            respuesta = ''

        elif respuesta == '3':
            print('--- Tus datos actuales ---')
            print(f'Nombre: {cliente_actual.nombre_completo}')
            print(f'DNI: {cliente_actual.dni}')
            print(f'Edad: {cliente_actual.edad}')
            print('Dirección: ' + getattr(cliente_actual, 'direccion', 'No especificada'))
            print(f'Carnets: {cliente_actual.carnets}')
            print('--------------------------')
            print('Modificar datos del usuario:')
            print('1: Añadir Carnet')
            print('2: Cambiar edad')
            print('3: Cambiar dirección')
            print('4: Volver atrás')
            opc = input('Seleccione una opción: ').strip()
            if opc == '1':
                nuevos_carnets_input = input('Introduce el/los nuevos carnets separados por coma: ').strip().upper()
                validos = ['AM', 'A1', 'A2', 'A', 'B', 'B+E', 'B1', 'C1', 'C', 'C1+E', 'C+E', 'D1', 'D', 'D1+E', 'D+E',
                           'LCM', 'LVA']
                nuevos_carnets = [c.strip() for c in nuevos_carnets_input.split(',') if c.strip()]

                any_added = False
                for carnet in nuevos_carnets:
                    if carnet in validos and carnet not in cliente_actual.carnets:
                        cliente_actual += carnet
                        any_added = True
                        print(f'Carnet {carnet} añadido con éxito.')
                    elif carnet not in validos:
                        print(f'Carnet {carnet} no es válido en España.')
                    else:
                        print(f'Ya tienes el carnet {carnet}.')

                if any_added:
                    print(f'Carnets actuales: {cliente_actual.carnets}')
                    # Guardamos cambios en JSON
                    from funciones import guardar_datos_json, cargar_datos_json
                    todos_clientes = cargar_datos_json('clientes.json')
                    for c in todos_clientes:
                        if c['dni'] == cliente_actual.dni:
                            c['carnets'] = cliente_actual.carnets
                            break
                    guardar_datos_json('clientes.json', todos_clientes)
            elif opc == '2':
                # Cambiamos la edad si pone un numero positivo
                try:
                    nueva_edad = int(input('Introduce la nueva edad: '))
                    if nueva_edad < 18:
                        print('Error: Debes ser mayor de edad para usar la plataforma.')
                    else:
                        cliente_actual.edad = nueva_edad
                        print(f'Edad actualizada a {nueva_edad}.')
                        from funciones import guardar_datos_json, cargar_datos_json
                        todos_clientes = cargar_datos_json('clientes.json')
                        for c in todos_clientes:
                            if c['dni'] == cliente_actual.dni:
                                c['edad'] = cliente_actual.edad
                                break
                        guardar_datos_json('clientes.json', todos_clientes)
                except ValueError:
                    print('Error: Se debe introducir un número entero positivo.')
            elif opc == '3':
                nueva_dir = input('Introduce la nueva dirección: ').strip()
                cliente_actual.direccion = nueva_dir
                print('Dirección actualizada con éxito.')
                from funciones import guardar_datos_json, cargar_datos_json
                todos_clientes = cargar_datos_json('clientes.json')
                for c in todos_clientes:
                    if c['dni'] == cliente_actual.dni:
                        c['direccion'] = cliente_actual.direccion
                        break
                guardar_datos_json('clientes.json', todos_clientes)
            elif opc == '4':
                print('Volviendo al menú del cliente...')
            else:
                print('Opción no válida.')
            respuesta = ''

        elif respuesta == '4':
            print('Volviendo al inicio...')
        else:
            print('ERROR: Acción Invalida')
            respuesta = ''


def menu_empresa(lista_vehiculos: list) -> None:
    respuesta = ''
    print(('-' * 25))

    while respuesta != '1' and respuesta != '2' and respuesta != '3' and respuesta != '4' and respuesta != '5':
        print('¿Que desea?'.center(25))
        print('1: Dar de alta un vehiculo')
        print('2: Dar de baja un vehiculo')
        print('3: Modificar datos de un vehiculo')
        print('4: Mostrar datos de un vehiculo')
        print('5: Volver al menú principal')

        respuesta = input('Acción: ')
        print()

        if respuesta == '1':
            v = alta_vehiculo()
            if v:
                lista_vehiculos.append(v)
            respuesta = ''
        elif respuesta == '2':
            matricula = input('Introduce la matricula del vehiculo a dar de baja: ').strip().upper()
            vehiculo_encontrado = None
            for v in lista_vehiculos:
                if v.matricula == matricula:
                    vehiculo_encontrado = v
                    break

            if vehiculo_encontrado:
                lista_vehiculos.remove(vehiculo_encontrado)
                guardar_datos_json('vehiculos.json', lista_vehiculos)
                print(f'Vehiculo {matricula} dado de baja correctamente.')
            else:
                print('No se ha encontrado el vehiculo.')
            respuesta = ''

        elif respuesta == '3':
            matricula = input('Introduce la matricula del vehiculo a modificar: ').strip().upper()
            vehiculo_encontrado = None
            for v in lista_vehiculos:
                if v.matricula == matricula:
                    vehiculo_encontrado = v
                    break

            if vehiculo_encontrado:
                print('1. Modificar precio por dia')
                print('2. Modificar kilometros')
                print('3. Modificar estado')
                opcion_mod = input('Elige que quieres modificar: ')

                if opcion_mod == '1':
                    try:
                        nuevo_precio = float(input('Introduce el nuevo precio: '))
                        vehiculo_encontrado._Vehiculo__precio_dia = nuevo_precio  # Modificamos el atributo privado
                        guardar_datos_json('vehiculos.json', lista_vehiculos)
                        print('Precio modificado con exito.')
                    except ValueError:
                        print('Precio no valido.')
                elif opcion_mod == '2':
                    try:
                        nuevos_km = float(input('Introduce los nuevos kilometros: '))
                        vehiculo_encontrado.kilometros = nuevos_km
                        guardar_datos_json('vehiculos.json', lista_vehiculos)
                        print('Kilometros modificados con exito.')
                    except ValueError:
                        print('Kilometros no validos.')
                elif opcion_mod == '3':
                    nuevo_estado = input('Introduce el nuevo estado (ej. Disponible, Taller...): ')
                    vehiculo_encontrado.estado = nuevo_estado
                    guardar_datos_json('vehiculos.json', lista_vehiculos)
                    print('Estado modificado con exito.')
                else:
                    print('Opcion no valida.')
            else:
                print('No se ha encontrado el vehiculo.')
            respuesta = ''

        elif respuesta == '4':
            matricula = input('Introduce la matricula del vehiculo a mostrar: ').strip().upper()
            vehiculo_encontrado = None
            for v in lista_vehiculos:
                if v.matricula == matricula:
                    vehiculo_encontrado = v
                    break

            if vehiculo_encontrado:
                print('========================')
                print(f'Matricula: {vehiculo_encontrado.matricula}')
                print(f'Marca: {vehiculo_encontrado.marca}')
                print(f'Modelo: {vehiculo_encontrado.modelo}')
                print(f'Kilometros: {vehiculo_encontrado.kilometros}')
                print(f'Estado: {vehiculo_encontrado.estado}')
                print(f'Empresa: {vehiculo_encontrado.empresa}')
                print('========================')
            else:
                print('No se ha encontrado el vehiculo.')
            respuesta = ''
        elif respuesta == '5':
            print('Volviendo al inicio...')
        else:
            print('ERROR: Acción Invalida')