x=eval(input('\nQual o valor de x\n? '))
n=eval(input('Qual o valor de n\n? '))

i=1
termo_i=1
soma=1

while (i <= n):
    termo_i = termo_i * x / i
    soma = soma + termo_i
    i=i+1

print('O valor da soma é', soma)