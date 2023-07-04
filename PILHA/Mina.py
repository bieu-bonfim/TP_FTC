import random
class Mina:
    
    def __init__(self, nome, salas):
        self.nome = nome
        self.mina = []
        self.salas = salas
        
    def criaMina(self):
        self.mina.append('>')
        for i in range(len(self.salas)):
            if int(self.salas[i]) == 0:
                for k in range(10):
                    self.mina.append(0)
                self.mina.append('&')
            if int(self.salas[i]) == 1:
                pos = random.randint(1, 4)
                array = criaSala(pos, 1)
                for k in range(len(array)):
                    self.mina.append(array[k])
                self.mina.append('&')
            if int(self.salas[i]) == 2:
                pos = random.randint(1, 4)
                array = criaSala(pos, 2)
                for k in range(len(array)):
                    self.mina.append(array[k])
                self.mina.append('&')
            if int(self.salas[i]) == 3:
                pos = random.randint(1, 4)
                array = criaSala(pos, 3)
                for k in range(len(array)):
                    self.mina.append(array[k])
                self.mina.append('&')
            if int(self.salas[i]) == 4:
                pos = random.randint(1, 4)
                array = criaSala(pos, 4)
                for k in range(len(array)):
                    self.mina.append(array[k])
                self.mina.append('&')
            if int(self.salas[i]) == 5:
                pos = random.randint(1, 4)
                array = criaSala(pos, 5)
                for k in range(len(array)):
                    self.mina.append(array[k])
                self.mina.append('&')
            if int(self.salas[i]) == 6:
                pos = random.randint(1, 4)
                array = criaSala(pos, 6)
                for k in range(len(array)):
                    self.mina.append(array[k])
                self.mina.append('&')
            if int(self.salas[i]) == 7:
                pos = random.randint(1, 4)
                array = criaSala(pos, 7)
                for k in range(len(array)):
                    self.mina.append(array[k])
                self.mina.append('&')
            if int(self.salas[i]) == 8:
                pos = random.randint(1, 4)
                array = criaSala(pos, 8)
                for k in range(len(array)):
                    self.mina.append(array[k])
                self.mina.append('&')
            if int(self.salas[i]) == 9:
                pos = random.randint(1, 4)
                array = criaSala(pos, 9)
                for k in range(len(array)):
                    self.mina.append(array[k])
                self.mina.append('&')
        self.mina.append('<')
        for i in range(len(self.mina)):
            print(self.mina[i], end='')
        print()
                    
def criaSala(num_ones, minerio):
    array = [0] * 10
    positions = random.sample(range(10), num_ones)

    for pos in positions:
        array[pos] = minerio

    return array
                