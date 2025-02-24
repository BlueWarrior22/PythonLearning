import string

#lista = list(map(int, string.digits))
numbers = list(range(0,101))

#print(lista)
#print(numbers)

def imprimir_if (lista, fn):
    output = []
    for elemento in lista:
            if fn(elemento):
                output.append(elemento)
    print(output)

imprimir_if(numbers, lambda x : x%2 == 0)
imprimir_if(numbers, lambda x: x%3 == 0 or x%5 == 0)
imprimir_if(numbers, lambda x: x >= 50)
imprimir_if(numbers, lambda x: x>=10 and x<=50 or x>=80 and x<=100)