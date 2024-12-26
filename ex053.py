frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é: {inverso}, logo')
if inverso == junto:
    print('a frase é um PALÍNDROMO!')
else:
    print('a frase NÃO é um PALÍNDROMO!')
