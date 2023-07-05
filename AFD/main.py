import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.append('../')

from AFD.Jokenpo_AFD import *
from OutTerm import *
from colorama import init, Fore, Back, Style

init()

def menu():
    clear_terminal(0)
    print_slow(f"\x1b[91m\x1b[1m Seja bem vindo ao combate\
 que definirá o destino dos Domínios! \x1b[0m".center(180, "-"), "\n")
    print_slow(
        f"\x1b[1mApós a grande batalha, após tantas perdas, os\
 domínios concordaram em fazer uma MD3 de Jokenpô!\x1b[0m".center(175), "\n"
    )
    print_slow(
        f"\x1b[1mDesta forma os dois reinos devem informar suas três jogadas\
e após isso será informado o domínio vencedor.\x1b[0m". center(175), "\n"
    )
    while True:
        result = game()
        if result:
            break


def game():
    afd = Jokenpo_AFD()

    print("*".center(167, "-"))
    print_slow(f"\x1b[1mDomínio 1, escreva suas 3 jogadas separadas por espaço:", "\n")
    print_slow(f"\x1b[31mPapel: 0", "\n")
    print_slow(f"\x1b[32mPedra: 1", "\n")
    print_slow(f"\x1b[34mTesoura: 2", "\n")
    print_slow(f"\x1b[36m->\x1b[0m", " ")
    domain1 = list(map(int, input_p("").split()))

    print_slow(f"\x1b[1mDomínio 2, escreva suas 3 jogadas separadas por espaço:", "\n")
    print_slow(f"\x1b[31mPapel: 0", "\n")
    print_slow(f"\x1b[32mPedra: 1", "\n")
    print_slow(f"\x1b[34mTesoura: 2", "\n")
    print_slow(f"\x1b[36m->\x1b[0m", " ")
    domain2 = list(map(int, input_p("").split()))

    match afd.get_result(domain1, domain2):
        case "Domain 1":
            print_slow(f"\n\x1b[1mO Domínio 1... \x1b[32mfoi o Vencedor\x1b[0m!!!", "\n")
            return True
        case "Draw":
            print_slow(f"\n\x1b[1mDeu empate... Vamos ter que realizar outra MD3!\x1b[0m", "\n")
            return False
        case "Domain 2":
            print_slow(f"\n\x1b[1mO Domínio 2... \x1b[32mfoi o Vencedor\x1b[0m!!!", "\n")
            return True
