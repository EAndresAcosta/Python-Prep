#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:
negativo = []
i = -15
while i < 0:
    negativo.append(i)
    i += 1
print(negativo)

# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:
i = 0
while i < len(negativo):
    if negativo[i] % 2 == 0:
        print('par numero', negativo[i])
    i += 1

# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:
lista = [i for i in negativo if i % 2 == 0]
print(lista)

# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:
for i in negativo[0:3]:
        print(i)

# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:
for i in enumerate(negativo):
    print(i)

# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:
lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[11]:
completar = []
for i in range(1, 21):
    if i not in lista:
        completar.append(i)
lista.extend(completar)
lista.sort()
print('lista completa', lista)

# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:
fibonacci = [0, 1]
i = 2
while i < 30:
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    i += 1
print('fibonacci =',fibonacci)

# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:
sum(fibonacci)

# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:
ultimos = 30
i = ultimos - 5
while i < ultimos:
    print(fibonacci[i] / fibonacci[i - 1])
    i += 1

# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
for i, c in enumerate(cadena):
    if c == 'n':
        print(i, c)

# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:
marcas = {'mercedez':10, 'bmw':9, 'audi':8, 'volkswagen':7 }
for i in marcas:
    print(i)

# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:
cadena = list(cadena)
cadena2 = iter(cadena)
longitud = len(cadena)
for i in range(0, longitud):
    print(next(cadena2))

# In[45]:





# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
union = zip(lista1, lista2)
print(list(union))

# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lis2 = []
for i in lis:
    if i % 7 == 0:
        lis2.append(i)
print(lis2)

# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
elementos = 0
for i in lis:
    if type(i) == list:
        elementos = elementos + len(i)
    else:
        elementos = elementos + 1
print(elementos)

# In[51]:





# In[57]:





# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:
for i, e in enumerate(lis):
    if type(e) != list:
        lis[i] = list(e)
print(lis)
