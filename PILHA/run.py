from PILHA.Mina import *
from PILHA.Anao import *
from PILHA.Crafting import *
from Auxiliar import roll

def genStr(size=2):
    opt = int(input('Escolha o modo:\n1- Caverna aleatória\n2- Caverna pré-definida'))
    if opt == 1:
        mina_str = ''
        for i in range(size):
            mina_str = mina_str + str(roll(10)-1)
        return mina_str
    elif opt == 2:
        mapa = input('\nInsira a caverna: ')
        return mapa

def run_pilha():
    mina = Mina('Moria', genStr(roll(5)))
    mina.criaMina()
    anao = Anao('Ballin', mina)
    anao.explorar()
