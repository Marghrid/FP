ano = eval(input('\n\nEscreva um ano para eu dizer se é bissexto\nAno -> '))
if (ano%4 == 0):
    if (ano%100 != 0):
        print ('O ano', ano, 'é bissexto')
    elif (ano%400 == 0):
        print ('O ano', ano, 'é bissexto')
else:
    print ('O ano', ano, 'é um ano comum')