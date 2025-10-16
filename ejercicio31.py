def es_par(num):
    if num % 2 == 0:
        print(f"El número {num} es par.")
    else:
        print(f"El número {num} es impar.")

num = int(input("Introduce un número: "))
es_par(num)
