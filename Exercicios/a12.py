# Exercício 1:
# TAD Pilha:
def nova_pilha():
    pilha = []
    return pilha

def empurra (pilha, elemento):
    pilha = pilha + [elemento,]
    return pilha

def topo (pilha):
    if not pilha_vazia(pilha):
        ult = len(pilha) - 1
        return pilha[ult]
    else:
        return ValueError ('pilha.topo: a pilha deve conter, pelo menos um elemento')
    
def tira (pilha):
    pilha = pilha[:len(pilha)-1]
    return pilha

def e_pilha(arg):
    return isinstance (arg, list)

def pilha_vazia (pilha):
    return pilha == []

def pilhas_iguais (p1, p2):
    return p1 == p2

# como eu fiz em casa:
def palindromo2(string):
    p = nova_pilha()
    comp = len(string)
    for i in range(comp//2):
        p = empurra(p, string[i])
    for i in range ((comp+1)//2, comp):
        if topo(p) == string[i]:
            p = tira(p)
        else:
            return False
    return True

# como a professora fez na aula:
def palindromo(cad):
    comp = len (cad)
    meio = comp //2
    p = nova_pilha()
    for i in range (meio):
        p = empurra (p, cad[i])
    meio = meio + comp % 2
    for i in range (meio, comp):
        if topo (p) != cad [i]:
            return False
        else:
            return pilha_vazia(p)
    

# Exercício 2:
# TAD Fila:
class fila:
    def __init__(self):
        fila.els = []

    def inicio(self):
        return fila.els[0]
    
    def comprimento(self):
        return len(fila.els)
    
    def coloca(self, elemento):
        fila.els = fila.els + [elemento]
        return fila
    
    def retira(self):
        fila.els = fila.els[1:]
        return fila
    
    def fila_para_lista(self):
        return self.els
    
    def fila_vazia(self):
        return fila.els == []
    
    def __repr__ (self):
        rep = '< ' + str(fila.els[0])
        for el in fila.els[1:]:
            rep = rep + ', ' + str(el)
        rep = rep + ' <'
        return rep
    
def soma_fila (fila):
    lista = fila_para_lista(fila)
    soma = 0
    for el in lista:
        soma = soma + el
    return soma