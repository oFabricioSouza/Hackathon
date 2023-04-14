from banco import Conta

# Declaração das contas
conta1 = Conta('0803', 'Fabricio', 5400.00, 6000.00)
conta2 = Conta('2204','Rayssa', 4000.00, 12000.00)

# Teste das funções:

print('--/--'*10)
conta1.extrato()

print('--/--'*10)
conta2.extrato()

conta1.trasnfere_para(conta2, 400.00)

print('--/--'*10)
conta2.extrato()

