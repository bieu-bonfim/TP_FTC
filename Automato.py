from Estado import Estado

class Automato:
  
  def __init__(self):
    self.estados = {}
    self.estado_atual = None
    
  def printSelf(self):
    print('Estados | Output:')
    for e in self.estados:
      self.estados[e].printSelf()
    print('Atual:')
    self.estado_atual.printSelf()
    
  def add_state(self, nome, output):
    state = Estado(nome, output)
    self.estados[nome] = state
    
  def set_current(self, nome):
    self.estado_atual = self.estados[nome]
    
  def get_state(self, nome):
    return self.estados[nome]