a=eval(input('\n\n\nEste programa tem o intuito de lhe indicar o maior de 3 n�meros. Indique:\n  a = '))
b=eval(input('  b = '))
c=eval(input('  c = '))

if (a>b):
    if (a>c):
        print ('a � o maior dos 3 n�meros')
    elif (a<c):
        print ('c � o maior dos 3 n�meros')
    else:
        print ('a � igual a c, e s�o maiores que b')

elif (b>a):
    if (b>c):
        print ('b � o maior dos 3 n�meros')
    elif (b<c):
        print ('c � o maior dos 3 n�meros')
    else:
        print ('b � igual a c, e s�o maiores que a')

else:
    if(a>c):
        print ('a � igual a b, e s�o maiores do que c')
    elif(a<c):
        print ('c � o maior dos 3 n�meros')
    else:
        print ('os n�meros s�o todos iguais, you sneaky bastard')