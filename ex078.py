'''lista = [1, 6, 2, 9]
lista[0] = 3
lista.append(10)
lista.sort(reverse=True)
lista.insert(0, 11)
if 8 in lista:
    lista.remove(8)
else:
    print('Não achei o número 8')
print(lista)
print(f'Essa lista tem {len(lista)} números')'''

'''valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')
print(valores)'''

listanum = []
maior = menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para {c+1}ª posição: ')))
    if c == 0:
        maior = menor = listanum[0]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor foi: {maior} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor foi: {menor} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
print()