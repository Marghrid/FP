#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fractions import gcd
from math import sqrt
from a03 import bissexto

def nr_dias_mes (mes, ano):
    if isinstance (mes, int) and 0 < mes < 13:
        if mes in (1, 3, 5, 7, 8, 10, 12):
            return 31
        if mes in (4,6,9,11):
            return 30
        if bissexto (ano):
            return 29
        return 28
    

class racional:
    def __init__ (self, num, den):
        if isinstance (num, int) and isinstance (den, int):
            div = gcd (num, den)    
            self.num = num // div   
            self.den = den // div
        else:
            raise TypeError ("racional.__init__: Os argumentos não são números")
        
    def __mul__ (self, other):
        prod_num = self.num * other.num
        prod_den = self.den * other.den
        div = gcd(prod_num, prod_den)
                
        return racional (prod_num // div, prod_den // div)
    
    def __add__ (self, other):
        soma_den = self.den * other.den
        soma_num = self.num * other.den + other.num * self.den
        div = gcd (soma_num, soma_den)
        
        return racional (soma_num // div, soma_den // div)
    
    def __repr__ (self):
        return str(self.num) + '/' + str(self.den)
    
    def __eq__ (self, other):
        return self.num * other.den == other.num * self.den
    
cria_rac = racional

def escreve_rac (rac):
    return rac
 
 
# Exercício 2:
class clock:
    def __init__ (self, horas, minutos, segundos):
        if isinstance (horas, int) and isinstance (minutos, int) and isinstance (segundos, int) :
            if 0 <= horas < 24 and 0 <= minutos < 60 and 0 <= segundos < 60:
                self.segundos, self.minutos, self.horas = minutos, horas, segundos
            else:
                raise ValueError ("clock.__init__: Os argumentos correspondentes \n\
                às horas, aos minutos ou aos segundos possuem valores inválidos")
        else:
            raise TypeError ("clock.__init__: Os argumentos não são números")
            
            
    def __repr__ (self):
        rel = str (self.horas) + ':'
        if self.horas < 10:
            rel = '0' + rel
        if self.minutos < 10:
            rel = rel + '0'
        rel = rel + str(self.minutos) + ':'      
        if self.segundos < 10:
            rel = rel + '0'
        rel = rel + str(self.segundos)      
        
        return rel

    def __eq__ (self, other):
        return self.horas == other.horas and self.minutos == other.minutos and self.segundos == other.segundos
    
    def __lt__ (self, other):
        return self.horas < other.horas or (self.horas == other.horas and (self.minutos < other.minutos or (self.minutos == other.minutos and self.segundos < other.segundos)))
        
    def diferenca_segundos (self, other):
        if self < other:
            return 3600 * (other.horas - self.horas) + 60 * (other.minutos - self.minutos) + other.segundos - self.segundos
        return ValueError

        
# Exercício 3:   
class data:
    def __init__ (self, dia, mes, ano):
        if isinstance(ano, int) and isinstance (mes, int) and isinstance (dia, int):
            if 0 < mes < 13 and 0 < dia <= nr_dias_mes (mes, ano):
                self.ano, self.mes, self.dia = ano, mes, dia
            else:
                raise ValueError ("data.__init__: Os argumentos correspondentes\n\
                ao dia e ao mês possuem valores inválidos")
        else:
            raise TypeError ("data.__init__: Os argumentos não são números")
    def __repr__ (self):
        if self.ano >= 0:
            return str(self.dia) + '/' + str(self.mes) + '/' + str(self.ano)
        return str(self.dia) + '/' + str(self.mes) + '/' + str(-self.ano) + ' AC'
    
    def __eq__ (self, other):
        return self.ano == other.ano and self.mes == other.mes and self.dia == other.dia
        
    def __lt__ (self, other):
        return self.ano < other.ano or (other.ano == self.ano and (self.mes < other.mes or (other.mes == self.mes and self.dia < other.dia)))
    
    def data_anterior (self, other):
        return self < other
       
    def idade (self, other):
        idade = other.ano - self.ano
        if self.mes > other.mes:
            idade = idade - 1
        elif self.mes == other.mes and self.dia > other.dia:
            idade = idade - 1
        return idade

# Exercício 4:
class ponto:
    def __init__ (self, xx, yy):
        if isinstance (xx, (int, float)) and isinstance (yy, (int, float)):
            self.x, self.y = xx, yy
        else:
            raise TypeError ("ponto.__init__: Os argumentos não são números")        
    
    def __repr__ (self):
        return '(' + str (self.x) + ',' + str (self.y) + ')'
            
    def distancia (self, other):
        return sqrt ( (self.x - other.x)**2 + (self.y - other.y)**2 )
    
    def quadrante (self):
        if self.x >= 0:
            if self.y >= 0:
                return 1
            return 2
        if self.y >= 0:
            return 4
        return 3

# Exercício 5:
class timestamp:
    def __init__ (self, dat, clk):
        if isinstance (dat, data) and isinstance (clk, clock):
            self.data, self.clock = dat, clk
        else:
            raise TypeError("timestamp.__init__: os argumentos são inválidos: \n\
            (1)  O primeiro argumento não é uma data, ou \n\
            (2)  O segundo argumento não é um clock")
            
    def __repr__ (self):
        return "data: " + str (self.data) + ";    time: " + str (self.clock)
    
    def __lt__ (self, other):
        return self.data < other.data or (self.data == other.data and self.clock < other.clock)
        
    def depois (self, other):
        return other < self
    
    def num_segundos (self):
        return self.data.ano * 31557600 + (self.data.mes * nr_dias_mes(self.data.mes, self.data.ano) + self.data.dia) * 86400 + self.clock.horas * 3600 + self.clock.minutos * 60 + self.clock.segundos
# Exercício 6:
class vector:
    def __init__ (self, xx, yy):
        if isinstance (xx, (int, float)) and isinstance (yy, (int, float)):
            self.x, self.y = xx, yy
        else:
            raise TypeError ("Os argumentos não são números")
    def __repr__ (self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
        
    def __eq__ (self, other):
        return self.x == other.x and self.y == other.y
        
    def abcissa (self):
        return self.x
    
    def ordenada (self):
        return self.y
 
    def eh_vetor_nulo (self):
        return self.x == 0 and self.y == 0
    
   
def eh_vetor (arg):
    return isinstance (arg, vector)

def vetores_iguais (v1, v2):
    return v1 == v2
    

# Exercício 7:
class pilha:
    def __init__ (self, *args):
        self.els = list (args)
        
    def __repr__ (self):
        ret = ''
        for el in self.els:
            ret = '\n' + str(el) + ret
        return ret
    
    def topo (self):
        self.els = self.els[len(self.els)]
        return self
    
    def empurra (self, arg):
        self.els = self.els + [arg]
        return self
    
    def tira (self):
        self.els = self.els [:len(self.els)-1]
        return self
    
    def e_pilha_vazia (self):
        return not self.els
    
    def __eq__ (self, other):
        return self.els == other.els
    