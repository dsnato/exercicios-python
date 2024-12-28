palavras = ('Corínthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético',
        'Botafogo', 'Atlético-PR','Bahia', 'São Paulo', 'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avaí',
        'Ponte Preta', 'Atlético-GO')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as seguintes vogais: ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l, end=' ')