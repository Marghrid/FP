print ('\n')
numero=''
digito=''
while (digito!='-1'):
    digito = input('Escreva um d�gito\n(-1 para terminar)\n')
    if (digito!='-1'):
        if (eval(digito)<=0):
            print('N�o pode colocar d�gitos negativos num n�mero inteiro')
        else:
            numero=numero+digito
print ('o numero e:', numero)