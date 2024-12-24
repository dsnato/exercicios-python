from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print(f'Você nasceu em {nasc} e tem {idade} anos.')
if idade == 18:
    print('Tá na hora de se alistar!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda não chegou sua vez de se alistar. Falta {saldo} anos para isso!')
    ano = atual + saldo
    print(f'O ano do seu alistamento será em {ano}')
else:
    saldo = idade - 18
    print(f'Já se alistou? Se não, tá atrasado {saldo} anos. Cuida!')
    ano = atual - saldo
    print(f'O ano do seu alistamento foi em {ano}')
