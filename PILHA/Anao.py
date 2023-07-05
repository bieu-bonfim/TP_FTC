from Mina import *
from time import sleep as s
from colorama import init, Fore, Back, Style
import sys
import os
init()

class Anao:
    
    def __init__(self, nome, mina : Mina):
        self.nome = nome
        self.bolsa = []
        self.mapa = mina
        self.estado = None
        self.moedas = 0
        
    def explorar(self):
        os.system('clear || cls')
        print('-------------------------------------------')
        print(f'Mapa da mina: ', end='')
        self.mapa.mostraMapa()
        print('-------------------------------------------')
        s(2)
        os.system('clear || cls')
        minerios = ['Ferro', 'Prata', 'Ouro', 'Platina', 'Esmeralda', 'Safira', 'Rubi', 'Diamante', 'Mithril']
        count = 0
        self.estado = 'inicio'
        self.anaoStatus()
        s(2)
        while True:
            if self.mapa.mina[count] == '<':
                os.system('clear || cls')
                self.estado = 'saindo'
                self.anaoStatus()
                print(f'{Back.RED}       ', end="", flush=True)
                s(0.7)
                print(f'{Back.RED}       ', end="", flush=True)
                s(0.7)
                print(f'{Back.RED}       ', end="", flush=True)
                s(0.7)
                print(f'{Back.RED}       ', end="", flush=True)
                s(0.7)
                print(f'{Back.RED}       {Back.RESET}', end="", flush=True)
                s(0.7)                
                print()
                os.system('clear || cls')
                print(f'{Fore.RED}Hora de Desempilhar!{Fore.RESET}')
                break
            if self.mapa.mina[count] == '>':
                self.estado = 'minerando'
                count += 1
                while True:
                    if self.mapa.mina[count] == 0:
                        print(f'{Fore.RED}{self.nome}{Fore.RESET} minerando', end="", flush=True)
                        s(1)
                        print('\r\033[2K', end="", flush=True)
                        s(0.5)
                        count += 1
                        continue
                    elif self.mapa.mina[count] == '&':
                        break
                    elif self.mapa.mina[count] == '<':
                        break
                    else:
                        minerio_atual = self.mapa.mina[count]
                        minerio_atual = minerios[minerio_atual-1]
                        self.bolsa.append(self.mapa.mina[count])
                        os.system('clear || cls')
                        print(f'Bioma: {self.mapa.bioma_atual} rico em {Fore.GREEN}{minerio_atual}{Fore.RESET}')
                        print('----------------------------------------------------------------------------------------------------------------------------')
                        self.printBolsa()
                        print('----------------------------------------------------------------------------------------------------------------------------')
                        minerio_atual = self.mapa.mina[count]
                        minerio_atual = minerios[minerio_atual-1]
                        print(f'{Fore.RED}{self.nome}{Fore.RESET} encontra {Fore.GREEN}{minerio_atual}{Fore.RESET}!', end="", flush=True)
                        s(1)
                        print('\r\033[2K', end="", flush=True)
                        s(1)
                        count += 1
            if self.mapa.mina[count] == '&' and self.mapa.mina[count+1] != '<':
                self.estado = 'avançando'
                os.system('clear || cls')
                self.anaoStatus()
                print(f'{Back.GREEN}      ', end="", flush=True)
                s(0.7)
                print(f'{Back.GREEN}      ', end="", flush=True)
                s(0.7)
                print(f'{Back.GREEN}      ', end="", flush=True)
                s(0.7)
                print(f'{Back.GREEN}      ', end="", flush=True)
                s(0.7)
                print(f'{Back.GREEN}      {Back.RESET}', end="", flush=True)
                s(0.7)
                count += 1
                bioma = random.randint(0, 4)
                self.mapa.bioma_atual = self.mapa.biomas[bioma]
                os.system('clear || cls')
                print(f'Bioma: {self.mapa.bioma_atual}')
                self.printBolsa()
                while True:
                    if self.mapa.mina[count] == 0:
                        print(f'{Fore.RED}{self.nome}{Fore.RESET} minerando', end="", flush=True)
                        s(1)
                        print('\r\033[2K', end="", flush=True)
                        s(0.5)
                        count += 1
                        continue
                    elif self.mapa.mina[count] == '&':
                        break
                    elif self.mapa.mina[count] == '<':
                        break
                    else:
                        minerio_atual = self.mapa.mina[count]
                        minerio_atual = minerios[minerio_atual-1]
                        self.bolsa.append(self.mapa.mina[count])
                        os.system('clear || cls')
                        print(f'Bioma: {self.mapa.bioma_atual} rico em {Fore.GREEN}{minerio_atual}{Fore.RESET}')
                        print('----------------------------------------------------------------------------------------------------------------------------')
                        self.printBolsa()
                        print('----------------------------------------------------------------------------------------------------------------------------')
                        print(f'{Fore.RED}{self.nome}{Fore.RESET} encontra {Fore.GREEN}{minerio_atual}{Fore.RESET}!', end="", flush=True)
                        s(1)
                        print('\r\033[2K', end="", flush=True)
                        s(1)
                        count += 1
            else:
                count+=1

        vender = inverted_array = self.bolsa[::-1]
        minerios = ['Ferro', 'Prata', 'Ouro', 'Platina', 'Esmeralda', 'Safira', 'Rubi', 'Diamante', 'Mithril']
        valores = ['1', '2', '5', '10', '12', '13', '14', '20', '50']
        for i in range(len(vender)):
            print(f'{Fore.RED}{self.nome}{Fore.RESET} vende {minerios[vender[i]-1]} e ganha {Fore.YELLOW}{valores[vender[i]-1]}{Fore.RESET} moedas!')
            self.moedas += int(valores[vender[i]-1])
        print(f'Moedas de {Fore.YELLOW}ouro{Fore.RESET} totais: {Fore.YELLOW}{self.moedas}{Fore.RESET}')
                
    def printBolsa(self):
        ferro = 0
        prata = 0
        ouro = 0
        platina = 0
        esmeralda = 0
        safira = 0
        rubi = 0
        diamante = 0
        mithril = 0
        
        for i in range(len(self.bolsa)):
            if self.bolsa[i] == 1:
                ferro += 1
            if self.bolsa[i] == 2:
                prata += 1
            if self.bolsa[i] == 3:
                ouro += 1
            if self.bolsa[i] == 4:
                platina += 1
            if self.bolsa[i] == 5:
                esmeralda += 1
            if self.bolsa[i] == 6:
                safira += 1
            if self.bolsa[i] == 7:
                rubi += 1
            if self.bolsa[i] == 8:
                diamante += 1
            if self.bolsa[i] == 9:
                mithril += 1
        print(f'Bolsa: {Fore.CYAN}ferro{Fore.RESET} = {ferro} | {Fore.CYAN}prata{Fore.RESET} = {prata} | {Fore.YELLOW}ouro{Fore.RESET} = {ouro} | {Fore.CYAN}platina{Fore.RESET} = {platina} | {Fore.GREEN}esmeralda{Fore.RESET} = {esmeralda} | {Fore.BLUE}safira{Fore.RESET} = {safira} | {Fore.RED}rubi{Fore.RESET} = {rubi} | {Fore.MAGENTA}diamante{Fore.RESET} = {diamante} | {Fore.MAGENTA}mithrill{Fore.RESET} = {mithril}')
            
            
    def anaoStatus(self):
        if self.estado == 'inicio':
            print(f'{Fore.RED}{self.nome}{Fore.RESET} começa sua jornada pela mina de {Fore.MAGENTA}{self.mapa.nome}!{Fore.RESET}')
        if self.estado == 'avançando':
            print(f'{self.nome} avança pela mina de {self.mapa.nome}')
        if self.estado == 'saindo':
            print(f'{self.nome} sai da mina e retorna com seus minérios.')