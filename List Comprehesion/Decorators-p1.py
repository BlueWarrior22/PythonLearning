#Un decorador es una funcion que recibe una funcion como argumento y le agrega alguna funcionalidad extra, devolviendo una nueva funcion modificada.

#Ejemplo:

def decorador(funcion_original):
    def envoltura():
        print('Antes de ejecutar la función')
        funcion_original()
        print('Despues de ejecutar la función') 
    return(envoltura)

@decorador
def saludo():
    print('Hola Wins')

saludo()

def mayusculas(funcion):
    def envoltura():
        resultado = funcion()
        return resultado.upper()
    return envoltura

@mayusculas

def mensaje():
    return 'hola wins!'

print(mensaje())

import time

def medir_tiempo(funcion):
    def envoltura():
        inicio = time.time()
        funcion()
        fin = time.time()
        print(f'Tiempo de ejecución: {fin-inicio:.5f} segundos')
    return envoltura

@medir_tiempo
def tarea():
    time.sleep(2) #Se simula un proceso de duracion 2 seg.
    print('Tarea completada')

tarea()

#🔹 3. Decorador para Verificar Permisos

def verificar_permisos(func):
    def envoltura(usuario):
        if usuario == 'admin':
            return func()
        else:
            return "Acceso restringido"
    return envoltura

@verificar_permisos
def funcion_top_secret():
    return "Información secreta revelada."

print (funcion_top_secret('admin'))
print (funcion_top_secret('invitado'))

#🔹 4. Decorador que Ejecuta una Función Varias Veces


def repetir(n):
    def decorador(funcion):
        def envoltura():
            for i in range (n):
                funcion()
        return envoltura
    return decorador

@repetir(10)
def hola():
    print('Hola Wins!')

hola()

#🔹 5. Decorador para Registrar Llamadas a una Función

def contador_llamadas(func):
    contador = 0
    def envoltura():
        nonlocal contador
        contador += 1
        print (f"La función {func.__name__} ha sido llamada {contador} veces")
        return func()
    return envoltura

@contador_llamadas
def saludo():
    print('Este es un saludo.')

saludo()
saludo()
saludo()
saludo()
saludo()

#🔹 6. Decorador para Validar Entradas de una Función

def validad_entradas(func):
    def envoltura(a, b):
        if b == 0:
            return 'Error, no se puede dividir entre 0'
        return func(a, b)
    return envoltura

@validad_entradas
def dividir(a, b):
    return a / b

print(dividir(10, 2))
print(dividir(10, 0))

#🔹 7. Decorador que Modifica el Mensaje de Retorno

def agregar_mensaje(func):
    def envoltura ():
        return func() + ' Que tengas un gran día!'
    return envoltura

@agregar_mensaje
def saludos():
    return 'Hola, Wins!'

print(saludos())

#🔹 8. Decorador con Parámetros Personalizados

def repetir_mensaje(n):
    def decorador(func):
        def envoltura():
            for _ in range(n):
                func()
        return envoltura
    return decorador

@repetir_mensaje(3)
def motiva():
    print("¡Tú puedes, Wins!")

#🔹 9. Decorador para Depurar Código

#Este muestra el nombre de la función y los argumentos con los que fue llamada.

def depurar(func):
    def envoltura(*args, **kwargs):
        print(f'Llamando a \'{func.__name__ }\' con argumentos {args} {kwargs}')
        return func(*args, **kwargs)
    return envoltura

@depurar
def sumar(a, b, c):
    return a + b + c

print(sumar(10, 5, 6))