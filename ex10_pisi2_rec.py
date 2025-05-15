def soma_array(arr, n):
    if n == 0:
        return 0
    else:
        return arr[n - 1] + soma_array(arr, n - 1)
