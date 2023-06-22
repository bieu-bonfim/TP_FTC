class Estado:
  def __init__(self, nome, output):
    self.nome = nome
    self.output = output
    self.transitions = {}
    
  def printSelf(self):
    print(f"{self.nome} | {self.output}")
    for t in self.transitions:
      print(f"{t} -> {self.transitions[t]}")
  
  def add_transition(self, leitura, destino):
    for l in leitura:
      self.transitions[l] = destino