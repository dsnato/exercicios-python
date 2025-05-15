def permutacoes(s, prefixo=""):
    if len(s) == 0:
        print(prefixo)
    else:
        for i in range(len(s)):
            novo_prefixo = prefixo + s[i]
            resto = s[:i] + s[i+1:]
            permutacoes(resto, novo_prefixo)
