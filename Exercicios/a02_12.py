print ('\n')
numero=''
digito=''
while (digito!='-1'):
    digito = input('Escreva um dígito\n(-1 para terminar)\n')
    if (digito!='-1'):
        if (eval(digito)<=0):
            print('Não pode colocar dígitos negativos num número inteiro')
        else:
            numero=numero+digito
print ('o numero e:', numero)