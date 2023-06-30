from Guerreiro import Guerreiro
from Combate import Combate

def duelo(maq1, maq2):
  print('duelo')

maq1 = Guerreiro('teste.txt', 'Valken', 'Soren')
maq2 = Guerreiro('teste.txt', 'Crisium', 'Alister')
combate = Combate([maq1, maq2], 'moore')
combate.start_combat()


