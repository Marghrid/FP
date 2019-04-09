# Devolve o número de inteiros positivos menores ou iguais a n que satisfazem p

def conta_p (n, pred):
    soma = 0
    for i in range (1, n+1):
        if pred(i):
            soma = soma + 1
    return soma