import random as r
import string as s

inventor_1 = "Nikola Tesla"  # Contribuyó a la corriente alterna y la radio.
inventor_2 = "Thomas Edison"  # Desarrolló la bombilla eléctrica y el fonógrafo.
inventor_3 = "Alexander Fleming"  # Descubrió la penicilina.
inventor_4 = "Alan Turing"  # Padre de la computación moderna y descifrador de códigos en la Segunda Guerra Mundial.
inventor_5 = "Tim Berners-Lee"  # Inventor de la World Wide Web.

lst_inventor_1 = [i for i in inventor_1]
print(lst_inventor_1)

lst_inventor_2 = [i for i in inventor_2]
print(lst_inventor_2)

lst_inventor_3 = [i for i in inventor_3]
print(lst_inventor_3)

lst_inventor_4 = [i for i in inventor_4]
print(lst_inventor_4)

lst_inventor_5 = [ i for i in inventor_5]
print(lst_inventor_5)

personas = [
    ("Carlos", r.randint(15, 50)),
    ("Andrea", r.randint(15, 50)),
    ("Javier", r.randint(15, 50)),
    ("Sofía", r.randint(15, 50)),
    ("Luis", r.randint(15, 50)),
    ("Elena", r.randint(15, 50)),
    ("Fernando", r.randint(15, 50)),
    ("Marta", r.randint(15, 50)),
    ("Diego", r.randint(15, 50)),
    ("Valeria", r.randint(15, 50))
]

persona_mayor_edad = [pm for pm in personas if pm[1]>=18]
print(len(persona_mayor_edad))
print(persona_mayor_edad)

multiplos_8 = [valor for valor in range(1, 501) if valor%8 == 0]
print(multiplos_8)
print()

nombres = [
    "Carlos", "Andrea", "Javier", "Sofía", "Luis", 
    "Elena", "Fernando", "Marta", "Diego", "Valeria",
    "Gabriel", "Camila", "Raúl", "Isabela", "Matías",
    "Lucía", "Pedro", "Mariana", "José", "Daniela"
]

nombres_compuestos = [[n1, n2] for n1 in nombres for n2 in nombres if n1 != n2]
print(nombres_compuestos)

print()

print(['Fizz'*(not nro%3) + 'Buzz'*(not nro%5) or nro for nro in range(1, 101)])