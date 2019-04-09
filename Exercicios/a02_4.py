passageiros=eval(input('\n\nPassageiros transportados: '))
passmilhgal=eval(input('Qual o consumo do avião em passageiros - milha / galão: '))

# x passageiros - milha / galão => x passageiros podem ser transportados uma milha, usando 1 galão de combustível

final=passageiros/passmilhgal
print ('Consumo em galões / milha: ', final)