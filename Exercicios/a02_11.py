segundos=1
print ('\n')

while (segundos>=0):
    segundos=eval(input('Escreva um n�mero de segundos\n(um n�mero negativo para terminar)\n? '))
    if (segundos >= 0):
        dias = segundos / 86400
        print ('O numero de dias correspondente �', dias)