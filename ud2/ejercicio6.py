# Pedir cuántos números se van a introducir
cantidad = int(input("¿Cuántos números deseas introducir?: "))

numeros = []  # Lista donde guardaremos los números

# Introducir los números por teclado
for i in range(cantidad):
    num = int(input(f"Introduce el número {i+1}: "))
    numeros.append(num)

# Mostrar en orden inverso
print("Los números en orden inverso son:")
for num in reversed(numeros):
    print(num)
