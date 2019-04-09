#  ----------- PROJETO 1 -----------
#   Margarida Ferreira - 80832
#   Miguel Marques - 24835
  

def pos_maximo (conjunto, comprimento):
# Funcao que recebe como argumentos uma lista ou tuplo, e o seu comprimento e
# devolve a posicao do seu maior elemento
    
    maximo, pos_maximo = -1, -1
    empate = False
    for i in range(comprimento):
        if conjunto[i] > maximo:
            pos_maximo = i
            maximo = conjunto[i]
            
    for j in range(comprimento):
        if conjunto[j] == maximo and j != pos_maximo:
            empate = True
        
    return (pos_maximo, empate)

def encontra_empatado (conjunto, posicao):     
# Funcao que recebe como argumentos uma lista ou tuplo, e a posicao de um dos
# seus elementos, e devolve a posicao em que esse elemento se repete
    for i in range(len(conjunto)):
        if conjunto[posicao] == conjunto[i] and posicao !=i:
            return i

def mandatos (nr_mandatos, nr_votos): 
    """
    Funcao que recebe o numero de mandatos para atribuicao e um tuplo com o numero de
    votos por candidatura num dado circulo eleitoral, e devolve um tuplo com o numero
    de mandatos atribuidos a cada candidatura nesse circulo eleitoral.
    """
    
    votos_por_candid = list(nr_votos)
    comp_nr_votos = len(nr_votos)
    mandatos_por_candid = [0]*comp_nr_votos
    
    for mandatos_atribuidos in range(nr_mandatos):
        candid_com_mais_votos, empate = pos_maximo(votos_por_candid, comp_nr_votos)     # seleciona o candidato com mais votos
        
        if empate:                                                                      # em caso de empate, seleciona o candidato que inicialmente tinha menos votos
            if nr_votos[encontra_empatado(votos_por_candid, candid_com_mais_votos)] < nr_votos[candid_com_mais_votos]:
                candid_com_mais_votos = encontra_empatado(votos_por_candid, candid_com_mais_votos)
          
        mandatos_por_candid[candid_com_mais_votos] = mandatos_por_candid[candid_com_mais_votos] + 1             # atribui um mandato ao candidato com mais votos              
        votos_por_candid[candid_com_mais_votos] = nr_votos[candid_com_mais_votos] / (mandatos_por_candid[candid_com_mais_votos] + 1)     # divide o numero original de votos do candidato com mais votos pelo divisor adequado
    
    return tuple(mandatos_por_candid)


def assembleia (votacoes):
    """
    Funcao que recebe como argumento um tuplo de tuplos com o resultado da votacao em
    cada circulo eleitoral, e devolve um tuplo com o numero total de mandatos
    atribuidos a cada candidatura na Assembleia da Republica.
    """
     
    mandatos_por_circulo_eleitoral= (16,3,19,3,4,9,3,9,4,10,47,2,39,9,18,6,5,9,5,6,2,2)    # de acordo com os dados da tabela 1
    mandatos_por_partido=[0]*15 
    
    for circulo_eleitoral in range(22):            # corre a funcao mandatos para cada um dos circulos eleitorais
        mandatos_do_circulo_eleitoral = mandatos(mandatos_por_circulo_eleitoral[circulo_eleitoral], votacoes[circulo_eleitoral])          
        for partido in range(15):              # soma ao numero de mandatos totais o numero de mandatos do circulo eleitoral
            mandatos_por_partido[partido]=mandatos_por_partido[partido] + mandatos_do_circulo_eleitoral[partido] 
        
    return tuple(mandatos_por_partido)


def max_mandatos(votacoes):
    """
    Funcao que recebe um tuplo de tuplos com o resultado da votacao em cada circulo eleitoral 
    e devolve uma string com a designacao da candidatura com mais mandatos atribuidos na Assembleia da Republica.
    """
    
    candidatos=('PDR\tPartido Democratico Republicano',
        'PCP-PEV\tCDU-Coligacao Democratica Unitaria',
        'PPD/PSD-CDS/PP\tPortugal a Frente',
        'MPT\tPartido da Terra',
        'L/TDA\tLIVRE/Tempo de Avancar',
        'PAN\tPessoas-Animais-Natureza',
        'PTP-MAS\tAgir',
        'JPP\tJuntos pelo Povo',
        'PNR\tPartido Nacional Renovador',
        'PPM\tPartido Popular Monarquico',
        'NC\tNos, Cidadaos!',
        'PCTP/MRPP\tPartido Comunista dos Trabalhadores Portugueses',
        'PS\tPartido Socialista',
        'B.E.\tBloco de Esquerda',
        ' PURP\tPartido Unido dos Reformados e Pensionistas')
    
    resultados_eleitorais = assembleia(votacoes)
    candid_com_mais_mandatos, empate = pos_maximo(resultados_eleitorais, 15)                # seleciona o candidato com mais votos
       
    if empate:
        return 'Empate tecnico'
    
    return candidatos[candid_com_mais_mandatos]     
