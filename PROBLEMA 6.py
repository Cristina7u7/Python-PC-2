def fibonacci_hasta(limite):
    fibonacci = [0, 1]  
    while True:
        siguiente = fibonacci[-1] + fibonacci[-2]
        if siguiente > limite:
            break
        fibonacci.append(siguiente)
    return fibonacci

limite = 50
serie_fibonacci = fibonacci_hasta(limite)
print(serie_fibonacci)