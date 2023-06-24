from Estado import Estado
from Auxiliar import leitura

class AutomatoMoore:
  
  def __init__(self, file):
    self.file = file
    self.estados = {}
    self.estado_atual = None
    self.init_moore()
    
  def init_moore(self):
    es, os, inicial, ts = leitura(self.file)
    for i in range(len(es)):
      self.add_state(es[i], os[i])
    self.estado_atual = self.estados[inicial]
    for t in ts:
      self.get_state(t['partida']).add_transition(t['leituras'], t['destino'])
  
  def print_self(self):
    print('Estados | Output:')
    for e in self.estados:
      self.estados[e].print_self()
    print('Atual:')
    self.estado_atual.print_self()
    
  def add_state(self, nome, output):
    state = Estado(nome, output)
    self.estados[nome] = state
    
  def set_current(self, nome):
    self.estado_atual = self.estados[nome]
    
  def get_state(self, nome):
    return self.estados[nome]
  
  def execute(self, input):
    new = self.estado_atual.transition(input)
    if new:
      self.set_current(new)
      print(self.estados[new].output)