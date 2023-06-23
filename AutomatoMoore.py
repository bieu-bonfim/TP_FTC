from Estado import Estado

class AutomatoMoore:
  
  def __init__(self, file):
    self.file = file
    self.estados = {}
    self.estado_atual = None
    self.init_moore()
    
  def init_moore(self):
    with open(self.file, 'r') as file:
      lines = file.readlines()

    for line in lines:
      if line.startswith('Q:'): 
        estado = line.strip().split(' ')[1:] 
        for e in estado:
          if e[0] == 'A':
            out = 'atk'
          elif e[0] == 'D':
            out = 'def'
          elif e[0] == 'C':
            out = 'cur'
          else:
            out = 'rng'
          self.add_state(nome=e, output=out)
      elif line.startswith('I:'): 
        initial = line.strip().split('I: ')[1]
        self.set_current(nome=initial)
      else:
        half1 = line.strip().split('|')[0]
        half2 = line.strip().split('|')[1]
        partida = half1.strip().split(' ')[0]
        destino = half1.strip().split(' ')[2]
        leituras = half2.strip().split(' ')
        self.get_state(nome=partida).add_transition(leituras, destino)
  
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
  