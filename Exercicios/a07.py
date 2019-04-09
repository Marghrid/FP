# Exerc�cio 1:
#    (a) A fun��o mist�rio retorna 'pos' se n for positivo e 'neg' se n for negativo
#    (b) A fun��o misterio_aux � recursiva porque ser chama a si pr�pria. A fun��o misterio � recursiva de causa pouque tem uma fun��o auxiliar que � recursiva
#    (c) Ahmm pois.
#    (d) � um processo recursivo, porque o espa�o de mem�ria aumenta linearmente com n




# Exerc�cio 6:
def numero_digitos (numero):
    valor, nr_digitos = 1, 0
    while numero >= 1:
        numero = numero/10
        nr_digitos = nr_digitos + 1
    return nr_digitos

# Exerc�cio 7:
def e_capicua (numero):
    nr_digitos = numero_digitos (numero)
    for a in range(1,nr_digitos//2):
        esquerda = numero % 10**a
        direita = numero // 10**(nr_digitos-a)
        if not esquerda == direita:
            return False
    return True