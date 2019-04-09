distancia=eval(input('\n\nQual a distancia percorrida? (Em Km) '))
tempo=eval(input('Em quanto tempo? (Em minutos)'))

velocidade1=distancia/(tempo/60)
velocidade2=(distancia*1000)/(tempo*60)

print('A velocidade media em Km/h foi', velocidade1)
print('Em m/s:', velocidade2)