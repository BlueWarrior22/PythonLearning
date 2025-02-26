#Ejemplo 1: Filtrar números pares de una lista

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda x : x%2 == 0, numeros))

print(pares)

#🔹 Ejemplo 2: Filtrar nombres con más de 5 letras

nombres = ["Ana", "Roberto", "Luis", "Carmen", "Juan"]

cinco_letras = list(filter(lambda longitud: len(longitud) >= 5, nombres))

print(cinco_letras)

#🔹 Ejemplo 3: Filtrar valores None de una lista

datos = [10, None, 20, "", 30, None, 40]

no_none = list(filter(lambda x: x is not None and x != '', datos))

print(no_none)

#🔹 Ejemplo 4: Filtrar palabras que contienen una letra específica

palabras = ["python", "java", "c++", "ruby", "javascript"]

contiene_a = list(filter(lambda x: 'a' in x, palabras))

print(contiene_a)

#🔹 Ejemplo 5: Filtrar estudiantes aprobados

estudiantes = [
    {"nombre": "Carlos", "nota": 85},
    {"nombre": "Ana", "nota": 40},
    {"nombre": "Pedro", "nota": 78},
    {"nombre": "Luis", "nota": 59},
]

aprobados = list(filter(lambda apro: apro["nota"] >= 60, estudiantes))

print(aprobados)

#Normalizar nombres de una lista


nombres = ["juan", "ANA", "PeDro", "jo", "maria", "LUIS", "al"]

nombres_normalizados = list(map(lambda x : x.capitalize(), nombres))

print(nombres_normalizados)

nombres_filtrados = list(filter(lambda x : len(x) > 3, nombres_normalizados))

print(nombres_filtrados)

#Filtrar y calcular precios con impuestos:

productos = [
    {"nombre": "Laptop", "precio": 1200},
    {"nombre": "Mouse", "precio": 50},
    {"nombre": "Teclado", "precio": 80},
    {"nombre": "Monitor", "precio": 300},
    {"nombre": "Silla", "precio": 150}
]

productos_caros = list(filter(lambda p: p['precio'] > 100, productos))

print(productos_caros)

precios_con_impuesto = list(map(lambda p: {'nombre': p['nombre'], 'precio final': round(p['precio']*1.10,2)}, productos_caros))

print(precios_con_impuesto)

#Filtrar palabras palíndromas:

palabras = ["radar", "python", "reconocer", "java", "oso", "casa", "ana"]

palindromas = list(filter(lambda x: x == x[::-1], palabras))

print(palindromas)

#Convertir temperaturas y filtrar:
'''
📌 Tenemos una lista de temperaturas en Celsius y queremos:
✅ Convertirlas a Fahrenheit.
✅ Filtrar las temperaturas mayores a 70°F.
'''

temperaturas_celsius = [10, 20, 30, 40, 50, 60, 70, 80]

fahrenheit = list(map(lambda x: round((x * 9/5) + 32, 2), temperaturas_celsius))

temperaturas_mayor_70 = list(filter(lambda x : x > 70, fahrenheit))

print(fahrenheit)
print(temperaturas_mayor_70)

#Filtrar correos electrónicos válidos:

'''
📌 Tenemos una lista de correos y queremos:
✅ Filtrar los que sean válidos (que contengan "@" y ".").
✅ Convertirlos a minúsculas.
'''

emails = ["User1@Gmail.com", "invalid-email", "test@outlook.com", "another@", "myemail@domain.com"]

correos_validos = list(filter(lambda x: '@' in x  and '.' in x, emails))

print(correos_validos)

correos_a_minusculas = list(map(lambda x: x.lower(), correos_validos))

print(correos_a_minusculas)

