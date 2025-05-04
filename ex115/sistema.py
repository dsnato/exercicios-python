from ex115.lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        cabeçalho('\033[36mOpção 1\033[m')
    elif resposta == 2:
        cabeçalho('\033[36mOpção 2\033[m')
    elif resposta == 3:
        cabeçalho('\033[35mSaindo do sistema... Até logo!\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
