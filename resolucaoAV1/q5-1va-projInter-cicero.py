class Veiculo:

    def __init__(self, chassi, modelo, placa):
        self.chassi = chassi
        self.modelo = modelo
        self.placa = placa


class Concessionaria:

    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.listaVeiculos = []
        self.endereço = endereco

    def adicionarVeiculo(self, Veiculo):
        self.listaVeiculos.append(Veiculo)


class Fabricante:

    def __init__(self):
        self.__listaConcessionarias = []

    def adicionarConcessionaria(self, Concessionaria):
        self.__listaConcessionarias.append(Concessionaria)


Corsa = Veiculo('XZ173', 'Corsa', 'PGT876')
Creta = Veiculo('ZY112', 'Creta', 'KLM754')
Onix = Veiculo('BX998', 'Onix', 'PVX991')
Corola = Veiculo('HJ536', 'Corola', 'JHB247')

RecifeVeiculos = Concessionaria('RecifeVeiculos', '814738392', 'Recife')
CaxangaAutomoveis = Concessionaria('CaxangaAutomoveis', '81436745', 'Caxanga')

RecifeVeiculos.adicionarVeiculo(Corsa)
RecifeVeiculos.adicionarVeiculo(Creta)
CaxangaAutomoveis.adicionarVeiculo(Onix)
CaxangaAutomoveis.adicionarVeiculo(Corola)

Honda = Fabricante()
Honda.adicionarConcessionaria(RecifeVeiculos)
Honda.adicionarConcessionaria(CaxangaAutomoveis)