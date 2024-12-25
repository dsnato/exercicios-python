lista = []
soma = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º número inteiro: '))
    if n % 2 == 0:
        soma += n
        lista.append(n)
print(f'A soma dos {len(lista)} números pares colocados foi: {soma}')
print(f'Os números colocados foram: {lista}')
