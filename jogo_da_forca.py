def exibir_palavra_secreta(palavra, letras_corretas):
    return ''.join([letra if letra in letras_corretas else '_' for letra in palavra])


def jogar_forca():
    palavra_secreta = "python"
    letras_corretas = set()
    letras_erradas = set()
    tentativas = 6

    print("\n🎮 Bem-vindo ao Jogo da Forca! 🎮")

    while tentativas > 0:
        print("\nPalavra: ", exibir_palavra_secreta(palavra_secreta, letras_corretas))
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {', '.join(letras_erradas)}" if letras_erradas else "Nenhuma letra errada ainda.")

        letra = input("\nDigite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("❌ Entrada inválida! Digite apenas uma letra.")
            continue

        if letra in letras_corretas or letra in letras_erradas:
            print("⚠️ Você já tentou essa letra!")
            continue

        if letra in palavra_secreta:
            letras_corretas.add(letra)
            print("✅ Boa! A letra está na palavra.")
        else:
            letras_erradas.add(letra)
            tentativas -= 1
            print("❌ Errou! A letra não está na palavra.")

        if set(palavra_secreta) == letras_corretas:
            print(f"\n🎉 Parabéns! Você adivinhou a palavra: {palavra_secreta}")
            break
    else:
        print(f"\n💀 Você perdeu! A palavra era: {palavra_secreta}")


jogar_forca()
