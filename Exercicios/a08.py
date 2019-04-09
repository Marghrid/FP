#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import random

# Exercicio 1:
l_nomes = [{'nome':{'nomep':'Jose', 'apelido':'Silva'}, 'morada':{'rua':'R. dos douradores', 'num': 34, 'andar':'6 Esq', 'localidade':'Lisboa', 'estado':'', 'cp':'1100-032', 'pais':'Portugal'}}, {'nome':{'nomep':'John', 'apelido':'Doe'}, 'morada':{'rua':'West Hazeltine Ave.', 'num': 57, 'andar':'', 'localidade':'Kenmore', 'estado':'NY', 'cp':'14317', 'pais':'USA'}}]

# (a)        l_nomes[1] = {'nome':{'nomep':'Jose', 'apelido':'Silva'}, 'morada':{'rua':'R. dos douradores', 'num': 34, 'andar':'6 Esq', 'localidade':'Lisboa', 'estado':'', 'cp':'1100-032', 'pais':'Portugal'}}
# (b)        l_nomes[1]['nome'] = {'nomep':'Jose', 'apelido':'Silva'}, 'morada':{'rua':'R. dos douradores', 'num': 34, 'andar':'6 Esq', 'localidade':'Lisboa', 'estado':'', 'cp':'1100-032', 'pais':'Portugal'}
# (c)        l_nomes[1]['nome'][apelido] = 'Silva'
# (d)        l_nomes[1]['nome'][apelido][0] = 'S'

# Exercicio 2 (a):
def baralho ():
    retorno = []
    naipes = ('espadas', 'copas', 'ouros', 'paus')
    valores = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K')
    for np in naipes:
        for vlr in valores:
            retorno = [{'np': np, 'vlr': vlr}] + retorno
    
    return retorno

# Exercicio 2 (b):
def baralha (baralho):
    n_cartas = len (baralho)
    for carta in range(len(baralho)):
        aleatorio = int(random()) * (n_cartas-1)
        baralho[carta], baralho[aleatorio] = baralho[aleatorio], baralho[carta]
        
    return baralho

# Exercicio 3:
def distribui (baralho):
    ret = [[],[],[],[]]
    nr_cartas = len(baralho)
    for carta in range (nr_cartas):
        jogador = carta % 4
        ret[jogador] = ret[jogador] + [baralho[carta]]
    return ret


def conta_palavras(string):
    palavra = ''
    nr_palavras = {}
    string = string + ' '
    for i in string:
        if i != ' ':
            palavra = palavra + i
        else:
            if palavra in nr_palavras:
                nr_palavras[palavra] = nr_palavras[palavra] + 1
            else:
                nr_palavras[palavra] = 1
            palavra = ''
                
    return nr_palavras

# Exercicio 4:
def mostra_ordenado (dicionario):
    lista = []
    for elemento in dicionario:
        lista = lista + [elemento]
    lista = ordena (lista)
    for elemento in lista:
        print (elemento, ': ', dicionario[elemento], sep = '')
        
def ordena (lista):
    maior_indice = len (lista) - 1
    trocas = True
    while trocas:
        trocas = False
        for i in range (maior_indice):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                trocas = True
        maior_indice = maior_indice - 1
    
    return lista

# Exercicio 5:

def escreve_esparsa (diciomatriz):
    n_linhas, n_colunas = 0, 0
    for elemento in diciomatriz:
        if elemento[0] > n_linhas:
            n_linhas = elemento[0]
        if elemento [1] > n_colunas:
            n_colunas = elemento[1]
       
    for linha in range (n_linhas + 1):
        for coluna in range (n_colunas + 1):
            if (linha, coluna) in diciomatriz:
                print (diciomatriz[(linha, coluna)], end = '   ')
                
            else:
                print (0, end='   ')
        print ()
        
def soma_esparsas (diciomatriz1, diciomatriz2):
    for element in diciomatriz2:
        if element in diciomatriz1:
            diciomatriz1[element] = diciomatriz1[element] + diciomatriz2[element]
        else:
            diciomatriz1[element] = diciomatriz2[element]
    escreve_esparsa(diciomatriz1)        

# Exercicio 6:

def mais_antigo (bib):
    titulo_mais_antigo, ano_mais_antigo = bib[0]['titulo'], bib[0]['ano']
    for livro in bib:
        if livro['ano'] < ano_mais_antigo:
            ano_mais_antigo = livro['ano']
            titulo_mais_antigo = livro['titulo']
    return titulo_mais_antigo

a = [{'autores': ['G. Arroz', 'J. Monteiro', 'A. Oliveira'],
      'titulo': 'Arquitectura de computadores',
'editor': 'IST Press',
'cidade': 'Lisboa',
'ano': 2007,
'numpags': 799,
'isbn': '978-972-8469-54-2'},
     
     {'autores': ['J.P. Martins'],
'titulo': 'Logica e Raciocinio',
'editor': 'College Publications',
'cidade': 'Londres',
'ano': 2014,
'numpags': 438,
'isbn': '978-1-84890-125-4'}]

# Exercicio 7:
def inverte_dic (dicionario):
    resultante = {}
    for key in dicionario:
        for  element in dicionario [key]:
            if element in resultante:
                resultante [element] = resultante [element] + [key]
            else:
                resultante [element] = [key]
    return resultante

# Exercício 8:
def ataques_rainhas (dicioxadrez):
    rainhas = ()
    for posicao in dicioxadrez:
        if dicioxadrez[posicao][1] == 'rainha':
            rainhas = rainhas + (posicao,)
        for posicao in rainhas:
            res = ataques_possiveis(posicao)
       # for 
        
        
def ataques_possiveis (posicao):
    ataques, pos = (), []
    #for coluna in (1, 2, 3, 4, 5, 6, 7, 8, 9):
    #   for linha in range ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'):
   # while pos != list(posicao):
        