n = eval(input('\nQuantos são os alunos?  '))
print('Indique agora as notas de cada um dos alunos')
aluno = 1
positivas = 0

while (aluno <= n):
    nota=eval(input('?   '))
    if(nota >= 10):
        positivas = positivas + 1
    aluno = aluno + 1
    
print (positivas, 'alunos tiveram nota positiva, o que correspode a', (100*positivas/n), '%')