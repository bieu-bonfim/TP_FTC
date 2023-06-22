with open('teste.txt', 'r') as file:
  lines = file.readlines()

estados = [] 
transits = []
initial = None 

for line in lines:
  if line.startswith('Q:'): 
    estado = line.strip().split(' ')[1:] 
    estados.append(estado) 
  elif line.startswith('I:'): 
    initial = line.strip().split('I: ')[1]
  else:
    half1 = line.strip().split('|')[0]
    half2 = line.strip().split('|')[1]
    transit = {
      "partida": half1.strip().split(' ')[0],
      "destino": half1.strip().split(' ')[2],
      "leituras": half2.strip().split(' ')
    }
    transits.append(transit)
    
print("Q values:", estados)
print("Initial I:", initial)
print("Transitions:", transits)