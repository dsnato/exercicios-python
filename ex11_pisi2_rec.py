def inverter_array(arr, inicio, fim):
    if inicio >= fim:
        return
    # Troca os elementos
    arr[inicio], arr[fim] = arr[fim], arr[inicio]
    # Chamada recursiva
    inverter_array(arr, inicio + 1, fim - 1)
