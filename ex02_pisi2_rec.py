def maximo_recursivo(V, n):
    if n == 1:
        return V[0]
    else:
        max_restante = maximo_recursivo(V, n - 1)
        return V[n - 1] if V[n - 1] > max_restante else max_restante
