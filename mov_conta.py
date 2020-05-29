from pessoa import Conta

cliente1 = Conta("Gilbarllyson R.Silva", "30/02/1995", "132.433.139-10")

print('Informação do Cliente 01')
print('Nome:', cliente1.nome)
print('CPF:', cliente1.cpf)
print('Data de Nasc:', cliente1.data_nasc)

cliente1.tipoconta()
cliente1.data_vencimento()
cliente1.pagar()
cliente1.receber()
cliente1.validar_cpf()

cliente2 = Conta("Paulo Henrique Pereira", "20/07/1965", "332.456.139-13")

print('Informação do Cliente 02')
print('Nome:', cliente2.nome)
print('CPF:', cliente2.cpf)
print('Data de Nasc:', cliente2.data_nasc)

cliente2.tipocont2()
cliente2.data_vencimento2()
cliente2.pagar2()
cliente2.receber2()
cliente2.validar_cpf()