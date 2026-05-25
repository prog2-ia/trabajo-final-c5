Link del repositorio de github: https://github.com/prog2-ia/trabajo-final-c5 

Trabajo hecho por: Enrique Martín Masegosa y Carlos Onica

# Sistema de Alquiler de Vehículos

Este es nuestro trabajo de programación II. Es un programa para gestionar una empresa que alquila coches, motos y furgonetas.

##  Qué hace el programa

Básicamente tiene dos modos:
1. Cliente: Puedes entrar metiendo tu DNI, ver los vehículos que hay y simular presupuestos o alquilar directamente.
2. Empresa: Puedes añadir vehículos.


## Instalación/Uso

No hace falta instalar nada, solo tener Python instalado. Todo lo demás (como el módulo json) ya viene con Python.

Para arrancar el programa:
 1 - Descargar y descomprimir el .zip del proyecto
 2 - Abrir la terminal y ubicarse con el comando cd en la carpeta del proyecto
 3 - Ejecutar el fichero main con ./main
 4 - En caso de Error: Permiso denegado. Usar comando 'chmod -x main'
 5 - Volver a intentar ejecutar el fichero main

## Ejemplos para probar

Si lo probáis, podéis darle a iniciar como cliente y poner el vuestro DNI o NIE para crear un usuario que se guardará en el archivo json de clientes, o uno cualquiera como por ejemplo '55019506X' para acceder a uno ya creado. Luego le dais a alquilar o sacar presupuesto. Os pedirá la matrícula de un coche a elegir y los días. Veréis cómo el programa genera e imprime automáticamente el presupuesto o la factura final. Hay un sistema de descuentos para clientes premium si llevas más de 500€ gastados, cosa que el menú calcula automáticamente simulando a un usuario real. A la hora de alquilar, el programa tiene cuenta que no esté alquilado, tomando la fecha actual del dispositivo, por lo que podréis probar a hacer un alquiler y luego ver en el historial de la cuenta de ese cliente cómo se ha generado y guardado, además de que luego ese vehículo deja de aparecer en la lista de vehículos disponibles.

Lo mismo si iniciáis como empresa: os pedirá un CIF válido (podéis usar por ejemplo el 'B12345674').

### Copia de Seguridad Automática
También hemos implementado un sistema de copias de seguridad automáticas. Al salir del programa de forma escribiendo 'salir' en el menú principal, el sistema utiliza las librerías `os` y `shutil` para rastrear todos los archivos con datos `.json` y hacer una copia de respaldo en una única carpeta llamada `copia_seguridad` que se actualiza. Podéis probar a entrar, hacer alguna modificación (como alquilar un coche o cambiar la edad de vuestro cliente) y luego salir del programa para comprobar cómo se actualiza esta carpeta.


## Esquema del Proyecto (Archivos y Funciones)

Aquí dejamos un resumen rápido de cómo está estructurado el código y para qué sirve cada cosa:

### Archivos Principales
* `main.py`
  * `if __name__ == '__main__':` Carga todos los datos de los archivos `.json` al empezar.
  * `inicio`: Es la función principal que arranca el programa y te pregunta si eres cliente o empresa.
* `menu.py`
  * `menu_cliente`: Aquí está toda la lógica del menú interactivo cuando entras como cliente (alquilar, presupuestos, ver datos...).
  * `menu_empresa`: El menú para cuando entras como empresa.
* `funciones.py` (Aquí están casi todas las funciones sueltas que usamos en el proyecto)
  * `cargar_datos_json`: Lee la información guardada.
  * `guardar_datos_json`: Guarda la información cuando hacemos cambios.
  * `alta_vehiculo`: Te va pidiendo por pantalla todos los datos para crear un coche/moto/furgoneta nuevo.
  * `vehiculo_disponible`: Comprueba en el historial si un vehículo ya está alquilado en esas fechas o no.
  * `mostrar_vehiculos`: Imprime por pantalla la lista de vehículos libres.
  * `buscar_vehiculo_por_matricula`: Busca un vehículo en la lista usando su matrícula.
  * `alta_usuario`: Pide los datos por pantalla para registrar a un cliente nuevo.
  * `verificar_id`: Comprueba que la letra y los números del DNI/NIE sean correctos.
  * `validar_cif`: Comprueba que el formato del CIF de la empresa sea válido.
  * `validar_matricula`: Comprueba que las matrículas cumplan el formato (4 números y 3 consonantes).
  * `guardar_historial_json`: Guarda el registro (factura) cada vez que alguien alquila.
* `excepciones.py`: Archivo donde guardamos errores (Edad mínima, DNI falso o Matrícula falsa).

### Archivos de Datos (.json)
* `clientes.json`: Guarda los datos de la gente registrada.
* `empresas.json`: Guarda los datos de las empresas dueñas de los coches.
* `vehiculos.json`: La lista con todos los vehículos de la app.
* `historial.json`: Los tickets y recibos de los alquileres pasados.

### Clases (Orientación a Objetos)
Todas las clases las tenemos metidas en la carpeta `clases/` separadas en archivos para que quede más limpio:
* `Cliente`: La clase base (o padre) para los usuarios.
  * `Casual`: Subclase de cliente normal.
  * `Premium`: Subclase de cliente VIP con descuentos especiales.
* `Empresa`: Para crear las empresas de alquiler.
* `Vehiculo`: Clase padre (Abstracta) para todo lo que tenga ruedas.
  * `Coche`, `Moto`, `Furgoneta`: Subclases de Vehiculo con sus cosas específicas (capacidad del maletero, carga, etc).
* `Alquiler`: Clase para calcular y generar el recibo final cuando confirmas que alquilas algo.
* `Presupuesto`: Clase parecida a Alquiler pero que solo te muestra cuánto te va a costar, sin confirmar la reserva.
