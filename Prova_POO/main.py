class Conta:
    # Iniciação do construtor:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    # Função de depósito:
    def depositar(self, valor):
        self.saldo += valor
        print(f'Valor depositado R${valor}')

    # Função de saque:
    def sacar(self, valor):
        # Condição para verificar se a conta possui o valor solicitado:
        if(self.saldo >= valor):
            self.saldo -= valor
            print(f'Valor solicitado para saque R${valor}')
        
        else:
            print(f'Você não tem a quantia de R${valor}.\n'
            f'Seu saldo atual é de R${self.saldo}')

    # Função de tranferência:
    def transfere(self, destino, valor):
        # Condição que verifica se a conta possui o valor para transferência
        if(self.saldo >= valor):
            self.saldo -= valor
            destino.saldo += valor
            print(f'{self.titular} fez uma transferência de R${valor} para {destino.titular}')
        
        else:
            print(f'{self.titular} você não tem a quantia de R${valor} para transferir.\n'
            f'Seu saldo atual é de R${self.saldo}.')

    # Função para mostrar todos os dados:
    def extrato(self):
        print(f'Titular: {self.titular}. \n'
        f'Numero: {self.numero}.\n'
        f'Saldo: {self.saldo}\n'
        f'Limite de crédito: {self.limite}.')
