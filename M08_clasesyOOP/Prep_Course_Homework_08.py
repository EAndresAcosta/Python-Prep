#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

# In[1]:
class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada

# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>

# In[5]:
class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.doblar = 0

    def Acelerar(self, veloci):
        self.velocidad += veloci

    def Frenar(self, veloci):
        self.velocidad -= veloci

    def Doblar(self, grados):
        self.doblar += grados

# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# In[6]:
v1 = Vehiculo('Azul', 'Auto', 2.0)
v2 = Vehiculo('Rojo', 'Moto', 999)
v3 = Vehiculo('Negro', 'Camioneta', 3.0)

v1.Acelerar(50)
v2.Acelerar(120)
v3.Acelerar(80)

v1.Frenar(-30)
v2.Frenar(-60)

v3.Doblar(90)
v1.Doblar(-90)

# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# In[12]:
class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.doblar = 0

    def Acelerar(self, veloci):
        self.velocidad += veloci

    def Frenar(self, veloci):
        self.velocidad -= veloci

    def Doblar(self, grados):
        self.doblar += grados
    
    def Estado(self):
        print('Velocidad:', self.velocidad, 'Direccion:', self.doblar)

    def Detalle(self):
        print('Color:', self.color, 'Tipo:', self.tipo, 'Cilindrada:', self.cilindrada)


# In[13]:
v1 = Vehiculo('Azul', 'Auto', 2.0)
v1.Estado()
v1.Detalle()

# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 7<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

# In[33]:
class Funciones:
    def __init__(self) -> None:
        pass

    def es_primo(self, numero):
        num_primo = True
        if numero <= 1:
            return False
        for divisor in range(2, int(numero ** 1/2) + 1):
            if numero % divisor == 0:
                num_primo = False
                break
        if num_primo:
            return num_primo

    def repeated(self, lista):
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
    
    def convertir_grados(self, valor, origen, destino):
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
    
    def factorial(self, numero):
        if type(numero) != int:
            return("Debe ingresar un numero entero")
        if numero < 0:
            return("El numero debe ser positivo")
        if numero <= 1:
            return 1
        numero = numero * self.factorial(numero - 1)
        return numero

herramienta = Funciones()

# 6) Probar las funciones incorporadas en la clase del punto 5

# In[28]:
herramienta.es_primo(7)

herramienta.repeated([1,2,3,1,2,1,3,2,1,3])

herramienta.convertir_grados(2, 'farenheit', 'celcius')

herramienta.factorial(7)

# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# In[55]:
class Funciones:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def es_primo(self):
        for i in self.lista:
            if self.__es_primo(i):
                print(i, 'Es numero primo')
            else:
                print(i, 'No es numero primo')

    def convertir_grados(self, origen, destino):
        for i in self.lista:
            print(i, 'Grados', origen, 'son', self.__convertir_grados(i, origen, destino), 'Grados', destino)

    def factorial(self):
        for i in self.lista:
            print('El factorial de', i, 'es', self.__factorial(i))

    def __es_primo(self, numero):
        num_primo = True
        if numero <= 1:
            return False
        for divisor in range(2, int(numero ** 1/2) + 1):
            if numero % divisor == 0:
                num_primo = False
                break
        if num_primo:
            return num_primo

    def repeated(self, menor):
        lista_unicos = []
        lista_repeticiones = []
        if len(self.lista) == 0:
            return None
        if (menor):
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)
        for elemento in self.lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo
    
    def __convertir_grados(self, valor, origen, destino):
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
    
    def __factorial(self, numero):
        if (type(numero) != int):
            return("Debe ingresar un numero entero")
        if (numero < 0):
            return("El numero debe ser positivo")
        if (numero == 1):
            return 1
        if (numero > 1):
            numero = numero * self.__factorial(numero - 1)
        return numero

f = Funciones([2,3,5,4,2,3,2,5,3,2,3,2,4,2])

f.es_primo()
f.convertir_grados('celcius', 'farenheit')
moda, repe = f.repeated(False)
print('El valor modal es', moda, 'y se repite', repe)
f.factorial()

# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

# In[1]:
from herramientas import *

f2 = Herramientas([5,6,8,9,11,15,17,19])

f2.verifica_primo()