# Exercício 1:
#    (a) A função mistério retorna 'pos' se n for positivo e 'neg' se n for negativo
#    (b) A função misterio_aux é recursiva porque ser chama a si própria. A função misterio é recursiva de causa pouque tem uma função auxiliar que é recursiva
#    (c) Ahmm pois.
#    (d) É um processo recursivo, porque o espaço de memória aumenta linearmente com n




# Exercício 6:
def numero_digitos (numero):
    valor, nr_digitos = 1, 0
    while numero >= 1:
        numero = numero/10
        nr_digitos = nr_digitos + 1
    return nr_digitos

# Exercício 7:
def e_capicua (numero):
    nr_digitos = numero_digitos (numero)
    for a in range(1,nr_digitos//2):
        esquerda = numero % 10**a
        direita = numero // 10**(nr_digitos-a)
        if not esquerda == direita:
            return False
    return True