n = eval(input('Escreva um inteiro\n? '))
num,pos = 0,1

while n != 0:
    digito = n % 10
    if digito % 2 != 0:
        num = num + digito * pos
        pos = 10 * pos
    n = (n - digito)//10
print ('Resultado:', num)