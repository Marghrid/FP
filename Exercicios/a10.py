#!/usr/bin/env python
# -*- coding: utf-8 -*-

from a08 import ordena

def conta_vogais(fich):
    f = open(fich, 'r', encoding = 'UTF-8')
    vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    linha = f.readline()
    while linha != '':
        for el in linha:
            if el in ('a', 'e', 'i', 'o', 'u'):
                vogais[el] = vogais[el] + 1
        linha = f.readline()
    f.close()
    return vogais

def inverte(fich1, fich2):
    f1 = open(fich1, 'r', encoding = 'UTF-8')
    linhas = f1.readlines()
    f1.close
    f2 = open(fich2, 'a', encoding = 'UTF-8')
    print(file=f2)
    for i in range (len(linhas)-1, -1, -1):
        f2.write(linhas[i] + '\n')
    f2.close()

def concatena (lst, fich):
    linhas = []
    for file in lst:
        f = open(file, 'r', encoding = 'UTF-8')
        linhas = linhas + f.readlines() + ['\n']
        f.close ()
    f2 = open (fich, 'w', encoding = 'UTF-8')
    for line in linhas:
        f2.write(line)
    f2.close()
    
def procura(palavra, ficheiro):
    f = open (ficheiro, 'r', encoding = 'UTF-8')
    linhas = f.readlines()
    for linha in linhas:
        if palavra in linha:
            print (linha)

def corta(fichin, fichout, n):
    if isinstance (n, int) and n >= 0:
        fin = open (fichin, 'r', encoding = 'UTF-8')
        conteudo = fin.read()
        fin.close()
        conteudo = conteudo[:n]
        fout = open (fichout, 'w', encoding = 'UTF-8')
        fout.write(conteudo)
        fout.close()

def ordena_ficheiro(fich):
    f = open(fich, 'r', encoding = 'UTF-8')
    linhas = f.readlines()
    linhas = ordena(linhas)
    f.close()
    for linha in linhas:
        print (linha[:len(linha)-1])