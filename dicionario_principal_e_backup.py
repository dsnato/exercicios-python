# Dicionários para armazenar os dados
principal = {}
backup = {}

# Loop para inserir dados
while True:
    chave = input("Digite a chave (ou 'sair' para encerrar): ")
    if chave.lower() == 'sair':
        break

    valor = input("Digite o valor: ")

    # Adicionando no dicionário principal e backup
    principal[chave] = valor
    backup[chave] = valor

    # Verificando se o dicionário principal atingiu o tamanho 5
    if len(principal) == 5:
        print("\nDicionário principal atingiu 5 elementos. Dados:")
        for k, v in principal.items():
            print(f"{k}: {v}")

        # Limpando o dicionário principal
        principal.clear()
        print("\nDicionário principal foi esvaziado.\n")

# Exibindo o conteúdo do backup após o programa encerrar
print("\nConteúdo do backup:")
for k, v in backup.items():
    print(f"{k}: {v}")

