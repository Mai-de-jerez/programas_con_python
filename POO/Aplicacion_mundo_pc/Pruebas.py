from Aplicacion_mundo_pc.clase_Computadora import Computadora
from Aplicacion_mundo_pc.clase_monitor import Monitor
from Aplicacion_mundo_pc.clase_Orden import Orden
from Aplicacion_mundo_pc.clase_Raton import Raton
from Aplicacion_mundo_pc.Clase_Teclado import Teclado

print('*** Mundo PC ***')

# Creamos una primer orden
teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP', 27)
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('Gamer', 'Bluetooth')
raton2 = Raton('Gamer', 'Bluetooth')
monitor2 = Monitor('Gamer', 34)
computadora2 = Computadora('Gamer', monitor2, teclado2, raton2)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)

teclado3 = Teclado('Dell', 'Bluetooth')
raton3 = Raton('Dell', 'Bluetooth')
monitor3 = Monitor('Dell', 27)
computadora3 = Computadora('Dell', monitor3, teclado3, raton3)
orden1.agregar_computadora(computadora3)
print(orden1)