
n=eval(input('\n\n\nEste programa destina-se a factorizar em primos um número,\
  \nn, maior que 1, indicado pelo utilizador.\n\nIndique o valor de n: '))

divisor,vezes = 2,0

while n!=1:
  expoente=0
  while n%divisor == 0:
    expoente=expoente+1
    n=n//divisor
  if(expoente == 1):
    if(vezes==1):
      print('*', end=' ')
    print(divisor, end=' ')
    vezes=1
  elif(expoente != 0):
    if(vezes==1):
         print('*', end=' ')    
    print(divisor,'^',expoente, end=' ', sep='')
    vezes=1
  divisor=divisor+1
  #else print('divisor=divisor máximo') 