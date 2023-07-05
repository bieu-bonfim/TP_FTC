from PILHA.Mina import *
from PILHA.Anao import *
from PILHA.Crafting import *
from Auxiliar import roll

def genStr(size=2):
    mina_str = ''
    for i in range(size):
        mina_str = mina_str + str(roll(10)-1)
    return mina_str

def run_pilha():
    mina = Mina('Moria', genStr(roll(5)))
    mina.criaMina()
    anao = Anao('Ballin', mina)
    anao.explorar()
