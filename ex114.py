import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.kaggle.com/learn/python')
except urllib.error.URLError:
    print('O site não está acessível no momento.')
else:
    print('Consegui acessar o site com sucesso.')
