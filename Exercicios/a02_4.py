passageiros=eval(input('\n\nPassageiros transportados: '))
passmilhgal=eval(input('Qual o consumo do avi�o em passageiros - milha / gal�o: '))

# x passageiros - milha / gal�o => x passageiros podem ser transportados uma milha, usando 1 gal�o de combust�vel

final=passageiros/passmilhgal
print ('Consumo em gal�es / milha: ', final)