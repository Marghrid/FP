horas = eval(input('\n\nQuantas horas trabalhou o empregado?'))
sal�rio = eval(input('Qual o seu sal�rio/hora?'))

if (horas<=40):
    ordenado=horas*sal�rio
else:
    ordenado=(40 + 2*(horas-40))*sal�rio

print('O ordenado semanal do empregado deve ser de', ordenado)