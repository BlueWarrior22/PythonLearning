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

def decorador_con_parametros(func):
    def envoltura(p1, p2, p3):
        func(p1, p2, p3)
        print('{} vive en {}'.format(p1, p3))
    return envoltura

@decorador_con_parametros
def imprimir_nombre_completo(nm1, ap1, pa1):
    print('Hola, Mi nombre completo es {} {}.'.format(nm1, ap1, pa1))

imprimir_nombre_completo('Javier', 'Perez', 'Nicaragua')