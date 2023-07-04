class EstadoAFN:

    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.transicoes = []
        
    def addTransition(self, transition):
        self.transicoes.append(transition)
        
    def showTransitions(self):
        for i in range(len(self.transicoes)):
            print(self.transicoes[i])