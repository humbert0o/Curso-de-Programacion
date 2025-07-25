alumnos = {
    "Luis": {"Matemáticas", "Historia", "Biología"},
    "Ana": {"Matemáticas", "Física", "Química"},
    "Carlos": {"Historia", "Arte", "Biología"},
}

materias_unicas = set.union(*alumnos.values())
print("Materias únicas:",materias_unicas)

materias_comunes = alumnos["Luis"].intersection(alumnos["Ana"])
print("Materias comunes entre Luis y Ana:",materias_comunes)

alumnos["Carlos"].add("Física")

alumnos["Carlos"].discard("Arte")

for alumno, materias in alumnos.items():
    print(f"{alumno} cursa {len(materias)} materias.")
