
# Exercicio 1:
def valida_isbn (isbn):
    """Recebe como argumento um string correspondente a um ISBN, e devolve True se for valido"""
    if isinstance (isbn, str) and isinstance (eval(isbn), int):
        soma = 0
        for i in range(len(isbn)):
            if i%2 == 0:
                soma = soma + eval(isbn[i])
            else:
                soma = soma + 3*eval(isbn[i])
        return soma%10 == 0
    else:
        raise TypeError('O argumento deve ser uma string contendo um inteiro')

# Exercicio 2:
def junta_ordenadas (lista1, lista2):                    
    
    if isinstance (lista1, list) and isinstance (lista2, list):
        comp_lista1, comp_lista2 = len(lista1), len(lista2)
        i, j = 0, 0
        while i < comp_lista1:
            while lista1[i] > lista2[j] and j < comp_lista2 - 1:
                j = j + 1
                # aqui o j vai ser a primeira entrada da lista2 que e maior do que a entrada i da lista 1
            
            lista2 = lista2 + [0]
            
            for a in range (comp_lista2, j, -1):
                lista2[a] = lista2[a-1]
            
            lista2[j] = lista1[i]
            comp_lista2 = len(lista2)
            
            i=i+1
            
        return lista2
    else:
        raise TypeError('junta_ordenadas: Os argumentos devem ser listas')
             
# Exercicio 3:
def ordena (lista):
    if isinstance(lista, list):
        maximo, minimo = lista[0], lista[0]
        posicao = 1
        ordem = [0]*len(lista)
        for i in lista:
            if i > maximo:
                maximo = i
            elif i < minimo:
                minimo = i
        
        comprimento = len(lista)
        for k in range(minimo, maximo + 1):
            for j in range(comprimento):              #tirar o len do for
                if lista[j] == k:
                    ordem[j] = posicao
                    posicao = posicao + 1
                
        
        return ordem
        
    else:
        raise TypeError('ordena: o argumento deve ser uma lista')

# Exercicio 4
def elemento_matriz (matriz, linha, coluna):
    if isinstance (matriz, list) and isinstance (linha, int) and isinstance (coluna, int):
        nr_colunas = len (matriz[0])
        if linha < 0 or linha >= len (matriz):
            print ('indice ivalido: linha', linha)
            
        elif coluna < 0 or coluna >= nr_colunas:
            print ('indice invalido: coluna', coluna)
                
        else:
            for line in matriz:        
                if isinstance (line, list):
                    if len(line) != nr_colunas:
                        print ('Matriz invalida: linha', line, 'tem comprimento diferente de', nr_colunas)
                else:
                    raise TypeError ('elemento_matriz:', 'O primeiro argumento deve ser uma lista de listas')
                
            return matriz[linha][coluna]
    
    else:
        raise TypeError ('elemento_matriz:', 'O primeiro argumento deve ser uma lista de listas e o segundo e terceiro argumentos devem der inteiros')
    

# Exercicio 5:
def matriz(matriz):
    if isinstance (matriz, list):
        for line in matriz:
            if isinstance (line, list):
                for el in line:
                    if isinstance (el, int) or isinstance (el, float):
                        print (' ', el, end='  ')
                        
                    else:
                        raise TypeError ('matriz:', 'Os elementos da matriz nao sao todos numeros reais')
                
                print ('')
            
            else:
                raise TypeError ( 'matriz:', 'O argumento nao e uma lista de listas')
        
    else:
        raise TypeError ( 'matriz:', 'O argumento nao e uma lista')
    

# Exercicio 6:
def soma_matrizes (m1, m2):
    if isinstance (m1, list) and isinstance (m2, list):
        if len (m1) == len (m2):
            
            soma = []
            for linha in range (len (m1)):
                if isinstance (m1[linha], list) and isinstance(m2[linha], list):
                    if len (m1[linha]) == len(m2[linha]):
                        
                        linha_soma = []
                        for el in range (len (m1[linha])):
                            if (isinstance (m1[linha][el], int) or isinstance (m1[linha][el], float)) and (isinstance (m2[linha][el], int) or isinstance (m2[linha][el], float)):
                                linha_soma = linha_soma + [ m1[linha][el] + m2[linha][el] ]
                                
                            else:
                                raise TypeError ('soma_matrizes', 'Os elementos das matrizes nao sao numeros reais ou inteiros')
                        
                        soma = soma + [linha_soma]
                    else:
                        raise ValueError ('soma_matrizes', 'As linhas das matrizes nao têm todas o mesmo comprimento')
                    
                else:
                    raise TypeError ('soma_matrizes', 'Os argumentos nao sao listas de listas')
                
            matriz (m1)
            print ('\n   +\n')
            matriz (m2)
            print ('\n   =\n')
            matriz(soma)
            return soma
            
        else:
            raise ValueError ('soma_matrizes', 'As matrizes nao têm o mesmo numero de linhas')
    
    else:
        raise TypeError ('soma_matrizes', 'Os argumentos nao sao listas')
    

# Exercicio 7:
def produto_matrizes (m1, m2):
    produto = []
    
    for row in range(len(m1)):
        linha_produto = []
        prod = 0
        for el in range(len(m1[0])):
            prod = prod + m2[el][row] * m1[row][el]
            print (prod)
            linha_produto = linha_produto + [prod]
        produto = produto + [linha_produto]
    
    matriz(m1)
    print ('\n')
    matriz(m2)
    print ('\n')
    matriz(produto)
    print ( '\n')
    return produto

# Exercicio 8:

def inverte (lst):
    if isinstance (lst, list):
        for i in range (len (lst) // 2):
            lst[i], lst [-i-1] = lst[-i-1], lst[i]
    else:
        raise ValueError ('inverte:', 'o argumento deve ser uma lista')
    
    return lst

# Exercicio 9:

def duplica_elementos (lst):
    i = 0
    while i < len(lst):
        lst = lst + [0]
        for j in range(len(lst)-1, i, -1):
            lst[j] = lst[j-1]
        lst[i+1] = lst[i]
        i = i + 2
        
    return lst
    
        