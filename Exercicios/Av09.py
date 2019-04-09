# Suponham que bib � uma lista correspondente aos livros que existem numa biblioteca. Cada elemento da lista representa um livro, sob a forma de um dicionario, com entradas 'Autores', 'ano de publica��o', 'numero de p�ginas do livro', etc. Escreva uma fun��o media_paginas que recebe uma bib e calcula a media do numero de paginas dos livros da biblioteca.

def media_paginas (bib):
    pags_total = 0
    for livro in bib:
        pags_total = pags_total + livro ['numpags']
    return pags_total / len(bib)