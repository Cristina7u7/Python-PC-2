def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

numero = int(input("Inserte un número entero que sea no negativo: "))
resultado = factorial(numero)
print("El factorial es: ", resultado)