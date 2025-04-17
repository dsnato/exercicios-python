'''
Tarefa: Crie uma função recursiva que execute a operação de potencialização.
Entrada: 2 3
Saída: 8
'''

def potencia(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * potencia(base, exp-1)

print(potencia(2, 3))
