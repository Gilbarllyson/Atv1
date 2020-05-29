class Pessoa:
    
    def __init__(self, nome, data_nasc):
        self.nome = nome
        self.data_nasc = data_nasc
        
    def pagar(self):
        print('Valor a ser pago...')
    
    def receber(self):
        print('Valor a receber...')

    
  
class Conta(Pessoa):
    
    def __init__(self, nome, data_nasc, cpf=None):
        self.cpf = cpf
        super().__init__(nome, data_nasc)

    def validar_cpf(self):
        if len(self.cpf) == 14:
            print('CPF Válido!')
        else:
            print('CPF Inválido!')
        
        print('#---------------------------------------#')

    def tipoconta(self):
        print('Tipo da conta:', "Poupança Ouro")
    
    def pagar(self):
        print('O valor a ser pago é:', "R$ 200")

    def data_vencimento(self):
        print('Vencimento: ', "10/06/2020")

    def receber(self):
        print('O valor a receber é:', "R$ 1.200")    

#-------------------------------------------------------------#

    def pagar2(self):
        print('O valor a ser pago é:', "R$ 20,76")   

    def data_vencimento2(self):
        print('Vencimento: ', "20/011/2020")

    def receber2(self):
        print('O valor a receber é:', "R$ 150,22")

    def tipocont2(self):
        print('Tipo da conta:', "Corrente")    
    