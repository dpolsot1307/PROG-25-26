numeros = [25, 12, 30, 10, 8]

suma_for = 0
for num in numeros:
    suma_for += num
print("Suma con for:", suma_for)

suma_while = 0
i = 0
while i < len(numeros):
    suma_while += numeros[i]
    i += 1
print("Suma con while:", suma_while)
