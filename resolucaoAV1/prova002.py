#crie uma lista armazenar 20 idades (solicite ao usuário)

lista = []
maior = 0
menor = float('inf')

for i in range(20):
    idade = int(input(f'Digite a idade do usuário {i+1}: '))
    lista.append(idade)
    if idade < menor:
        menor - idade
    if idade > maior:
        maior = idade

print('Maior idade: ', maior)
print('Menor idade: ', menor)
