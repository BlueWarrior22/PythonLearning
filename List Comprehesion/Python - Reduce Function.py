#Python - Reduce Function

"""
📌 reduce() se usa para reducir una secuencia de valores a un único resultado, aplicando una función acumulativa.
📌 Se encuentra en el módulo functools, por lo que primero debemos importarlo:
"""

from functools import reduce

#Syntaxis

# reduce(función_acumuladora, iterable, valor_inicial_opcional)

#🔹 Ejemplo 1: Sumar todos los números de una lista:

numeros = [1, 2, 3, 4, 5]

suma_total = reduce(lambda acumulador, numero: acumulador + numero, numeros)

print(numeros)

print(suma_total)


numbers_str = ['1', '2', '3', '4', '5']

def suma_dos_numeros(x1, x2):
    return int(x1)+int(x2)

suma_numeros_str = reduce(suma_dos_numeros, numbers_str)

print(suma_numeros_str)

#🔹 Ejemplo 3: Encontrar el número más grande en una lista:

numeros_1 = [12, 45, 7, 89, 34, 23]

mayor = reduce(lambda a, b: a if a > b else b, numeros_1)

print(mayor)

#🔹 Ejemplo 4: Concatenar una lista de strings:

palabras = ["Hola", "mundo", "esto", "es", "Python"]

cadena_str = reduce(lambda acumulador, palabra: acumulador + " " + palabra, palabras)

print(cadena_str)

#🔹 Ejemplo 5: Calcular el total a pagar con descuentos:

precios = [100, 200, 50, 400, 150]

total_a_pagar = reduce(lambda subtotal, precio: subtotal + (precio*0.9), precios,0)

print(total_a_pagar)