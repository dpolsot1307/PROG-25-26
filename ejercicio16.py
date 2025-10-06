sobresaliente = [9, 10]
notable = [8, 7]
bien = [6]
suficiente = [5]
insuficiente = [0, 1, 2, 3, 4]

nota = int(input("Escribe tu nota: "))

if nota in sobresaliente:
    print("Sobresaliente")
elif nota in notable:
    print("Notable")
elif nota in bien:
    print("Bien")
elif nota in suficiente:
    print("Suficiente")
elif nota in insuficiente:
    print("Insuficiente")

