"""nome = input('Digite o nome do usuário: ')

nome_composto = nome.split()
sobrenome, primeiro_nome = nome_composto
print(f'{nome_composto[-1]}, {nome_composto[0]}')
"""
nome = input('Digite o nome completo do usuário: ').split()
print(f'{nome[-1]}, {nome[0]}')
