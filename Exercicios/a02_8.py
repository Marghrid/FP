a=eval(input('\n\n\nEste programa tem o intuito de lhe indicar o maior de 3 números. Indique:\n  a = '))
b=eval(input('  b = '))
c=eval(input('  c = '))

if (a>b):
    if (a>c):
        print ('a é o maior dos 3 números')
    elif (a<c):
        print ('c é o maior dos 3 números')
    else:
        print ('a é igual a c, e são maiores que b')

elif (b>a):
    if (b>c):
        print ('b é o maior dos 3 números')
    elif (b<c):
        print ('c é o maior dos 3 números')
    else:
        print ('b é igual a c, e são maiores que a')

else:
    if(a>c):
        print ('a é igual a b, e são maiores do que c')
    elif(a<c):
        print ('c é o maior dos 3 números')
    else:
        print ('os números são todos iguais, you sneaky bastard')