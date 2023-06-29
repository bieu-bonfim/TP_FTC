from Estado import Estado
from Auxiliar import leitura, roll

class AutomatoMoore:
  
  def __init__(self, file : str, nome : str):
    self.file = file
    self.nome = nome
    self.estados = {}
    self.estado_atual : Estado = None
    # self.atk_bonus = 0
    # self.hit_bonus = 0
    # self.armor_class = 0
    # self.heal_bonus = 0
    self.life = 20
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
  
  def execute(self, inpt):
    new = self.estado_atual.get_transition(inpt)
    if new:
      self.set_current(new)
      act = self.estado_atual.output
      num = 0
      if act == 'rng':
        act = roll(6)
        act = 'def' if act == 1 else 'cur' if act == 2 else 'atk'
      if act == 'atk':
        num = roll(8)
        print(f'A {self.nome} desfere um golpe de {num} de dano!')
      elif act == 'def':
        num = roll(6)
        print(f'A {self.nome} se defende, mitigando um total de {num} de dano!')
      elif act == 'cur':
        num = roll(4)
        print(f'A {self.nome} conjura um ritual de cura, recuperando {num} de vida!')
      return act, num
    else:
      print('Entrada não reconhecida')