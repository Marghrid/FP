def soma_quadrados(n):
    resultado = 0
    while n>0:
        resultado = resultado + n**2
        n = n-1
    return resultado