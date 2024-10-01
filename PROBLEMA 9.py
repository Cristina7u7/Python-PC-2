def eliminar_vocales(cadena):
    vocales = "aeiouAEIOU"
    return ''.join([letra for letra in cadena if letra not in vocales])

entrada = input("Ingresa un pequeño texto: ")
salida = eliminar_vocales(entrada)
print(salida)