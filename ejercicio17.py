op = input("Operacion que quieres a realizar: (sumar, restar, multiplicar, dividir): ")

num1 = input("Primer nunmero: ")
num1 = int(num1)

num2 = input("Segundo numero: ")
num2 = int(num2)

if op == "sumar":
    print("Resultado: ", num1 + num2)
elif op == "restar":
    print("Resultado: ", num1 - num2)
elif op == "multiplicar":
    print("Resultado: ", num1 * num2)
elif op == "dividir":
    print("Resultado: ", num1 / num2)

