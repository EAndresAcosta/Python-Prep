# 1) Crear un script con el nombre "clase09_ej1.py" que reciba 3 parametros a elección, verificando que sean exactamente esa cantidad, y muestre como salida los parámetros recibidos

import sys

if len(sys.argv) == 4:
    print('Primer parametro:', sys.argv[1])
    print('Segundo parametro:', sys.argv[2])
    print('Tercer parametro:', sys.argv[3])
else:
    print('ERROR ingreso mas de 3 parametros')