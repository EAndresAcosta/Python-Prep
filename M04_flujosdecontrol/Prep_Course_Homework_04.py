#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
num = [1, 2, 3, 4, 5]
for i in num:
    if i > 0:
        print(i, "Es mayor a cero")
    else:
        print(i, "Es menor a cero")


# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:
num = 2
var = "2"
if num == var:
    print("Son el mismo tipo de dato")
else:
    print("No son el mismo tipo de dato")


# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
enteros = [2, 3, 4, 7, 8, 9, 10, 17, 18, 20]
for i in enteros:
    if i % 2 == 0:
        print(i, "Es entero")
    else:
        print(i, "No es entero")


# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
for i in range(0, 6):
    print("Valor", str(i), "elevado a la 3ra potencia", str(i ** 3))


# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
ciclo = 3
for i in range(0, ciclo):
    ciclo == 3
    print(i)


# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:
n = 7
if type(n) == int and n > 0:
    factorial = 1
    while n > 0:
        factorial *= n
        n -= 1
    print("El factorial es", factorial)
else:
    print(None)


# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
num = 1
while num < 5:
    print("Ciclo while #" + str(num))
    for i in range(1, num+1):
        print("Ciclo for #" + str(i))
    num += 1


# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
n = 5
for i in range(1, n):
    print("Ciclo for " + str(i))
    var = n
    while (var > 0):
        print("Ciclo while " + str(n))
        n -= 1
        if var >= 0:
            break


# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:
for numero in range(2, 31):
    if numero <= 1:
        print("0 y 1 no son numeros primos")
        break
    es_primo = True
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(numero, " Es primo")


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:
for numero in range(2, 31):
    if numero <= 1:
        print("0 y 1 no son numeros primos")
        break
    es_primo = True
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(numero, " Es primo")


# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:
for numero in range(2, 31):
    if numero <= 1:
        print("0 y 1 no son numeros primos")
        break
    es_primo = True
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(numero, " Es primo")


# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:
n = 100
while n <= 300:
    n += 1
    if n % 12 != 0:
        continue
    print(n, " Es dividible por 12")


# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
num = 1
continuar = 1
for numero in range(2, num):
    if numero <= 1:
        print("0 y 1 no son numeros primos")
        break
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(numero, " Es primo")
        print("Desea encontrar el proximo numero primo")
        if input() != 1:
            print("Se finaliza el proceso")
            break
    else:
        es_primo = True
        num += 1


# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:
num = 99
while num < 300:
    if num % 3 == 0 and num % 6 == 0:
        print(num, "Es el primer numero divisible por 3 y multiplo de 6")
        break
    num += 1

