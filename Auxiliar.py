def leitura(file):
  with open(file, 'r') as file:
    lines = file.readlines()

  outputs = []
  transitions = []

  for line in lines:
    if line.startswith('Q:'): 
      estados = line.strip().split(' ')[1:]
      for e in estados:
        if e[0] == 'A':
          out = 'atk'
        elif e[0] == 'D':
          out = 'def'
        elif e[0] == 'C':
          out = 'cur'
        else:
          out = 'rng'
        outputs.append(out)
    elif line.startswith('I:'): 
      inicial = line.strip().split('I: ')[1]
    else:
      half1 = line.strip().split('|')[0]
      half2 = line.strip().split('|')[1]
      partida = half1.strip().split(' ')[0]
      destino = half1.strip().split(' ')[2]
      leituras = half2.strip().split(' ')
      for l in leituras:
        transitions.append({
          l: destino
        })

  return estados, outputs, inicial, transitions