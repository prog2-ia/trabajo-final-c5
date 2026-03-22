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

Para arrancar el programa, solo tienes que ejecutar desde la terminal:

python main.py

## Ejemplos para probar

Si lo probáis, podéis darle a iniciar como cliente y poner el vuestro para crear un usuario que se guardará en el archivo json de clientes, o uno cualquiera como por ejemplo 'Y0866893Z' para acceder a uno ya creado. Luego le dais a alquilar o sacar presupuesto. Os pedirá la matrícula de un coche a elegir y los días. Veréis cómo el programa genera e imprime automáticamente el presupuesto o la factura final. Hay un sistema de descuentos para clientes premium si llevas más de 500€ gastados, cosa que el menú calcula automáticamente simulando a un usuario real.

Lo mismo si iniciáis como empresa: os pedirá un CIF válido (podéis usar el de ejemplo que sale en pantalla: 'B12345674'). De momento fuciona solo dar de alta un vehículo.


