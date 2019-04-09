n = eval(input('\nEscreva um inteiro\n? '))
soma,pos = 0,1

while n != 0:
    digito = n % 10
    if digito % 2 == 0:
        soma = soma + digito
    n = n//10
print ('Soma de todos os digitos pares neste inteiro e:', soma)