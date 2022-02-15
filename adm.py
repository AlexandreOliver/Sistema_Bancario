class gerente:

    senha = 12345678
    
    def __init__(self, nome):
        self.nome = nome

class conta:

    def __init__(self, N_conta, dv, agencia):
        
        self.N_conta = N_conta
        self.dv = dv
        self.agencia = agencia
        
