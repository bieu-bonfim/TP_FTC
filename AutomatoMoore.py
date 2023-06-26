from Estado import Estado
from Auxiliar import leitura

class AutomatoMoore:
  
  def __init__(self, file):
    self.file = file
    self.estados = {}
    self.estado_atual = None
    self.init_moore()
    
  def init_moore(self):
    es, inicial, ts = leitura(self.file)
    for e in es:
      if e[0] == 'A':
        out = 'atk'
      elif e[0] == 'D':
        out = 'def'
      elif e[0] == 'C':
        out = 'cur'
      elif e[0] == 'I':
        out = ''
      else:
        out = 'rng'
      self.add_state(e, out)
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
    new = self.estado_atual.get_transition(input)
    if new:
      self.set_current(new)
      print(self.estados[new].output)