#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt

# Exercício 1
def cinco(x):
    return x==5

# Exercício 2
def horas_dias(horas):
    return horas/24

# Exercício 3
def bissexto (ano):
    return (ano%4 == 0 and ano%100 != 0) or ano%400 == 0

# Exercício 4
def arctg (x, termos):
    arctg, sinal, potencia_x = 0, 1, x
    for n in range(termos):
        # Eu tinha:
        #arctg=arctg+((((-1)**n)*(x**(2*n+1)))/2*n+1)
        # Mas pode ser:
        #arctg = arctg + (-1)**n*x**2*n+1/(2*n+1)
        # No entanto, para evitar calcular expoentes muito elevados, posso calcular cada while a partir do anterior, usando uma variável para sinal, e uma para a potencia de x em questão:
        arctg = arctg + sinal * potencia_x / (2*n+1)
        potencia_x = potencia_x * x**2
        sinal = -sinal
    return arctg

# Exercício 5
def dia_da_semana (dia, mes, ano):
    if mes==1 or mes==2:
        mes=12+mes
        ano=ano-1
    dia_da_semana = (dia + ((13*(mes+1))//5) + ano%100 + ((ano%100)//4) + ((ano//100)/4) - 2*(ano//100)) % 7
    if dia_da_semana == 0:
        return 'Sábado'
    elif dia_da_semana == 1:
        return 'Domingo'
    elif dia_da_semana == 2:
        return 'Segunda-feira'
    elif dia_da_semana == 3:
        return 'Terça-feira'
    elif dia_da_semana == 4:
        return 'Quarta-feira'
    elif dia_da_semana == 5:
        return 'Quinta-feira'
    elif dia_da_semana == 6:
        return 'Sexta-feira'

# Exercício 6
def triangular (n):
    i=1
    while n>0:
        n=n-i
        i=i+1
    return n==0 and i>1

# Exercício 7
def primo(n):
    divisor = 2
    if n == 1:
        return False
    while divisor <= sqrt(n):
        if n%divisor == 0:
            return False
        divisor = divisor + 1
    return True

# Exercício 8
def n_esimo_primo (n):
    primos, primot = 0, 1
    while primos < n:
        if primo(primot):
            primos = primos + 1
        primot = primot + 1
    return primot-1