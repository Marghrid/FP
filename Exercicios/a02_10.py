horas = eval(input('\n\nQuantas horas trabalhou o empregado?'))
salário = eval(input('Qual o seu salário/hora?'))

if (horas<=40):
    ordenado=horas*salário
else:
    ordenado=(40 + 2*(horas-40))*salário

print('O ordenado semanal do empregado deve ser de', ordenado)