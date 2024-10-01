def es_numero_perfecto(numero):
    divisores = [i for i in range(1, numero) if numero % i == 0]
    return sum(divisores) == numero

def numeros_perfectos_menores(limite):
    perfectos = []
    for num in range(1, limite):
        if es_numero_perfecto(num):
            perfectos.append(num)
    return perfectos

limite = 1000
numeros_perfectos = numeros_perfectos_menores(limite)
print(numeros_perfectos)