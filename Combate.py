from AutomatoMoore import AutomatoMoore

from colorama import init, Fore, Back, Style
init()

class Combate:
  
  def __init__(self, maqs, tipo):
    self.turno = 0
    self.maqs = maqs
    self.tipo = tipo
    
  def start_combat(self):
    while self.maqs[0].life > 0 and self.maqs[1].life >0:
      inp = self.start_turn()
      
      act1, num1 = self.maqs[(self.turno-1)%2].execute(inp)
      act2, num2 = self.maqs[(self.turno)%2].execute(inp)
        
      self.action_moore(num1, num2, act1, act2)

      self.maqs[0].print_life()
      self.maqs[1].print_life()
    if self.maqs[0].life <= 0 and self.maqs[1].life <= 0:
      print('empatou kkkk')
    elif self.maqs[0].life <= 0:
      print(f"{self.maqs[0].nome} morreu")
    else:
      print(f"{self.maqs[1].nome} morreu")
    
  def start_turn(self):
    self.turno += 1
    print(f'Início do turno {Fore.RED}{self.turno}{Style.RESET_ALL}')
    print(f'Vez do campeão de {Fore.RED}{self.maqs[(self.turno-1)%2].nome_reino}, {Fore.CYAN}{self.maqs[(self.turno-1)%2].nome}{Style.RESET_ALL}')
    return input('Inscrevei a ordem do comandamento para a ação deste turno: >> ')
  
  def action_moore(self, num1, num2, act1, act2):
    if act1 == 'atk':
      if act2 == 'def':
        self.maqs[(self.turno)%2].life -= (num1 - num2) if (num1 - num2) > 0 else 0
        print(f'{self.maqs[(self.turno)%2].nome} se defende, mitigando {Fore.BLUE}{num2}{Style.RESET_ALL} pontos de dano!')
      else:
        self.maqs[(self.turno)%2].life -= num1
      print(f'{ self.maqs[(self.turno-1)%2].nome} desfere um golpe, causando {Fore.RED}{num1}{Style.RESET_ALL} de dano!')
    elif act1 == 'cur':
      self.maqs[(self.turno-1)%2].life += num1
      print(f'{ self.maqs[(self.turno-1)%2].nome} recebe uma benção divina, recuperando {Fore.GREEN}{num1}{Style.RESET_ALL} pontos de vida!')
      
    if act2 == 'atk':
      if act1 == 'def':
        self.maqs[(self.turno-1)%2].life -= (num2 - num1) if (num2 - num1) > 0 else 0
        print(f'{ self.maqs[(self.turno-1)%2].nome} se defende, mitigando {Fore.BLUE}{num1}{Style.RESET_ALL} pontos de dano!')
      else:
        self.maqs[(self.turno-1)%2].life -= num2
      print(f'{self.maqs[(self.turno)%2].nome} desfere um golpe, causando {Fore.RED}{num2}{Style.RESET_ALL} de dano!')
    elif act2 == 'cur':
      self.maqs[(self.turno)%2].life += num2
      print(f'{self.maqs[(self.turno)%2].nome} recebe uma benção divina, recuperando {Fore.GREEN}{num2}{Style.RESET_ALL} de vida!')