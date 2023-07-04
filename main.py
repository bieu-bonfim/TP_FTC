from Moore.Guerreiro import Guerreiro
from Moore.Combate import Combate

from Moore.Menu import creation

maq1 = creation()
maq2 = creation()

combate = Combate([maq1, maq2])
combate.start_combat()


