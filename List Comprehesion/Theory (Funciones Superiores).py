# In Python the high-order functions (HOF) are functions that can take other functions as argument or return functions as results.
# HOF are a fundamental concept in functional programming.

def operar (v1, v2, fn):
    return fn (v1, v2)

def sumar (x1,x2):
    return x1 + x2

def restar (x1,x2):
    return x1 - x2

def multplicar (x1,x2):
    return x1 * x2

def dividir (x1,x2):
    return x1 / x2

result1 = operar(5, 6, sumar) #HOF
print(result1)

result2 = operar(21, 6, restar) #HOF
print(result2)

result3 = operar(10, 8, multplicar) #HOF
print(result3)

result4 = operar(24, 4, dividir) #HOF
print(result4)