from math import sqrt
print('\n\nEste programa destina-se a calcular a média e o desvio padrão\nde 5 números reais (x1 a x5), indicados pelo utiliador')
x1=eval(input('x1= '))
x2=eval(input('x2= '))
x3=eval(input('x3= '))
x4=eval(input('x4= '))
x5=eval(input('x5= '))

media = (x1+x2+x3+x4+x5) / 5
desvio_padrao = sqrt( 0.25 * ((x1-media) + (x2-media) + (x3-media) + (x4-media) + (x5-media)) ** 2)

print('a media dos 5 valores e', media, 'e o desvio padrão é ', desvio_padrao)