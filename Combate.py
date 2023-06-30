from Auxiliar import roll, clear_console
from colorama import init, Fore, Back, Style
init()

class Combate:
  
  def __init__(self, maqs, tipo):
    self.turno = 0
    self.maqs = maqs
    self.maq1 = None
    self.maq2 = None
    self.tipo = tipo
    
  def start_combat(self):
    while self.maqs[0].life > 0 and self.maqs[1].life >0:
      self.maq1 = self.maqs[(self.turno-1)%2]
      self.maq2 = self.maqs[(self.turno)%2]
      inp = self.start_turn()
      clear_console()
      
      act1, num1 = self.maq1.execute(inp)
      act2, num2 = self.maq2.execute(inp)
        
      self.action(num1, num2, act1, act2)

      self.maq1.print_life()
      self.maq2.print_life()
      
      self.maqs[(self.turno-1)%2] = self.maq1
      self.maqs[(self.turno)%2] = self.maq2
      
    if self.maq1.life <= 0 and self.maq2.life <= 0:
      print('empatou kkkk')
    elif self.maq1.life <= 0:
      print(f"{self.maq1.nome} morreu")
    else:
      print(f"{self.maq2.nome} morreu")
    
  def start_turn(self):
    self.turno += 1
    print(f'Início do turno {Fore.RED}{self.turno}{Style.RESET_ALL}')
    print(f'Vez do campeão de {Fore.RED}{self.maq1.nome_reino}, {Fore.CYAN}{self.maq1.nome}{Style.RESET_ALL}')
    return input('Inscrevei a ordem do comandamento para a ação deste turno: >> ')
  
  def action(self, num1, num2, act1, act2):
    if act1 == 'atk':
      hit_raw = roll(20)
      hit = hit_raw+self.maq1.hit_bonus
      hit_str = str(hit)
      
      if hit_raw == 20:
        hit_str = Fore.GREEN+hit_str+Style.RESET_ALL
      if hit_raw == 1:
        hit_str = Fore.RED+hit_str+Style.RESET_ALL
        
      print(f'{self.maq1.nome} tenta desferir um golpe ({hit_str})...')
      got_hit = False
      
      if act2 == 'def':
        if hit >= self.maq2.armor_class + num2:
          print(f'{self.maq2.nome} tenta se defender, mas o golpe é {Fore.RED}forte demais{Style.RESET_ALL} para ser aparado!')
          got_hit = True
        else:
          print(f'{self.maq2.nome} ergue seu escudo com prontidão, {Fore.BLUE}mitigando completamente{Style.RESET_ALL} o golpe!')
          got_hit = False
      else:
        if hit >= self.maq2.armor_class:
          print(f'{ self.maq1.nome} ataca com rapidez, sem dar tempo de reação ao inimigo!')
          got_hit = True
        else:
          print(f'{ self.maq2.nome}, com muita agilidade, consegue se esquivar do golpe!')
          got_hit = False
      if got_hit:
        if hit_raw == 20:
          print(f'{self.maq1.nome} brande sua espada, carregando o peso de todas as almas de {Fore.RED}{self.maq1.nome_reino}{Style.RESET_ALL},')
          print(f'e desfere um ataque impiedoso sob o campeão de {Fore.BLUE}{self.maq2.nome_reino}{Style.RESET_ALL}.')
          num1 = num1+roll(10)
        self.maq2.life -= num1
        print(f'O ataque acerta o campeão de {self.maq2.nome_reino}, causando {Fore.RED}{num1}{Style.RESET_ALL} de dano!')
    elif act1 == 'cur':
      self.maq1.life += num1
      print(f'{ self.maq1.nome} recebe uma benção divina, recuperando {Fore.GREEN}{num1}{Style.RESET_ALL} pontos de vida!')
    elif act1 == 'def':
      print(f'{ self.maq1.nome} se prepara para {Fore.BLUE}defender{Style.RESET_ALL}!')
      
    print('\nEm resposta a isso:\n')
      
    if act2 == 'atk':
      hit_raw = roll(20)
      hit = hit_raw+self.maq2.hit_bonus
      hit_str = str(hit)
      
      if hit_raw == 20:
        hit_str = Fore.GREEN+hit_str+Style.RESET_ALL
      if hit_raw == 1:
        hit_str = Fore.RED+hit_str+Style.RESET_ALL
        
      print(f'{self.maq2.nome} tenta desferir um golpe ({hit_str})...')

      got_hit = False
      if act1 == 'def':
        if hit >= self.maq1.armor_class + num1:
          print(f'{self.maq1.nome} tenta se defender, mas o golpe é {Fore.RED}forte demais{Style.RESET_ALL} para ser aparado!')
          got_hit = True
        else:
          print(f'{self.maq1.nome} ergue seu escudo com prontidão, {Fore.BLUE}mitigando completamente{Style.RESET_ALL} o golpe!')
          got_hit = False
      else:
        if hit >= self.maq1.armor_class:
          print(f'{ self.maq2.nome} ataca com rapidez, sem dar tempo de reação ao inimigo!')
          got_hit = True
        else:
          print(f'{ self.maq1.nome}, com muita agilidade, consegue se esquivar do golpe!')
          got_hit = False
      if got_hit:
        if hit_raw == 20:
          print(f'{self.maq2.nome} brande sua espada, carregando o peso de todas as almas de {Fore.RED}{self.maq2.nome_reino}{Style.RESET_ALL},')
          print(f'e desfere um ataque impiedoso sob o campeão de {Fore.BLUE}{self.maq1.nome_reino}{Style.RESET_ALL}.')
          num2 = num2+roll(10)
        self.maq1.life -= num2
        print(f'O ataque acerta o campeão de {self.maq1.nome_reino}, causando {Fore.RED}{num2}{Style.RESET_ALL} de dano!')
    elif act2 == 'cur':
      self.maq2.life += num1
      print(f'{ self.maq2.nome} recebe uma benção divina, recuperando {Fore.GREEN}{num1}{Style.RESET_ALL} pontos de vida!')
    elif act2 == 'def':
      print(f'{ self.maq2.nome} preparou sua {Fore.BLUE}defesa{Style.RESET_ALL}!')