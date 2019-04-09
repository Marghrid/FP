tempo=eval(input("\n\nEscreva o numero de segundos: "))
dias= tempo//(86400)
horas = (tempo%86400) // 3600
minutos = ((tempo%86400)%3600) // 60
segundos = ((tempo%86400)%3600)%60

print('  dias:', dias, '     horas: ', horas)
print('  minutos:', minutos,   '   segundos',segundos)