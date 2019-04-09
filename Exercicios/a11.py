from math import gcd
from random import randrange

# Exercício 1:
class racional:
    def __init__ (self, n, d):
        if isinstance (n, int) and isinstance (d, int) and d != 0:
            self.num = n // gcd(n, d)
            self.den = d // gcd(n, d)
        else:
            raise ValueError ('O primeiro argumento (numerador) deve ser um inteiro,\n\
        e o segundo argumento (denominador) deve ser um inteiro diferente de zero')
    
    def nume (self):
        return self.num
    
    def deno (self):
        return self.den
    
    def __eq__(self, other):
        self.num * other.deno() == self.den * other.nume()
        
    def __lt__ (self, other):
        self.num * other.deno() < self.den * other.nume()
    
    def __add__(self, other):
        return racional (self.num * other.deno() + self.den * other.nume(), self.den * other.deno())
    
    def __mul__ (self, other):
        return racional(self.num * other.nume(), self.den * other.deno())  

    def __repr__ (self):
        if self.den < 0:
            return str(-self.num) + '/' + str(-self.den)
        return str(self.num) + '/' + str(self.den)

# Exercício 2:
class estacionamento:
    def __init__(self, lot):
        if isinstance(lot, int) and lot >= 0:
            self.lot = lot
        else:
            raise ValueError ('estacionamento: O argumento deve ser um inteiro não negativo')
    
    def entra (self):
        self.lot = self.lot - 1
    
    def sai (self):
        self.lot = self.lot + 1
    
    def lugares (self):
        return self.lot

# Exercício 3:
class conjunto:
    def __init__ (self):
        self.els = []
    
    def insere(self, el):
        if el not in self.els:
            self.els = self.els + [el]
            return self
        return el
    
    def elementos (self):
        return tuple (self.els)
    
    def el_conj(self):
        if self.els != []:
            i = randrange(len(self.els))-1
            return self.els[i]
    
    def retira_conj(self, el):
        if el in self.els:
            self.els.remove(el)
            return self
        return el

    def cardinal(self):
        return len(self.els)
    
    def e_conj_vazio (self):
        return self.els == []
    
    def pertence (self, el):
        return el in self.els
    
    def __repr__ (self):
        c = '{'
        c = c + str(self.elementos()[0])
        for el in self.elementos()[1:]:
            c = c + ', ' + str(el)
        c = c + '}'
        return c
    
def subconjunto (c1, c2):
    if isinstance (c1, conjunto) and isinstance (c2, conjunto):
        for el in c1.elementos():
            if not c2.pertence(el):
                return False   
        return True
    raise TypeError ('subconjunto: Os argumentos devem ser conjuntos')

def uniao (c1, c2):
    if isinstance (c1, conjunto) and isintance (c2, conjunto):
        uni = conjunto()
        for el in c1.elementos():
            uni.insere(el)
        for el in c2.elementos():
            uni.insere(el)
        return uni
    raise TypeError ('uniao: Os argumentos devem ser conjuntos')

def interseccao (c1, c2):
    if isinstance (c1, conjunto) and isinstance (c2, conjunto):
        inte = conjunto()
        for el in c1.elementos:
            if c2.pertence(el):
                inte.insere(el)
        return inte
    raise TypeError ('interseccao: Os argumentos devem ser conjuntos')
def diferenca (c1, c2):
    if isinstance (c1, conjunto) and isinstance (c2, conjunto):
        dif = conjunto()
        for el in c1.elementos():
            if not c2.pertence (el):
                dif.insere(el)
        return dif
    raise TypeError ('diferenca: Os argumentos devem ser conjuntos')
    
    
# Exercício 4:
class mem_A:
    def __init__(self):
        self.vals = {}
        
    def val(self, m, n):
        if (m, n) in self.vals:
            return self.vals[(m, n)]
        elif m == 0:
            self.vals[(m, n)] = n + 1
            return n + 1        #neste caso tanto faz returnar o valor do dicionário ou n+i porque a operação é simples
        elif m > 0 and n == 0:
            self.vals[(m, n)] = self.val(m-1, 1)
            return self.vals[(m, n)]   #aqui retorna o valor do dicionário para não voltar a chamar a função, porque isso é ineficiente
        elif m > 0 and n > 0:
            self.vals[(m, n)] = self.val (m-1, self.val (m, n-1))
            return self.vals[(m, n)]
        else:
            raise ValueError('mem_A: Os argumentos são inválidos')
    def mem (self):
        return self.vals