from colorama import init, Fore, Back, Style
from Guerreiro import Guerreiro
init()

def creation():
  print(f'Seja bem vindo ao combate que definirá o destino dos reinos.')
  print(f'O conselho dos lordes requisita que cada reino inscreva um')
  print(f'dos deus guerreiros para lutar pela liberdade e pela honra.')
  print(f'Escreva o nome de seu {Fore.GREEN}pergaminho de inscrição{Style.RESET_ALL} e detalhe as')
  print(f'características de seu guerreiro logo abaixo.')
  print(f'Que o destino seja definido na arena de {Fore.RED}Vermécia{Style.RESET_ALL}!\n')
  
  print(f'Insira o {Fore.BLUE}nome de seu pergaminho{Style.RESET_ALL}')
  file = input(' >> ')
  print(f'Qual o {Fore.BLUE}nome de seu campeão{Style.RESET_ALL}?')
  guerr = input(' >> ')
  print(f'Qual o {Fore.BLUE}nome de seu reinado{Style.RESET_ALL}?')
  reino = input(' >> ')
  
  print(f'Agora, insira a {Fore.MAGENTA}distribuição de pontos de status{Style.RESET_ALL} de seu guerreiro: ')
  print(f'OBS: Você possui 10 pontos, insira a pontuação com separação de')
  print(f'espaços na ordem DEX STR WIS:')
  points = input('>> ')
  points = points.strip().split()
  maq = Guerreiro(file, reino, guerr, int(points[0]), int(points[1]), int(points[2]))
  
  return maq

