#  ----------- PROJETO 2 -----------
#   Margarida Ferreira - 80832
#   Miguel Marques - 24835
  
#Operacoes TAD coordenada:
# Construtor:
def cria_coordenada (l,c):
    """
    Construtor do tipo coordenada. Recebe dois argumentos inteiros positivos,
    o primeiro dos quais corresponde a uma linha l e o segundo a uma coluna c,
    e devolve um elemento do tipo coordenada correspondente à célula (l : c).
    """
    if isinstance(l,int) and isinstance(c,int) and l>0 and c>0:
        return (l,c)
    else:
        raise ValueError('cria_coordenada: argumentos invalidos')

# Seletores:
def coordenada_linha(c):
    """
    Recebe uma coordenada e devolve a linha respetiva.
    """
    return c[0]

def coordenada_coluna(c):
    """
    Recebe uma coordenada e devolve a coluna respetiva.
    """
    return c[1]

# Reconhecedor:
def e_coordenada(arg):
    """
    Recebe um argumento e devolve True caso esse argumento seja do tipo
    coordenada, e False em caso contrário.
    """
    return isinstance (arg, tuple) and len(arg) == 2 and isinstance (arg[0], int)\
        and arg[0] > 0 and isinstance (arg[1], int) and arg[1] > 0
    
# Teste:
def coordenadas_iguais(c1,c2):
    """
    Recebe duas coordenadas e devolve True caso esses estas correspondam à mesma
    célula do tabuleiro, e False caso contrário.
    """
    return c1[0] == c2[0] and c1[1] == c2[1]

# Representacao externa:
def coordenada_para_cadeia(c):
    """
    Recebe uma coordenada e devolve uma cadeia de caracteres que a represente.
    """
    return '(' + str(coordenada_linha(c)) + ' : ' + str(coordenada_coluna(c)) + ')'

#TAD tabuleiro:

#Funcoes auxiliares:
def tuplo_de_tuplos_de_inteiros_positivos(t):
    """
    Tem valor verdadeiro se o seu argumento e um tuplo constituido apenas por
    outros tuplos, que por sua vez sao constituidos apenas por inteiros
    positivos, e valor falso caso contrario
    """
    if t != ():
        for i in t:
            if not tuplo_de_inteiros_positivos(i):
                return False
        return True
    return False

def tuplo_de_inteiros_positivos(i):
    """Tem valor verdadeiro se o seu argumento e um tuplo constituido apenas por
    inteiros positivos, e valor falso caso contrario"""
    if i != ():
        for n in i:
            if not isinstance (n,int) or n <= 0:
                return False
        return True
    return False

def cria_celulas(l,c):
    """Cria uma lista com l listas, cada uma das quais constituida por c 0s.
    Correspondera aos valores iniciais das celulas de um novo tabuleiro"""
    celulas = []
    for i in range(l):                          # Nao pode escrever-se [[0]*c]*l porque se obteria
        celulas_aux = []                        # uma lista com l vezes a mesma lista. Assim, quando    
        for j in range(c):                      # fosse alterada uma das l listas, se-lo-iam todas
            celulas_aux = celulas_aux + [0]     # (visto que sao a mesma lista)
        celulas = celulas + [celulas_aux]
    return celulas

#Operacoes TAD tabuleiro:
#Construtor:
def cria_tabuleiro(t):
    def teste_especificacoes (t):
        """Testa que as especificacoes fornecidas sao validas em termos de
        numero de linhas e colunas que abrangem"""
        if isinstance(t, tuple) and len(t)==2\
            and tuplo_de_tuplos_de_inteiros_positivos(t[0])\
            and tuplo_de_tuplos_de_inteiros_positivos(t[1]):
            num_linhas = len (t[0])
            num_colunas = len (t[1])
            soma_els = 0
            for i in t[0]:
                num_els = len (i)                   # O numero de celulas que devem ser preenchidas
                for j in i:                         # em cada linha, somado ao numero minimo de
                    soma_els = soma_els + j         # espacos em branco que devem existir entre
                soma_els = soma_els + num_els - 1   # elas (igual a len(especificacao) - 1), nao
                if soma_els > num_colunas:          # deve ser superior ao numero de colunas
                    return False                    # existentes no tabuleiro.
                soma_els = 0
                
            for i in t[1]:
                num_els = len(i)                    # Processo analogo para as especificacoes
                for j in i:                         # referentes as colunas - a soma nao deve ser
                    soma_els = soma_els + j         # superior ao numero de linhas existentes
                soma_els = soma_els + num_els - 1   # no tabuleiro.
                if soma_els > num_colunas:
                    return False
                soma_els = 0
            return True
        return False    
    if teste_especificacoes (t):
        # O numero linhas / colunas do tabuleiro vai ser igual
        # ao numero de especificacoes das linhas / colunas.
        celulas = cria_celulas (len(t[0]),len(t[1]))                           
        return {'esp_linhas': t[0],'esp_colunas': t[1], 'celulas':celulas}     
    else:
        raise ValueError('cria_tabuleiro: argumentos invalidos')

#Seletores:  
def tabuleiro_dimensoes(t):
    """
    Recebe um tabuleiro t e devolve um tuplo com dois elementos, cujo primeiro
    é o número de linhas do tabuleiro e o segundo o número de colunas do mesmo.
    """
    return (len(t['esp_linhas']), len(t['esp_colunas']))

def tabuleiro_especificacoes(t):
    """
    Recebe um tabuleiro t e devolve um tuplo composto por dois tuplos de tuplos
    de inteiros, cujo primeiro elemento corresponde à especificação das linhas e
    o segundo à especificação das colunas.
    """
    return (t['esp_linhas'], t['esp_colunas'])    

def tabuleiro_celula (t, c):
    """
    Recebe um tabuleiro t e uma coordenada c e devolve um inteiro entre 0 e 2,
    que corresponde ao valor contido na célula do tabuleiro referente à
    coordenada c: Caso a célula correspondente a c esteja vazia, devolve o
    valor 0, caso corresponda a uma célula em branco devolve o valor 1 e caso
    esteja preenchida devolve o valor 2.
    """
    if e_coordenada(c) and e_tabuleiro(t)\
        and coordenada_linha(c) <= tabuleiro_dimensoes(t) [0]\
        and coordenada_coluna(c) <= tabuleiro_dimensoes(t) [1]:

        linha = coordenada_linha (c) - 1
        coluna = coordenada_coluna (c) - 1
        return t['celulas'][linha][coluna]
    raise ValueError ('tabuleiro_celula: argumentos invalidos')

#Modificador:
def tabuleiro_preenche_celula(t, c, e):
    """
    Recebe um tabuleiro t, uma coordenada c e um inteiro e entre 0 e 2, e
    modifica o tabuleiro t, preenchendo a célula referente à coordenada c com o
    elemento e, que pode ser 0, 1 ou 2, para representar o vazio, uma célula em
    branco ou uma caixa, respetivamente. Devolve o tabuleiro modificado.
    """
    if e_tabuleiro (t) and e_coordenada (c) and e in (0,1,2)\
        and coordenada_linha(c) <= tabuleiro_dimensoes(t) [0]\
        and coordenada_coluna(c) <= tabuleiro_dimensoes(t) [1]:

        linha = coordenada_linha (c) - 1
        coluna = coordenada_coluna (c) - 1        
        t['celulas'][linha][coluna] = e
        return t
    raise ValueError ('tabuleiro_preenche_celula: argumentos invalidos')

#Reconhecedor:
def e_tabuleiro(arg):
    """
    Recebe um argumento e devolve True se for do tipo tabuleiro e False caso contrário.
    """
    if isinstance (arg, dict) and len (arg) == 3 and 'esp_linhas' in arg\
        and 'esp_colunas' in arg and 'celulas' in arg\
        and isinstance (arg['esp_linhas'], tuple)\
        and isinstance (arg['esp_colunas'], tuple)\
        and isinstance (arg['celulas'], list)\
        and arg['celulas'] != []\
        and len(arg['esp_linhas']) == len(arg['celulas']):

        num_colunas = len(arg['celulas'][0])
        for linha in arg['celulas']:
            if len(linha) != num_colunas:
                return False
        if num_colunas != len(arg['esp_colunas']):
            return False
        return True
    return False

#Testes:
def tabuleiro_preenchido(t):
    """Recebe um tabuleiro e retorna Verdadeiro caso o tabuleiro esteja
    totalmente preenchido, e Falso caso contrario"""
    for linha in range (tabuleiro_dimensoes(t)[0]):
        for coluna in range(tabuleiro_dimensoes(t)[1]):
            el = tabuleiro_celula(t, cria_coordenada(linha + 1, coluna + 1))
            if el == 0:
                return False
    return True

def tabuleiro_completo (t):
    """
    Recebe um tabuleiro t e devolve True caso t esteja totalmente preenchido
    corretamente de acordo com as suas especificações, e False em caso contrário.
    """

    def verificacao_esp (lista_de_listas, tuplo_de_especificacoes): 
        """Funcao auxiliar de tabuleiro_completo que vefica que as celulas
        preenchidas numa dada linha / coluna obedecem as especificacoes atribuidas
        a essa linha / coluna"""
        for j in range(len(lista_de_listas)):
            cels_pintadas = 0
            esp_atual = 0
            for i in range(len(lista_de_listas[j])):
                if lista_de_listas[j][i] == 2:
                    cels_pintadas = cels_pintadas + 1
                if (lista_de_listas[j][i] == 1 or\
                    i == len(lista_de_listas[j])-1) and cels_pintadas != 0:

                    if cels_pintadas != tuplo_de_especificacoes[j][esp_atual]:
                        return False       
                    esp_atual = esp_atual + 1
                    cels_pintadas = 0
        return True
    
    if tabuleiro_preenchido(t):
        lst_colunas = []                            # Cria uma lista de listas com os valores
        for col in range (len(t['celulas'][0])):    # correspondentes as celulas de cada coluna
            lst_col_atual = []                      # do tabuleiro.
            for linha in t['celulas']:
                lst_col_atual = lst_col_atual + [linha[col]]
            lst_colunas = lst_colunas + [lst_col_atual]
    
        return verificacao_esp(t['celulas'], t['esp_linhas']) \
            and verificacao_esp (lst_colunas, t['esp_colunas']) 
    return False

def tabuleiros_iguais(t1,t2):
    """
    Recebe dois tabuleiros t1 e t2 e devolve True caso t1 e t2 correspondam a
    dois tabuleiros com as mesmas especificações e quadros com o mesmo conteúdo,
    e False em caso contrário.
    """
    return t1 == t2

#Representacao externa:
def escreve_tabuleiro(t):
    """ Recebe um tabuleiro t e escreve para o ecrã a sua representação externa. """
    def comprimento_max_tuplo_tuplos(tup):
        """Funcao que recebe um tuplo e devolve o valor do comprimento do
        maior dos tuplos que o contitui"""
        max = 0
        for i in tup:
            if len(i) > max:
                max = len(i)
        return max
  
    comp_max_esp_colunas = comprimento_max_tuplo_tuplos(tabuleiro_especificacoes(t)[1]) 
    for comp_atual in range(comp_max_esp_colunas,0,-1):
        imp_linha = ''
        for coluna in tabuleiro_especificacoes(t)[1]:
            diferenca = len(coluna) - comp_atual
            if diferenca < 0:
                imp_linha = imp_linha + '     '                 
            else:
                imp_linha = imp_linha + '  ' + str(coluna[diferenca]) + '  '
        print(imp_linha + '  ')     
    
    comp_max_esp_linhas = comprimento_max_tuplo_tuplos(tabuleiro_especificacoes(t)[0])
    for linha in range(tabuleiro_dimensoes(t)[0]):
        imp_linha = ''
        for coluna in range(tabuleiro_dimensoes(t)[1]):
            el = tabuleiro_celula(t, cria_coordenada(linha + 1, coluna + 1))
            if el == 0:
                el = '?'
            elif el == 1:
                el = '.'
            else:
                el = 'x'
            imp_linha = imp_linha + '[ ' + el + ' ]'
            
        for el in tabuleiro_especificacoes(t)[0][linha]:                
            imp_linha = imp_linha + ' ' + str(el)
            
        diferenca = comp_max_esp_linhas-len(tabuleiro_especificacoes(t)[0][linha])
        
        if diferenca > 0:
            imp_linha = imp_linha + '  '*diferenca
        print(imp_linha + '|')
    print()
    
#TAD jogada
#Construtor:
def cria_jogada(c,i):
    """
    Construtor do tipo jogada. Recebe uma coordenada e um inteiro com valor 1 ou 2.
    """
    if e_coordenada(c) and i in (1,2):
        return (c, i)
    else:
        raise ValueError('cria_jogada: argumentos invalidos')

#Seletores
def jogada_coordenada(J):
    """Recebe uma jogada e devolve a coordenada respetiva."""
    return J[0]

def jogada_valor(J):
    """Recebe uma jogada e devolve o valor respetivo."""
    return J[1]

#Reconhecedor
def e_jogada(arg):
    """
    Recebe um argumento e devolve True caso esse argumento seja do tipo jogada,
    e False em caso contrário.
    """
    return isinstance(arg,tuple) and len(arg) == 2 \
        and e_coordenada(arg[0]) and arg[1] in (1,2)

#Teste:
def jogadas_iguais(J1,J2):
    """Recebe duas jogadas e devolve True caso correspondam à mesma jogada e False caso contrário."""
    return J1 == J2

#Representacao externa:
def jogada_para_cadeia(J):
    """
    Recebe uma jogada e devolve uma cadeia de caracteres que a representa.
    """
    linha = coordenada_linha(jogada_coordenada(J))
    coluna = coordenada_coluna(jogada_coordenada(J))
    return '('+ str(linha) + ' : ' + str(coluna) + ')' + ' --> ' + str(jogada_valor(J))

#Funcoes Adicionais
def le_tabuleiro(ficheiro):
    """
    Recebe uma cadeia de caracteres que corresponde ao nome do ficheiro com os dados
    de especificação do jogo, e devolve um tuplo de dois tuplos com a especificação
    das linhas e colunas, respetivamente. 
    """
    fich = open(ficheiro,'r')
    especificacoes = fich.readline()
    fich.close()
    return eval(especificacoes)

def pede_jogada(t):
    """
    Recebe o tabuleiro do jogo e devolve a jogada que o jogador pretende executar
    ou o valor False caso o utilizador não introduza uma coordenada válida para o
    tabuleiro em causa.
    """
    def cadeia_para_tuplo_de_inteiros(cadeia):
        """Funcao que recebe uma cadeia de caracteres, e devolve o valor da linha e
        coluna nela expressas, caso esta cadeia de caracteres represente corretamente
        uma coordenada, e devolve o valor Falso em caso contrario"""
        numero = ''
        i = 1
        comp = len(cadeia)
        if cadeia[0]=='(':
            while i < comp :
                if ord(cadeia[i]) in range(48 , 58):
                    numero = numero + cadeia[i]
                    i = i+1
                elif cadeia[i:i+3] == ' : ':
                    if numero == '':
                        return False
                    else:
                        linha = int(numero)
                        numero = ''
                        i = i+3
                elif cadeia[i] == ')':
                    if numero == '':
                        return False
                    else:
                        coluna = int(numero)
                        i = i+1
                else:
                    return False
            return linha, coluna
        return False
    
    dim = tabuleiro_dimensoes(t)
    posicao = input('Introduza a jogada\n- coordenada entre (1 : 1) e ('
        + str(dim[0]) + ' : ' + str(dim[1]) + ') >> ')
    valor = eval(input('- valor >> '))
    if cadeia_para_tuplo_de_inteiros(posicao) != False:
        linha,coluna = cadeia_para_tuplo_de_inteiros(posicao)
        if linha > dim[0] or coluna > dim[1]:
            return False
        return cria_jogada(cria_coordenada(linha,coluna), valor)

def jogo_picross(ficheiro):
    """
    Permite jogar um jogo completo de Picross. Recebe como argumento uma cadeia
    de caracteres representando o nome do ficheiro com a especificação do
    tabuleiro, e devolve True caso o tabuleiro resultante do jogo esteja
    completo (quadro completo e de acordo com as especificações) e False caso
    contrário.
    """
    T = cria_tabuleiro(le_tabuleiro(ficheiro))
    print ('JOGO PICROSS')
    escreve_tabuleiro(T)
    while not tabuleiro_preenchido(T):
        J = pede_jogada(T)
        if not J:
            print('Jogada invalida.')
        else:    
            c = jogada_coordenada(J)
            v = jogada_valor(J)
            T = tabuleiro_preenche_celula(T,c,v)
            escreve_tabuleiro(T)
    if tabuleiro_completo (T):
        print('JOGO: Parabens, encontrou a solucao!')
        return True
    print ('JOGO: O tabuleiro nao esta correto!')
    return False
