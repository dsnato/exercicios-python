# Inicializando a agenda como um dicionário vazio
agenda = {}

# Loop para inserir dados até o usuário decidir parar
while True:
    # Leitura dos dados
    cpf = input("Digite o CPF (ou 'sair' para encerrar): ")

    if cpf.lower() == 'sair':  # Condição para encerrar o loop
        break

    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    telefone = input("Digite o telefone: ")

    # Inserindo os dados no dicionário
    agenda[cpf] = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }

# Imprimindo a agenda no formato especificado
print("\nAgenda completa:")
for cpf, dados in agenda.items():
    print(f"{cpf}: {dados['nome']}-{dados['idade']}-{dados['telefone']}")
