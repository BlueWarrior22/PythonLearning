#Se pueden usar múltiples decoradores en una misma función. 
#Python los aplica de arriba hacia abajo, es decir, el decorador más cercano a la función se ejecuta primero.

def mayusculas(func):
    def envoltura():
        return func().upper()
    return envoltura

def agregar_mensaje(func):
    def envoltura():
        return func() + " Sigue así, Tu puedes!"
    return envoltura

@mayusculas
@agregar_mensaje
def saludos_1():
    return "Hola, Wins!"

print(saludos_1())


import time

def medir_tiempo(func):
    def envoltura():
        inicio = time.time()
        resultado = func()
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.2f} segundos")
        return resultado
    return envoltura

def depurar(func):
    def envultura():
        print(f'Llamando a \'{func.__name__}\':')
        return func()
    return envultura

@medir_tiempo
@depurar
def tarea_1():
    time.sleep(1)
    print("Tarea completada.")

tarea_1()