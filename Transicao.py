class Transicao:
  def __init__(self, read, dest):
    self.read = read
    self.dest = dest
    
  def printSelf(self):
    print(f"({self.read} -> {self.dest}")