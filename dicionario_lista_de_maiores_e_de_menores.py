# Dicionário principal para armazenar todas as pessoas
pessoas = {}

# Loop para cadastro de pessoas
while True:
    cpf = input("Digite o CPF (ou 'sair' para encerrar): ")
    if cpf.lower() == 'sair':
        break

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))  # Convertendo a idade para inteiro

    # Adicionando a pessoa ao dicionário
    pessoas[cpf] = {
        "nome": nome,
        "idade": idade
    }

# Separando as pessoas em dois dicionários
maiores_de_idade = {}
menores_de_idade = {}

for cpf, dados in pessoas.items():
    if dados["idade"] >= 18:
        maiores_de_idade[cpf] = dados
    else:
        menores_de_idade[cpf] = dados

# Exibindo o resultado
print("\nPessoas maiores de 18 anos:")
for cpf, dados in maiores_de_idade.items():
    print(f"{cpf}: {dados['nome']} - {dados['idade']} anos")

print("\nPessoas menores de 18 anos:")
for cpf, dados in menores_de_idade.items():
    print(f"{cpf}: {dados['nome']} - {dados['idade']} anos")
