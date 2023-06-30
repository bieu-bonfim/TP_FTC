from AutomatoMoore import AutomatoMoore
from Combate import Combate

def duelo(maq1, maq2):
  print('duelo')

maq1 = AutomatoMoore('teste.txt', 'Valken', 'Soren')
maq2 = AutomatoMoore('teste.txt', 'Crisium', 'Alister')
combate = Combate([maq1, maq2], 'moore')
combate.start_combat()


