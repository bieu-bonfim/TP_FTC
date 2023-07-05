from PILHA.Mina import *
from PILHA.Anao import *
from PILHA.Crafting import *

def run_pilha():
    mina = Mina('Moria', '9')
    mina.criaMina()
    anao = Anao('Ballin', mina)
    anao.explorar()
