n = []
p = []
i = []
while True:
    n.append(int(input('Digite um número: ')))
    r = str(input('Quer conitnuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
for v in n:
    if v % 2 == 0:
        p.append(v)
    elif v % 2 == 1:
        i.append(v)
print('==' * 30)
print(f'A lista completa é: {n}')
print(f'A lista de pares é: {p}')
print(f'A lista de ímpares é: {i}')
