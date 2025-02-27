'''# Classe Veículo
class Veículo:
    def __init__(self, chassi, modelo, placa):
        self.chassi = chassi
        self.modelo = modelo
        self.placa = placa

    def __str__(self):
        return f"Chassi: {self.chassi}, Modelo: {self.modelo}, Placa: {self.placa}"

# Classe Concessionária
class Concessionária:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.estoque_veículos = []  # Lista vazia de veículos no estoque

    def adicionarVeículo(self, veículo):
        self.estoque_veículos.append(veículo)

    def __str__(self):
        veículos = "\n".join(str(veículo) for veículo in self.estoque_veículos)
        return f"Concessionária: {self.nome}, Telefone: {self.telefone}\nVeículos no Estoque:\n{veículos}\n"

# Classe Fabricante
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.__lista_concessionarias = []  # Lista privada de concessionárias

    def adicionarConcessionária(self, concessionária):
        self.__lista_concessionarias.append(concessionária)

    def listarConcessionarias(self):
        print(f"Fabricante: {self.nome}")
        for concessionária in self.__lista_concessionarias:
            print(concessionária)

# Programa Principal
if __name__ == "__main__":
    # Criando veículos
    veículo1 = Veículo("12345A", "Fiat Uno", "ABC-1234")
    veículo2 = Veículo("67890B", "Fiat Palio", "DEF-5678")
    veículo3 = Veículo("54321C", "Fiat Toro", "GHI-9012")
    veículo4 = Veículo("09876D", "Fiat Argo", "JKL-3456")

    # Criando concessionárias
    concessionária1 = Concessionária("Concessionária Alfa", "(11) 1234-5678")
    concessionária2 = Concessionária("Concessionária Beta", "(11) 8765-4321")

    # Adicionando veículos às concessionárias
    concessionária1.adicionarVeículo(veículo1)
    concessionária1.adicionarVeículo(veículo2)

    concessionária2.adicionarVeículo(veículo3)
    concessionária2.adicionarVeículo(veículo4)

    # Criando um fabricante e adicionando as concessionárias
    fabricante = Fabricante("Fiat")
    fabricante.adicionarConcessionária(concessionária1)
    fabricante.adicionarConcessionária(concessionária2)

    # Listando as concessionárias e seus veículos associados ao fabricante
    fabricante.listarConcessionarias()
'''

class Veiculo:
    def __init__(self, chassi, modelo, placa):
        self.chassi = chassi
        self.modelo = modelo
        self.placa = placa


class Concessionaria:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.listaVeiculos = []

    def adicionarVeiculo(self, veiculo):
        self.listaVeiculos.append(veiculo)


class Fabricante:
    def __init__(self):
        self.__listaConcessionarias = []

    def adicionarConcessionaria(self, concessionaria):
        self.__listaConcessionarias.append(concessionaria)


# Criando objetos de Veiculos
corsa = Veiculo('XZ173', 'Corsa', 'PGT876')
creta = Veiculo('ZY112', 'Creta', 'KLM754')
onix = Veiculo('BX998', 'Onix', 'PVX991')
corola = Veiculo('HJ536', 'Corola', 'JHB247')

# Criando objetos de Concessionarias
recife_veiculos = Concessionaria('RecifeVeiculos', '814738392', 'Recife')
caxanga_automoveis = Concessionaria('CaxangaAutomoveis', '81436745', 'Caxanga')

# Adicionando veículos às concessionárias
recife_veiculos.adicionarVeiculo(corsa)
recife_veiculos.adicionarVeiculo(creta)
caxanga_automoveis.adicionarVeiculo(onix)
caxanga_automoveis.adicionarVeiculo(corola)

# Criando objeto de Fabricante e adicionando concessionárias
honda = Fabricante()
honda.adicionarConcessionaria(recife_veiculos)
honda.adicionarConcessionaria(caxanga_automoveis)
