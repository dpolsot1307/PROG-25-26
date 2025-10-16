def cuentaA(texto):
    cuenta = texto.count("a") + texto.count("A")
    return cuenta

frase = "Hola y Adios"
print(cuentaA(frase))
