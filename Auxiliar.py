from random import randint

def leitura(file : str):
  with open(file, 'r') as file:
    lines = file.readlines()
    
  transitions = []

  for line in lines:
    if line.startswith('Q:'): 
      estados = line.strip().split(' ')[1:]
    elif line.startswith('I:'): 
      inicial = line.strip().split('I: ')[1]
    else:
      half1 = line.strip().split('|')[0]
      half2 = line.strip().split('|')[1]
      partida = half1.strip().split(' ')[0]
      destino = half1.strip().split(' ')[2]
      leituras = half2.strip().split(' ')
      transitions.append({
        'partida': partida,
        'destino': destino,
        'leituras': leituras,
      })

  return estados, inicial, transitions

def roll(max : int):
  return randint(1, max+1)