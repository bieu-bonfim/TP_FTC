import Estado
import Transicao
from Automato import Automato

with open('teste.txt', 'r') as file:
  lines = file.readlines()

maquina = Automato()

for line in lines:
  if line.startswith('Q:'): 
    estado = line.strip().split(' ')[1:] 
    for e in estado:
      maquina.add_state(nome=e, output='teste')
  elif line.startswith('I:'): 
    initial = line.strip().split('I: ')[1]
    maquina.set_current(nome=initial)
  else:
    half1 = line.strip().split('|')[0]
    half2 = line.strip().split('|')[1]
    partida = half1.strip().split(' ')[0]
    destino = half1.strip().split(' ')[2]
    leituras = half2.strip().split(' ')
    maquina.get_state(nome=partida).add_transition(leituras, destino)
    
# print("Q values:", estados)
# print("Initial I:", initial)
# print("Transitions:", transits)

maquina.printSelf()