#The built-in high-order in Python are functions that can take other functions as arguments or return functions.
#These allow for writing cleaner and more efficient code.

numeros = list(range(1, 101))

numeros_x_2 = list(map(lambda x: x*2, numeros))

print(numeros_x_2)

def cuadrado_fn(n):
    return n ** 2

cuadrado = list(map(cuadrado_fn, numeros))

print(cuadrado)

#3️⃣ map() con Múltiples Iterables

numeros_pares = list(range(0, 101, 2))
numeros_tres = list(range(0, 101, 3))

sumando_dos_iterables = list(map(lambda x, y: x + y, numeros_pares, numeros_tres))

print(sumando_dos_iterables)

conver_str = (list(map(str, sumando_dos_iterables)))
print(conver_str)

personas = [
    {"nombre": "Alice", "edad": 25},
    {"nombre": "Bob", "edad": 30},
    {"nombre": "Charlie", "edad": 22}
]

users_names = (list(map(lambda name: name["nombre"], personas)))
users_age = (list(map(lambda age: age["edad"], personas)))

print(users_names)
print(users_age)

#1️⃣ Convertir Celsius a Fahrenheit

celsius = [0, 10, 20, 30, 40]

fahrenheit = (list(map(lambda c: (c * 9/5) + 32, celsius)))

print(fahrenheit)

#2️⃣ Capitalizar nombres en una lista

nombres = ["ana", "pedro", "maria", "juan"]

mayusculas = (list(map(lambda m: str.upper(m), nombres)))

print(mayusculas)

#3️⃣ Obtener longitudes de palabras

palabras = ["Python", "Decorators", "Map", "Function"]

longitud_palabras = list(map(len, palabras))

print(longitud_palabras)

emails = ["user1@gmail.com", "user2@yahoo.com", "user3@outlook.com"]

dominios = list(map(lambda d: d.split("@")[1], emails))

print(dominios)

#Question: Write a program which will find all such numbers which are divisible by 7 
# but are not a multiple of 5, between 2000 and 3200 (both included). 
# The numbers obtained should be printed in a comma-separated sequence on a single line.

numbers = list(range(2000,3200))

numbers_f = list(filter(lambda x: x % 7 == 0 and x % 5 != 0, numbers))

print(numbers_f)

from functools import reduce

cadena_str = reduce(lambda acomulador, numero: acomulador + '' + numero, str(numbers_f))

print(cadena_str)

l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))