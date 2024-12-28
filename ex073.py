times = ('Corínthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético',
        'Botafogo', 'Atlético-PR','Bahia', 'São Paulo', 'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avaí',
        'Ponte Preta', 'Atlético-GO')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'05 primeiros times são: {times[0:5]}')
print('-=' * 15)
print(f'04 últimos times são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição')
print('-=' * 15)
