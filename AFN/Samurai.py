from AFN.AFN import *
from Auxiliar import roll
from colorama import init, Fore, Back, Style
init()

class Samurai:
    def __init__(self, nome, vida, CA, dex, katana):
        self.nome = nome
        self.vida = vida
        self.CA = CA
        self.dex = dex
        self.katana= katana

    def recebe_ataque(self, inimigo:'Samurai'):
        if (roll(20) + inimigo.dex) >= self.CA:
            rolamento = roll(inimigo.katana)
            self.vida = self.vida - rolamento
            print(f'A lâmina de {Fore.CYAN}{inimigo.nome}{Fore.RESET} sibila no ar, atingindo {Fore.CYAN}{self.nome}{Fore.RESET} e causando {rolamento} de {Fore.RED}dano{Fore.RESET}!')
        else:
            print(f'A katana de {Fore.CYAN}{inimigo.nome}{Fore.RESET} ressoa enquanto se choca com a lâmina de {self.nome} que {Fore.GREEN}defende{Fore.RESET} o ataque!')
            
    def ataques_mutuos(self, inimigo: 'Samurai'):

        if (roll(20) + inimigo.dex) >= self.CA and (roll(20) + self.dex) >= inimigo.CA:
            dano1 = roll(inimigo.katana)
            dano2 = roll(self.katana)
            print(f'Os dois samurais em um {Fore.YELLOW}lampejo{Fore.RESET} se trespassam com suas lâminas... {Fore.CYAN}{self.nome}{Fore.RESET} sofre {Fore.RED}{dano1} de dano{Fore.RESET} e causa {Fore.RED}{dano2} de dano{Fore.RESET} a {Fore.CYAN}{inimigo.nome}{Fore.RESET}!')
            self.vida = self.vida - dano1
            inimigo.vida = inimigo.vida - dano2
        elif (roll(20) + inimigo.dex < self.CA) and (roll(20) + self.dex) >= inimigo.CA:
            dano = roll(self.katana)
            print(f'{Fore.CYAN}{self.nome}{Fore.RESET} desvia a katana de {Fore.CYAN}{inimigo.nome}{Fore.RESET} velozmente, lançado {Fore.YELLOW}faíscas{Fore.RESET} ao vento e o cortando profundamente com {Fore.RED}{dano} de dano{Fore.RESET}!')
            inimigo.vida = inimigo.vida - dano
        elif (roll(20) + inimigo.dex >= self.CA) and (roll(20) + self.dex) < inimigo.CA:
            dano = roll(inimigo.katana)
            print(f'{Fore.CYAN}{self.nome}{Fore.RESET} tenta atacar {Fore.CYAN}{inimigo.nome}{Fore.RESET}, mas ele é mais rápido. Desferindo um golpe feroz que causa {Fore.RED}{dano} de dano{Fore.RESET}!')
        else:
            print(f'Os dois samurais golpeam violentamente... Suas lâminas se chocam no e {Fore.YELLOW}faíscas{Fore.RESET} iluminam suas faces... {Fore.GREEN}Ambos bloquearam{Fore.RESET}.')
        
        
            
def embainhar(samurai1 : 'Samurai', samurai2 : 'Samurai'):
    if samurai1.vida > 0 and samurai2.vida > 0:
        print(f'Os dois {Fore.CYAN}samurais{Fore.RESET} se observam atentamente enquanto guardam suas Katanas, mas nenhum deles cai.{Fore.RESET}')
    if samurai1.vida <= 0 and samurai2.vida <=0:
        print(f'Os dois {Fore.CYAN}samurais{Fore.RESET} lentamente deslizam suas katanas de volta para suas bainhas... Uma {Fore.BLUE}leve brisa{Fore.RESET} sopra por eles, {Fore.RED}enquanto ambos caem no chão mortos{Fore.RESET}.')
    if samurai1.vida > 0 and samurai2.vida <= 0:
        print(f'{Fore.CYAN}{samurai1.nome}{Fore.RESET} observa atentamente enquanto guarda sua lâmina, {Fore.BLUE}{samurai2.nome}{Fore.RESET} cai de joelhos, com um profundo corte em seu peito... {Fore.RED}Ele está morto.{Fore.RESET}')
    if samurai1.vida <= 0 and samurai2.vida > 0:
        print(f'{Fore.CYAN}{samurai2.nome}{Fore.RESET} respira fundo, {Fore.MAGENTA}folhas de cerejeira caem ao seu redor,{Fore.RESET} enquanto atrás dele {Fore.BLUE}{samurai1.nome}{Fore.RESET} cai {Fore.RED}sem vida{Fore.RESET} no chão{Fore.RESET}.')