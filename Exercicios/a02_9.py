ano = eval(input('\n\nEscreva um ano para eu dizer se � bissexto\nAno -> '))
if (ano%4 == 0):
    if (ano%100 != 0):
        print ('O ano', ano, '� bissexto')
    elif (ano%400 == 0):
        print ('O ano', ano, '� bissexto')
else:
    print ('O ano', ano, '� um ano comum')