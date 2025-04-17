def encontrar_peca_faltando():
    # Lê o número total de peças
    N = int(input("Digite o número total de peças (N): "))

    # Lê os N - 1 números fornecidos, separados por espaço
    pecas_presentes = list(map(int, input(f"Digite os {N - 1} números presentes separados por espaço: ").split()))

    # Verifica se a quantidade de peças fornecida está correta
    if len(pecas_presentes) != N - 1:
        print(f"Erro: você deve digitar exatamente {N - 1} números.")
        return

    # Soma total esperada de 1 a N
    soma_total = N * (N + 1) // 2

    # Soma real dos números presentes
    soma_parcial = sum(pecas_presentes)

    # A diferença é o número que está faltando
    peca_faltando = soma_total - soma_parcial

    # Exibe o resultado
    print(f"A peça que está faltando é: {peca_faltando}")


# Executa a função
if __name__ == "__main__":
    encontrar_peca_faltando()
