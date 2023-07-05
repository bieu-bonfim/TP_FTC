class Estado:
  def __init__(self, raridade):
    self.raridade = raridade
    self.transitions = {}
    
  def add_transition(self, leitura, destino):
    for l in leitura:
      self.transitions[l] = destino
      
  def get_transition(self, inpt):
    if inpt in self.transitions:
      return self.transitions[inpt]
    else:
      return False
    
  def print_self(self):
    print(f"{self.raridade}")
    for t in self.transitions:
      print(f"{t} -> {self.transitions[t]}")