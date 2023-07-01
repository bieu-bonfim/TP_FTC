from Guerreiro import Guerreiro
from Combate import Combate

from Menu import creation

maq1 = creation()
maq2 = creation()

combate = Combate([maq1, maq2])
combate.start_combat()


