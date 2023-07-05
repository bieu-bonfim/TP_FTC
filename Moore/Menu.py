from colorama import init, Fore, Back, Style
from Moore.Guerreiro import Guerreiro
from OutTerm import *
init()

def creation():
  clear_terminal(0)
  print_slow(f'\x1b[91m\x1b[1m Seja bem vindo ao combate\
 que definirá o destino dos reinos! \x1b[0m'.center(180, "-"), "\n")
  print_slow(f'\x1b[1m O conselho dos lordes requisita que cada reino inscreva um \
dos seus guerreiros para lutar pela liberdade e pela honra. \x1b[0m'.center(175), "\n")
  print_slow(f'\x1b[1m Escreva o nome de seu \x1b[32mpergaminho de inscrição\x1b[39m e \
detalhe as características de seu guerreiro logo abaixo. \x1b[0m'.center(185), "\n")
  print_slow(f'\x1b[1m Que o destino seja definido na arena de \x1b[31mVermécia\x1b[0m!\n'.center(180), "\n\n")
  
  print_slow(f'\x1b[1mInsira o \x1b[34mnome de seu pergaminho\x1b[0m', "\n")
  file = input(' >> ')
  print_slow(f'\x1b[1mQual o \x1b[34mnome de seu campeão\x1b[39m?\x1b[0m', "\n")
  guerr = input(' >> ')
  print_slow(f'\x1b[1mQual o \x1b[34mnome de seu reinado\x1b[39m?\x1b[0m', "\n")
  reino = input(' >> ')
  
  print_slow(f'\x1b[1mAgora, insira \
a {Fore.MAGENTA}distribuição de pontos de status\x1b[39m de seu guerreiro: \x1b[0m', "\n")
        
  print_slow(f'\x1b[1mOBS: Você possui 10 pontos, insira a pontuação \
com separação de espaços na ordem DEX STR WIS:\x1b[0m', "\n")
  points = input('>> ')
  print()
  os.system("clear")
  points = points.strip().split()
  maq = Guerreiro(file, reino, guerr, int(points[0]), int(points[1]), int(points[2]))
  
  return maq

