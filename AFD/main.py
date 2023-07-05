from Jokenpo_AFD import *
from colorama import init, Fore, Back, Style

init()


def menu():
    print(f"Seja bem vindo ao combate que definirá o destino dos domínios.")
    print(
        f"Após a grande batalha, após tantas perdas, os domínios concordaram em fazer uma MD3 de Jokenpô!"
    )
    print(
        f"Desta forma os dois reinos devem informar suas três jogadas, e após isso será informado o domínio vencedor."
    )
    while True:
        result = game()
        if result:
            break


def game():
    afd = Jokenpo_AFD()

    print(f"Domínio 1, escreva suas 3 jogadas separadas por espaço:")
    print(f"{Fore.RED}Papel: 0{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Pedra: 1{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Tesoura: 2{Style.RESET_ALL}")
    print(f"{Fore.CYAN}->{Style.RESET_ALL}", end=" ")
    domain1 = list(map(int, input().split()))

    print(f"Domínio 2, escreva suas 3 jogadas separadas por espaço:")
    print(f"{Fore.RED}Papel: 0{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Pedra: 1{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Tesoura: 2{Style.RESET_ALL}")
    print(f"{Fore.CYAN}->{Style.RESET_ALL}", end=" ")
    domain2 = list(map(int, input().split()))

    match afd.get_result(domain1, domain2):
        case "Domain 1":
            print(f"\nO Domínio 1... {Fore.GREEN}foi o Vencedor{Style.RESET_ALL}!!!\n")
            return True
        case "Draw":
            print(f"\nDeu empate... Vamos ter que realizar outra MD3!\n")
            return False
        case "Domain 2":
            print(f"\nO Domínio 2... {Fore.GREEN}foi o Vencedor{Style.RESET_ALL}!!!\n")
            return True


menu()
