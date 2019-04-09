n = eval(input('Escreva um inteiro positivo\n? '))
digitos, potencias_de_10 = 1, 0.1
num, pos = 0, 1

while n % potencias_de_10 != n:
    potencias_de_10 = potencias_de_10 * 10
    if n % potencias_de_10 == n:
        digitos = log10(potencias_de_10)

while n != 0:
    digito = n % 10
    num = num + digito*(pos*digitos-1)
    pos = 10 * pos
    n = (n - digito)//10    
    
while n != 0:
    digito = n % 10
    if digito % 2 != 0:
        num = num + digito * pos
        pos = 10 * pos
        n = (n - digito)//10
        
print ('Resultado:', num)