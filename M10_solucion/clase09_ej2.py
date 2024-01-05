# 2) Crear un script con el nombre "clase09_ej2.py2" que reciba como un valor de temperatura en grados centígrados, un valor de humedad y por último si llovio (Con True o False). Y que cada vez que sea invocado, cargue en el archivo provisto "clase09_ej2.csv" una marca de tiempo y esa información.

import sys
if len(sys.argv) == 2:
    import datetime
    import os
    x = datetime.datetime.now()
    print(f'Ahora el tiempo es: {x}')
    x = datetime.datetime.timestamp(x)

    lluvia = sys.argv[1]
    temperatura = input('Ingrese un valor en celcius')
    humedad = input('Ingrese un porcentaje de humedad')
    tiempo = str(x) + ',' + temperatura + ',' + humedad + ',' + lluvia

    dato_tiempo = open('clase09_ej2.csv', 'a')
    dato_tiempo.write(tiempo + '\n')
    dato_tiempo.close()

else:
    print("ERROR: Introduce el argumento)")
    print('Ejemplo: clase09_ej1.py <True o False>')

