from math import log

#Exercicio 1
def soma_digitos_pares (n):
    
    if isinstance (n, int):
        if n == 0:
            return 0
        elif n > 0:
            if n%2 == 0:
                return n%10 + soma_digitos_pares(n//10)
            
            else:
                return soma_digitos_pares(n//10)
        else:
            raise ValueError ('soma_digitos_pares:', 'O argumento não pode ser um número negativo')
    else:
        raise TypeError ('soma_digitos_pares:', 'O argumento deve ser um número inteiro')
    
#Exercicio 2
def apenas_digitos_impares (n):
    
    if isinstance (n, int):
        if n>0:
            if n%2 == 1:   
                if n<10:
                    return n
                else:
                    return n%10 + apenas_digitos_impares(n//10) * 10
            else:
                return apenas_digitos_impares(n//10)
        elif n == 0:
            return 0
        else:
            raise ValueError('apenas_digitos_impares:', 'o argumento deve ser um inteiro não negativo')
    else:
        raise TypeError('apenas_digitos_impares:', 'o argumento deve ser um inteiro')

#Exercicio 3
def sublistas (lst):
    if isinstance (lst, list):
        if len(lst) == 0:
            return 0
        if not isinstance(lst[0], list): #alternativamente, nesta linha posso por elif e colocar a linha 46 dentro de um else. É mais fácil de ler, mas faz o mesmo, com mais linhas.
            return sublistas(lst[1:])
        return 1 + sublistas(lst[0]) + sublistas(lst[1:])
                
    else:
        raise ValueError ('sublistas:', 'o argumento deve ser uma lista')

#Exercício 4
def calc_soma (x, n):
    def aux (x, n, termo, i, soma):
        if i>n:
            return soma
        return aux(x, n, termo * (x/(i+1)), i+1, soma + termo)
            
    if (isinstance(x, float) or isinstance(x, int)) and isinstance(n, int) and n>=0:   # validade dos argumentos
        return aux(x, n, 1, 0, 0)

    else:
        TypeError('calc_soma:','Os argumentos devem ser um número, real ou inteiro (x), e um inteiro não negativo (n)')

