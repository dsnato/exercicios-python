'''from time import sleep
i = int(input('Digite um número para o início do laço: '))
f = int(input('Digite um número para o fim do laço: '))
p = int(input('Digite um número para o passo do laço: '))
for c in range(i, f+1, p):
    print(c)
    sleep(1)
print('Fim!')'''

'''for c in range(1,20+1):
    n = str(input(f'Digite o nome do {c}º convidado: '))
print('Todos serão convidados imediatamente!')'''

'''lista = []
soma = 0
for c in range(1, 3+1):
    n = int(input(f'Digite o {c}º número que quer somar: '))
    lista.append(n)
    soma += n
print(f'A soma dos números: {lista} é igual a: {soma}!')'''

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BUM! BUM! POOW!')