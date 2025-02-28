class ContaBancaria:
    def __init__(self, nomeDoTitular, numero, saldo, tipo):
        self.__saldo = saldo  # O saldo é protegido contra acesso externo
        self.nomeDoTitular = nomeDoTitular
        self.numero = numero
        self.tipo = tipo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente para saque.")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def imprimir_dados(self):
        print(f"Titular: {self.nomeDoTitular}, Número: {self.numero}, Tipo: {self.tipo}, Saldo: R${self.__saldo:.2f}")


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        if isinstance(conta, ContaBancaria):
            self.contas.append(conta)
            print("Conta adicionada com sucesso.")
        else:
            print("Erro: Objeto não é uma conta bancária válida.")

    def remover_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                self.contas.remove(conta)
                print("Conta removida com sucesso.")
                return
        print("Conta não encontrada.")

    def imprimir_contas(self):
        print(f"Cliente: {self.nome}, CPF: {self.cpf}")
        for conta in self.contas:
            conta.imprimir_dados()

# Exemplo de uso
conta1 = ContaBancaria("João Silva", "12345", 1000.0, "corrente")
conta2 = ContaBancaria("João Silva", "67890", 2000.0, "poupança")

cliente = Cliente("João Silva", "123.456.789-00")
cliente.adicionar_conta(conta1)
cliente.adicionar_conta(conta2)

cliente.imprimir_contas()
conta1.depositar(500)
conta1.sacar(200)
cliente.imprimir_contas()
