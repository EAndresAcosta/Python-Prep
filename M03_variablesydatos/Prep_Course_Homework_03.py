#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
num = 8
print(num)



# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
constante = 8.5
print(type(constante))




# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
print(type(num))




# 4) Crear una variable que contenga tu nombre

# In[2]:
mi_nombre = 'Andres'



# 5) Crear una variable que contenga un número complejo

# In[3]:
num1 = 3 +3j




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print(type(num1))




# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:
pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
var1 = 'True'
var2 = True




# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print('el tipo de valor de var1 es ', type(var1), 'el tipo de valor de var2 es', type(var2) )



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
suma = 2 + 2.5
print(suma)



# 11) Realizar una operación de suma de números complejos

# In[2]:
suma = 2j + 2j
print(suma)




# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
adicion = suma + 3j
print(adicion)




# 13) Realizar una operación de multiplicación

# In[5]:
multi = 2 * 5
print(multi)




# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
print(2 ** 8)



# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
division = 27 / 4
print(division)




# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
division = 27 // 4
print(division)




# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
print(27 % 4)




# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
print(6 * 4 + 3)




# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
numero1 = 8
numero2 = 2
print(numero1 + numero2)




# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
print('2' == 2)




# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
number = '2'
number1 = int(number)
print(number1 == 2)




# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
a = float('3,8') #por que el valor inicial es un string y no se ha convertido a tipo float




# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
resta = 3
resta -= 1
print(resta)




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
print(1 << 2) # desplazamiento de bits del 1 dos posiciones hacia la izquierda y rellenando de ceros a la derecha conformando el numero binario 0100 = 4




# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
print(2 + '2') # por que no se puede sumar un entero con un string





# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
print('Andres ' * 2)


