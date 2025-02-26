#🔹 Ejemplo 1: Procesar una lista de empleados
"""📌 Tenemos una lista de empleados con su nombre, salario y años de experiencia.
✅ Aplicamos un aumento del 15% a los empleados con más de 5 años de experiencia.
✅ Filtramos empleados con salario mayor a $3000.
✅ Calculamos el total que la empresa pagará después del aumento."""

from functools import reduce

empleados = [
    {"nombre": "Juan", "salario": 2500, "experiencia": 6},
    {"nombre": "Ana", "salario": 4000, "experiencia": 4},
    {"nombre": "Luis", "salario": 3200, "experiencia": 8},
    {"nombre": "Marta", "salario": 2800, "experiencia": 10},
    {"nombre": "Pedro", "salario": 1500, "experiencia": 3}
]

aumento_empleados = list(map(lambda emp: {**emp,'salario': round(emp['salario'] * 1.15, 2)} if emp['experiencia'] > 5 else emp, empleados))
#print(empleados)
#print(aumento_empleados)
empleados_mayor_tresmil = list(filter(lambda a: a['salario']>3000, aumento_empleados))
print(empleados_mayor_tresmil)

total_salarios = reduce(lambda total, s_empleado: total + s_empleado['salario'], aumento_empleados, 0)
print('total salarios = ',total_salarios)