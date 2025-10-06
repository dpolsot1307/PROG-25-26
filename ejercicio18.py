a = int(input("Introduce el primer lado: "))
b = int(input("Introduce el segundo lado: "))
c = int(input("Introduce el tercer lado: "))

if a + b > c and a + c > b and b + c > a:
    print("Los lados forman un triángulo.")
    if a == b == c:
        print("Es un triángulo equilátero.")
    elif a == b or a == c or b == c:
        print("Es un triángulo isósceles.")
    else:
        print("Es un triángulo escaleno.")
else:
    print("Los lados NO pueden formar un triángulo.")
