def RaizQ(x, x0, e):
    if abs(x0 * x0 - x) <= e:
        return x0
    novo_x0 = (x0 * x0 + x) / (2 * x0)
    return RaizQ(x, novo_x0, e)
