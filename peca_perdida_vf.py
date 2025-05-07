
# Maneira pouco esperta
def esta_dentro(lista, x):
    '''função booleana que retorna se um número pertence a uma lista'''
    achou = False
    for i in lista:
        if x == i:
            achou = True
            break
    return achou

def main():
    '''Programa principal'''
    # lendo entrada
    quantidade_de_pecas = int(input())
    lista_incompleta = [int(i) for i in input().split()]

    # para cada item da lista completa, verificar se pertence à incompleta
    lista_completa = list(range(1, quantidade_de_pecas + 1))
    for i in lista_completa:
        if not esta_dentro(lista_incompleta, i):
            print(i)
            break

def main_medio_esperto():
    
main_pouco_esperto()

