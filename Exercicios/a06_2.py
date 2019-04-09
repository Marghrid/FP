# Funcionais sobre listas:
def transforma (tr, lista):
    res = list()
    for e in lista:
        res = res + [tr(e)]
    return res

def filtra (teste, lista):
    res = list()
    for e in lista:
        if teste(e):
            res = res + [e]
    return res

def acumula (fn, lst):
    res = lst [0]
    for i in range (1, len(lst)):
        res = fn (res, lst [i])
    return res


#  Exercício 1:
#  
#   (a) i. soma todos os naturais de 4 a 500 inclusive
#
#       ii. soma os quadrados de todos os múltiplos de 5, de 5 a 500 inclusive
#
#   (b):

def piatorio(linf, lsup, funcao):
    produto = 1
    while linf <= lsup:
        produto = produto * funcao (linf)
        linf = prox(linf)
    return produto

# (c)

def factorial (n):
    return piatorio (1, n, lambda y: y)

#Exercício 2:
#Funcionais sobre listas:
#     (i)   transforma (tr, lst)
#     (ii)  filtra (prod, lst)
#     (iii) acumula (op, lst)

def todos_lista (lst, predicado):
    return filtra(pred, lst) == lst
        
#Exercício 3:
def concentra (op, num):
    if num < 10:
        return num
    else:
        return op (num % 10, concentra (op, num // 10))
    
def produto (valor):
    return concentra(lambda x,y: x*y, valor)

# Exercício 4:

def muda(fn, num):
    if num < 10:   
        return fn(num)
    else:
        nn = fn(num % 10)
        return nn + 10 ** num_digitos(nn) * muda(fn, num // 10)
    
def num_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + num_digitos(n // 10)
    
def soma_dois (inteiro):
    return muda(lambda y: y+2, inteiro)

#Exercício 5: 
def op_els_lista(op, lst):
    if len (lst) > 2:
        return op (lst[0], lst[1:])
    return op (lst[0], lst[1])

def junta_listas (lista):
    return lista[0] + junta_listas (lista[1:])

#podia ter usar o acumula (op, lst) e escrever:
#    return acumula (lambda x, y: x+y, lst)

#Exercício 6:
def nenhum_p (n, p):
    for i in range (1, n+1):
        if p(i):
            return False
    return True