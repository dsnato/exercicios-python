# Recebe o nome completo do usuário
nome_completo = input("Digite seu nome completo: ")

# Divide o nome completo em partes (palavras)
nomes = nome_completo.split()

# O último nome será o último item da lista
ultimo_nome = nomes[-1]

# O primeiro nome será o primeiro item da lista
primeiro_nome = nomes[0]

# Exibe o resultado no formato desejado
print(f"{ultimo_nome}, {primeiro_nome}")
