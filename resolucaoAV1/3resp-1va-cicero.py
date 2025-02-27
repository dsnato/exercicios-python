# Inicialização da lista para armazenar as idades
idades = []

# Solicita as 20 idades ao usuário
print("Digite 20 idades:")
for i in range(20):
    idade = int(input(f"Digite a {i+1}ª idade: "))
    idades.append(idade)

# Inicializa as variáveis maior e menor idade
maior_idade, menor_idade = idades[0], idades[0]

# Loop para encontrar a maior e menor idade
for idade in idades:
    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade

# Exibe os resultados
print(f"\nA maior idade do grupo é: {maior_idade}; {menor_idade}")
print(f"A menor idade do grupo é: {menor_idade}")
