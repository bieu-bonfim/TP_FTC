from Moore.Estado import Estado
from Auxiliar import leitura, roll
from colorama import init, Fore, Back, Style
init()

class Guerreiro:
  
  def __init__(self, file : str, nome_reino : str, nome, dext, stre, wisd):
    self.file = file
    self.nome_reino = nome_reino
    self.nome = nome
    self.estados = {}
    self.estado_atual : Estado = None
    self.atk_bonus = stre
    self.hit_bonus = dext
    self.armor_class = 10 + dext
    self.heal_bonus = (wisd*2)
    self.life = 20 + stre
    self.init_guerreiro()
    
  def init_guerreiro(self):
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
    
  def print_life(self):
    print(f'Pontos de vida de {Fore.CYAN}{self.nome}: {Fore.RED}{self.life}{Style.RESET_ALL}')
    
  def add_state(self, nome, output):
    state = Estado(nome, output)
    self.estados[nome] = state
    
  def set_current(self, nome):
    self.estado_atual = self.estados[nome]
    
  def get_state(self, nome):
    return self.estados[nome]
  
  def execute(self, inpt):
    try:
      new = self.estado_atual.get_transition(inpt)
      self.set_current(new)
      act = self.estado_atual.output
      num = 0
      if act == 'rng':
        act = roll(6)
        act = 'def' if act == 1 else 'cur' if act == 2 else 'atk'
      if act == 'atk':
        num = roll(8)+self.atk_bonus
      elif act == 'def':
        num = roll(4)
      elif act == 'cur':
        num = roll(6)+self.heal_bonus
    except:
      print('Ação não inscrita nos pergaminhos, turno omitido')
      act = 'err'
      num = 0
    return act, num