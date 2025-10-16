def es_par(num):
    return "par" if num % 2 == 0 else "impar"

num = int(input("Introduce un número: "))
print(f"El número {num} es {es_par(num)}.")
