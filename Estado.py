class Estado:
  def __init__(self, output, transitions):
    self.output = output
    self.transitions = transitions
    
  def some_method(self):
    print(f"Parameter 1: {self.parameter1}")
    print(f"Parameter 2: {self.parameter2}")