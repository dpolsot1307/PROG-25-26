# Tabla de sueldos inicial
sueldos = [1800, 1200, 2000, 1200, 900]

print("Sueldos sin aumento:")
print(sueldos)

# Con esto aumento un 10% a cada sueldo
for i in range(len(sueldos)):
    sueldos[i] = sueldos[i] * 1.10

print("Sueldos actualizados con el 10% de aumento:")
print(sueldos)
