#🔹 Ejemplo 2: Análisis de notas de estudiantes

"""
📌 Tenemos una lista de estudiantes con nombre y notas.
✅ Calculamos el promedio de cada estudiante.
✅ Filtramos solo los estudiantes aprobados (promedio ≥ 70).
✅ Calculamos el promedio general de la clase."""

from functools import reduce

estudiantes = [
    {"nombre": "Carlos", "notas": [80, 75, 90]},
    {"nombre": "Andrea", "notas": [60, 65, 58]},
    {"nombre": "Jorge", "notas": [70, 72, 78]},
    {"nombre": "Lucía", "notas": [95, 85, 92]},
    {"nombre": "Miguel", "notas": [50, 55, 40]}
]

promedio_estudiante = list(map(lambda e: {**e, 'promedio': round(sum(e['notas']) / len(e['notas']),2)},estudiantes))
#print(promedio_estudiante)

promedio_setenta = list(filter(lambda p: p['promedio']>=70, promedio_estudiante))
#print(promedio_setenta)

promedio_clase = reduce(lambda total, e: total + e['promedio'], promedio_estudiante, 0)/len(promedio_estudiante)


for e in promedio_estudiante:
    print(e)
print(promedio_clase)