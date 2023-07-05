from OutTerm import *
import os

from Moore.Guerreiro import Guerreiro
from Moore.Combate import Combate
from AFN.AFN import AFN
import AFD.main as AFD
from Moore.Menu import creation
from PILHA.run import run_pilha

os.system("cls || clear")

print_slow("\x1b[1m\x1b[33m Bem vindo ao programa de simulações de autômatos! \x1b[0m".center(180, "-"), "\n\n")
print_slow("\x1b[1mSelecione o autômato que deseja simular:\x1b[0m", "\n\n")
print_slow("\x1b[1m\x1b[36mMáquina de Moore (Guerreiros) -> 1\x1b[0m", "\n")
print_slow("\x1b[1m\x1b[33mAFD (Jokenpo) ".ljust(39, "-") + "-> 2\x1b[0m", "\n")
print_slow("\x1b[1m\x1b[32mAFN (Samurai) ".ljust(39, "-") + "-> 3\x1b[0m", "\n")
print_slow("\x1b[1m\x1b[34mAutômato de pilha (Anão) ".ljust(39, "-") + "-> 4\x1b[0m", "\n")
print_slow("\x1b[1m\x1b[31mSair do programa! ".ljust(39, "-") + "-> 0\x1b[0m", "\n")
escolha = -1
while escolha not in range(5):
    escolha = int(input_p("\x1b[1m>> \x1b[0m"))
    if escolha not in range(5):
        print_slow("\x1b[1m\x1b[41m\nEntrada inválida, tente novamente!\x1b[0m", "\n\n")
    else:
        if escolha == 0:
            print_slow("\x1b[1m\x1b[41m\nPrograma terminado. Adeus!\x1b[0m", "\n\n")
            exit()
        elif escolha == 1:
            maq1 = creation()
            maq2 = creation()

            combate = Combate([maq1, maq2])
            combate.start_combat()
        elif escolha == 2:
            AFD.menu()
        elif escolha == 3:
            afn = AFN()
            afn.init_AFN()
        elif escolha == 4:
            run_pilha()





