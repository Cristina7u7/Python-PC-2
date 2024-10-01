pares = 0
impares = 0
numeros_ingresados = []

while True:
    desea_ingresar = input("¿Desea ingresar un número? (SI/NO): ").upper()
    if desea_ingresar == 'NO':
        break
    
    numero = int(input("Ingrese el número: "))
    numeros_ingresados.append(numero)
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Mostrar resultados
print("\nNúmeros ingresados:", numeros_ingresados)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)