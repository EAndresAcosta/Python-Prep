#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:
def es_primo(numero):
    num_primo = True
    if numero <= 1:
            return False
    for divisor in range(2, int(numero ** 1/2) + 1):
            if numero % divisor == 0:
                num_primo = False
                break
    if num_primo:
        return num_primo

nro = es_primo(29)
print(nro)

# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:
def nros_primos(lista):
    lista_nros_primos = []
    for elemento in lista:
        if es_primo(int(elemento)):
            lista_nros_primos.append(int(elemento))
    return lista_nros_primos    

lista_completa = list(range(1,20))
lista_primos = nros_primos(lista_completa)
print(lista_primos)

# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:
def repeated(lista):
    mas_repetido = []
    numero_repeticiones = []
    for numero in lista:
        if numero in mas_repetido:
            i = mas_repetido.index(numero)
            numero_repeticiones[i] += 1
        else:
            mas_repetido.append(numero)
            numero_repeticiones.append(1)
    repet = mas_repetido[0]
    cantidad = numero_repeticiones[0]
    for i, numero in enumerate(mas_repetido):
        if numero_repeticiones[i] > cantidad:
            repet = mas_repetido[i]
            cantidad = numero_repeticiones[i]
    return repet, cantidad

lis = [1,2,5,8,6,9,4,9,7,9,3,6,9]
repeated(lis)

# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:
def convertir_grados(valor, origen, destino):
    if origen == "celcius":
        if destino == "celcius":
            valor_destino = valor
        elif destino == "farenheit":
            valor_destino = (valor * (9/5)) + 32
        elif destino == "kelvin":
            valor_destino = valor + 273.15
        else:
            print("Debe pasar un destino correcto")
    
    elif origen == "farenheit":
        if destino == "celcius":
            valor_destino = (valor - 32) * 5 / 9
        elif destino == "farenheit":
            valor_destino = valor
        elif destino == "kelvin":
            valor_destino = ((valor - 32) * 5 / 9) + 273.15
        else:
            print("Debe pasar un destino correcto")
    
    elif origen == "kelvin":
        if destino == "celcius":
            valor_destino = valor - 273.15
        elif destino == "farenheit":
            valor_destino = ((valor - 273.15) * 9 / 5) + 32
        elif destino == "kelvin":
            valor_destino = valor
        else:
            print("Debe pasar un destino correcto")
    
    else:
        print("Debe pasar un destino correcto")

    return valor_destino

convertir_grados(1, 'celcius', 'kelvin')

# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:
metricas = ['celcius', 'kelvin', 'farenheit']
for i in range(len(metricas)):
    for j in range(len(metricas)):
        print(f'1 grado de {metricas[i]} a {metricas[j]} es igual a {convertir_grados(1, metricas[i], metricas[j])}')

# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:
def factorial(numero):
    if type(numero) != int:
        return("Debe ingresar un numero entero")
    if numero < 0:
        return("El numero debe ser positivo")
    if numero <= 1:
        return 1
    numero = numero * factorial(numero - 1)
    return numero

print(f'{factorial(5)}, {factorial(-4)}, {factorial(1)}, {factorial(2.3)}')
