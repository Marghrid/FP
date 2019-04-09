# Exercício 1
def explode (inteiro):
    if isinstance(inteiro, int):
        if inteiro>=0:
            divisor=1
            explodido = ()
            while divisor*10 <= inteiro:
                divisor = divisor * 10
            while divisor >= 1:
                explodido = explodido + (inteiro//divisor,)
                inteiro = inteiro%divisor
                divisor = divisor // 10
        else:
            raise ValueError('explode: O argumento é negativo')
    else:
        raise TypeError('explode: O argumento nao é um número inteiro')
    
    return explodido
        
# Exercício 2
def implode (t):
    if isinstance (t, tuple):
        implodido, lenght = 0, len(t)
        for i in range (lenght):
            if not isinstance (t[i], int):
                raise ValueError ("implode: Todos os elementos do tuplo devem ser inteiros")
            else:
                implodido = implodido + t[i]*10**(lenght-i-1)        
    else:
        raise TypeError('implode: O argumento nao é um tuplo')
    return implodido

# Algum erro manhoso entre os exercícios 2 e 3:
def num_para_seq_cod (inteiro):
    if isinstance(inteiro, int):
        if inteiro%1 == 0 and inteiro >= 0:
            divisor=1
            codificado = ()
            while divisor*10 <= inteiro:
                divisor = divisor * 10
            while divisor >= 1:
                if (inteiro//divisor) % 2 == 0:
                    codificado = codificado + (((inteiro//divisor) + 2) % 10,)
                else:
                    codificado = codificado + (((inteiro//divisor) + 8) %10,)
                        
                inteiro = inteiro%divisor
                divisor = divisor // 10
        else:
            raise ValueError('num_para_seq_cod: Inteiro nao positivo')
    else:
        raise TypeError('num_para_seq_cod: Argumento nao é um número inteiro')
    
    return codificado    
    

# Exercício 3
def filtra_pares (t):
    if isinstance(t, tuple):
        res = ()
        for i in range (len(t)):
            if isinstance (t[i], int):
                if t[i]%2 == 0:
                    res = res + (t[i],)
            else:                
                raise ValueError ("filtra_pares", "conteúdo do tuplo nao inteiro")
    else:
        raise TypeError ("filtra_pares:", "argumento nao é um tuplo")
    return res

# Exercício 4
def cc_para_int(frase):
    if isinstance (frase, str):
        final = 0
        for i in range(len(frase)):
            ordem_i = ord(frase[-i-1])
            final = final + ordem_i * 1000 ** i
        if ordem_i<100:
            print("0", end='')
            if ordem_i<10:
                print("0", end='')
    else:
        raise TypeError('cc_para_int', 'o argumento nao é uma string')
    
    return final

# Exercício 5:
def reconhece5(palavra):
    if isinstance(palavra, str):
        tamanho = len(palavra)
        for i in range(tamanho):
            if 'A'<palavra[i]<'D':
                
                if i>0 and palavra[i-1]<'5':
                    return False
                elif i == tamanho-1:
                    return False
            elif '0'<ord(palavra[i])<'5':
                if i==0:
                    return False
            else:
                return False
        return True
    else:
        raise TypeError('reconhece:', 'o argumento nao é uma string')

# Exercício 6
def reconhece6 (frase):
    """ A funcao recebe um tuplo, e retorna True se esse tuplo for uma frase da gramatica fornecida no enunciado. Se nao for, a funcao retorna False """
    if isinstance (frase, str):
        comprimento = len(frase)
        tem_c, nr_a1, nr_a2, nr_b1, nr_b2 = 0, 0, 0, 0, 0
        if ord(frase[0]) != 97 or ord(frase[comprimento-1]) != 97:
            print('tem um elemento que nao é "a", "b", nem "c"')
            return False
        #else:
        for i in range (1,comprimento-1):
            if ord(frase[i]) == 99:
                tem_c=1            
            if i < comprimento/2:
                if ord(frase[i]) == 97:
                    nr_a1=nr_a1+1
                elif ord(frase[i]) == 98:
                    nr_b1=nr_b1+1
            else:
                if ord(frase[i]) == 97: 
                    nr_a2=nr_a2+1
                elif ord(frase[i]) == 98:
                    nr_b2=nr_b2+1                
            if ord(frase[i])<97 or ord(frase[i])>99:
                return False
            elif ord(frase[i]) == 97 and (ord(frase[i+1]) == 99 or ord(frase[i-1]) == 99):
                print ('tem um "a" seguido ou antecedido de um "c"')
                return False
        if nr_a1 == 0 or nr_a2 == 0 or nr_b1 == 0 or nr_b2==0 or tem_c == 0 or nr_a1 != nr_a2 or nr_b1 != nr_b2:
            return False
            
        return True
    else:
        raise TypeError ('reconhece:', 'O argumento nao é um tuplo')

# Exercício 7:
def combinacoes(C1, C2):
    if isinstance (C1, str) and isinstance(C2, str):
        if len(C1) == 1 and len (C2) == 1:
            combinacoes_todas = ()
            combinacao = ()
            i=8
            while i < 16:
                binario = str(bin(i))
                print (binario)
                if binario[-1] == '0':
                    combinacao = combinacao + (C1,)
                elif binario[-1] == '1':
                    combinacao = combinacao + (C2,)
                    
                if binario[-2] == '0':
                    combinacao = combinacao + (C1,)
                elif binario[-2] == '1':
                    combinacao = combinacao + (C2,)            
                
                if binario[-3] == '0':
                    combinacao = combinacao + (C1,)
                elif binario[-3] == '1':
                    combinacao = combinacao + (C2,)
                
                combinacoes_todas = combinacoes_todas + (combinacao,)
                i = i+1
                combinacao = ()
                            
            return combinacoes_todas
        else:
            raise ValueError('combinacoes: uma ou ambas as strings tem mais de um caracter ou sao vazias')
    else:
        raise TypeError('combinacoes: um ou ambos os argumentos nao sao strings')
    

# Exercício 8:
def seq_racaman (numero_de_termos):
    resultado = (0,)
    
    for i in range(1, numero_de_termos):
        temp = resultado[i-1]-i
        if temp >0 and temp not in resultado:
            resultado=resultado + (temp,)
        else:
            resultado = resultado + (temp + 2*i,)
    
    return resultado



# Exercício 9:
def int_para_cc (codificado):
    if isinstance(codificado, int) and codificado >= 0:
        codificado2 = str(codificado)
        descodificado=''
        if len(codificado2)%3 != 0:
            codificado2 = '0'*(3 - len(codificado2)%3) + codificado2
            print (codificado2)
        for i in range(len(codificado2) // 3):
            caracter_i = chr(int(codificado2[-1-3*i]) + int(codificado2[-2-3*i])*10 + int(codificado2[-3-3*i])*100)
            descodificado = descodificado + caracter_i
        
        return caracter_i
    
    else:
        raise TypeError('int_para_cc: O argumento deve ser um inteiro positivo')