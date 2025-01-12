'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(1, 2, 3)
r2 = somar(4, 9)
r3 = somar(2)

print(f'Os valores somados foram: {r1}, {r2} e {r3}.')'''

'''def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

#Programa principal
f1 = fatorial(5)
f2 = fatorial(4)

print(f'Os fatoriais recebidos foram de {f1} e {f2}.')'''

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


#Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
