from main import Conta

# Registro das contas:
contaFabricio = Conta('2023-1', 'Fabricio', 350, 900)
contaRayssa = Conta('2002-4', 'Rayssa', 600, 1200)

# Operações:
contaFabricio.depositar(700)
contaFabricio.extrato()
print('--/--'*10)

contaRayssa.sacar(600)
contaRayssa.extrato()
print('--/--'*10)

contaFabricio.transfere(contaRayssa, 1200)
print('--/--'*10)
contaFabricio.extrato()
print('--/--'*10)
contaRayssa.extrato()

