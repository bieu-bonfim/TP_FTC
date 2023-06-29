from AutomatoMoore import AutomatoMoore

def duelo(maq1, maq2):
  print('duelo')

maq1 = AutomatoMoore('teste.txt', 'Maquina1')
maq2 = AutomatoMoore('teste.txt', 'Maquina2')
turno = 0

maqs = [maq1, maq2]

while maqs[0].life > 0 and maqs[1].life >0:
  turno += 1
  print(f'Início do turno {turno}')
  print(f'Vez de {maqs[(turno-1)%2].nome}')
  in1 = input('Insira o número de entrada dessa rodada >> ')
  
  act1, num1 = maqs[(turno-1)%2].execute(in1)
  act2, num2 = maqs[(turno)%2].execute(in1)
  
  if act1 == 'atk':
    if act2 == 'def':
      maqs[(turno)%2].life -= (num1 - num2) if (num1 - num2) > 0 else 0
    else:
      maqs[(turno)%2].life -= num1
  elif act1 == 'cur':
    maqs[(turno-1)%2].life += num1
    
  if act2 == 'atk':
    if act1 == 'def':
      maqs[(turno-1)%2].life -= (num2 - num1) if (num2 - num1) > 0 else 0
    else:
      maqs[(turno-1)%2].life -= num2
  elif act2 == 'cur':
    maqs[(turno)%2].life += num2
    
  print(f'Vida da {maqs[0].nome}: {maqs[0].life}')
  print(f'Vida da {maqs[1].nome}: {maqs[1].life}')
    

if maqs[0].life <= 0 and maqs[1].life <= 0:
  print('empatou kkkk')
elif maqs[0].life <= 0:
  print(f"{maqs[0].nome} morreu")
else:
  print(f"{maqs[1].nome} morreu")