from Estado import Estado
from colorama import init, Fore, Back, Style
from time import sleep as s
init()

class Crafting:
  
  def __init__(self, fita):
    self.fita = fita
    self.pos = 1
    self.estados = {}
    self.atual = None
    self.raridades = ['Ferro', 'Prata', 'Ouro', 'Platina', 'Esmeralda', 'Safira', 'Rubi', 'Diamante', 'Mithril']
    self.valores = ['1', '2', '5', '10', '12', '13', '14', '20', '50']
    self.init_crafting()
    
  def init_crafting(self):
    state = Estado('Nenhum')
    for i in range(9):
      state.add_transition(str(i+1), self.raridades[i])
    self.estados['Nenhum'] = state
    self.set_current('Nenhum')
    for i in range(9):
      state = Estado(self.raridades[i])
      for j in range(9):
        if j <= i:
          state.add_transition(str(j+1), self.raridades[i])
        else:
          state.add_transition(str(j+1), self.raridades[j])
      self.estados[self.raridades[i]] = state
    self.fita.insert(0, '<')
    self.fita.append('vazio')
    
  def set_current(self, nome):
    self.atual = self.estados[nome]
    
  def get_state(self, nome):
    return self.estados[nome]    
  
  def start_craft(self):
    while True:
      if self.fita[self.pos] == 'vazio':
        self.fita[self.pos] = self.raridades.index(self.atual.raridade)
        self.pos -= 1
        break
      new = self.atual.get_transition(str(self.fita[self.pos]))
      self.set_current(new)
      self.pos += 1
    print(f'Pelo visto, o minério mais raro que você encontrou foi {self.atual.raridade}')
    s(1)
    print('Agora, vamos calcular o valor total de seus achados...')
    print('------------------------------------------------------------')
    print(f'{Back.YELLOW}            ', end="", flush=True)
    s(0.7)
    print(f'{Back.YELLOW}            ', end="", flush=True)
    s(0.7)
    print(f'{Back.YELLOW}            ', end="", flush=True)
    s(0.7)
    print(f'{Back.YELLOW}            ', end="", flush=True)
    s(0.7)
    print(f'{Back.YELLOW}            {Back.RESET}', end="", flush=True)
    s(0.7)  
    print()
    print('------------------------------------------------------------')
    while True:
      if self.fita[self.pos] == '<':
        self.pos += 1
        break
      new = self.atual.get_transition(str(self.fita[self.pos]))
      self.fita[self.pos] = self.fita[self.pos]-1
      self.set_current(new)
      self.pos -= 1
    self.print_craft()
    
  def print_craft(self):
    armas_medievais = [
      "Flechas", 
      "Adaga", 
      "Espada curta", 
      "Espada longa", 
      "Machado de batalha",
      "Lança", 
      "Martelo de guerra", 
      "Arco longo", 
      "Espada lendária"
    ]
    cores = [
      "\033[1;30m"
      ,"\033[1;37m"
      ,"\033[1;35m"
      ,"\033[1;33m"
      ,"\033[1;32m"
      ,Fore.BLUE
      ,Fore.RED
      ,Fore.CYAN
      ,Fore.LIGHTRED_EX
    ]
    total = 0
    for i in range(1, len(self.fita)-1):
      total+=int(self.valores[self.fita[i]])
    cor_raridade = cores[self.fita[-1]]
    val_raridade = self.valores[self.fita[-1]]
    arma = armas_medievais[(total-int(val_raridade))%9]
    print(f"Parabéns! O anão conseguiu fazer {cor_raridade}{arma}{Style.RESET_ALL}!!!")
    s(3)
    print(f"O valor de seu item é de {Fore.YELLOW}{total}{Fore.RESET} moedas, feito com o mais puro {cor_raridade}{self.raridades[self.fita[-1]]}{Style.RESET_ALL}")
    
  def print_self(self):
    print('Estados')
    for e in self.estados:
      self.estados[e].print_self()
    print('Atual:')
    self.atual.print_self()