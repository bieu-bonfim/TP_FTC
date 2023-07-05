import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.append('../')

from OutTerm import *

from AFN.EstadoAFN import *
from colorama import init, Fore, Back, Style
from random import randint
from AFN.Samurai import *
import os
init()

class AFN:

    def __init__(self):
        self.estados : EstadoAFN = []
        self.estado_atual : EstadoAFN = None
    
    def init_AFN(self):
        os.system('clear || cls')
        entrada = self.criaEstados()
        self.criaTransicoes()
        
        # Inserir informações dos samurais: Nome, Vida, CA, Destreza, Dano da Arma (Valores de dados: d4, d6, d8, d10, d12)
        samurai1 = Samurai('Aori', 10, 10, 3, 8)
        samurai2 = Samurai('Sekuki', 20, 10, 3, 8)
        
        ## Start da máquina (set do estado incial como atual)
        self.estado_atual = self.estados[0]
        luta = []
        
        while True:
            print(f'Quantidade {Fore.RED}mínima{Fore.RESET} de ataques para não ferir o código de honra: {Fore.RED}{entrada+2}{Fore.RESET}')
            string1 = input(f"Insira os movimentos de {Fore.CYAN}{samurai1.nome}{Fore.RESET}: ")
            string2 = input(f"Insira os movimentos de {Fore.CYAN}{samurai2.nome}{Fore.RESET}: ")
            #if len(string1) < entrada+2 or len(string2) < entrada+2:
            #    os.system('clear || cls')
            #    print(f'{Fore.RED}Insira uma sequência de ataques de tamanho mínimo 5!{Fore.RESET}')
            #    continue
            if len(string1) != len(string2):
                if len(string1) > len(string2):
                    os.system('clear || cls')
                    print(f'{Fore.RED}{samurai1.nome} precisa declarar ataques iguais aos de seu adversário!{Fore.RESET}')
                    continue
                if len(string1) < len(string2):
                    os.system('clear || cls')
                    print(f'{Fore.RED}{samurai2.nome} precisa declarar ataques iguais aos de seu adversário!{Fore.RESET}')
                    continue
            os.system('clear || cls')
            print('Os combatentes avançam!')

            for i in range(len(string1)):
                luta.append(string1[i])
                luta.append(string2[i])
            

            prox = ['0', '0']
            counter = 0
            tamanho_palavra = len(luta)
            codigo_de_honra = True

            for z in range(tamanho_palavra):
                    if tamanho_palavra == 0 and self.estado_atual.tipo != 'End':
                        print(f'{Fore.RED}Houve uma violação do código de honra!{Fore.RESET}')
                        codigo_de_honra = False
                        break
                    if tamanho_palavra == 0 and self.estado_atual.tipo == 'End':
                        print(f'Os dois {Fore.CYAN}samurais{Fore.RESET} param... Guardando lentamente suas katanas.')
                        embainhar(samurai1, samurai2)
                        self.estado_atual = self.estados[0]
                        break
                    
                    #próximos dois símbolos da palavra
                    prox[0] = luta[counter]
                    prox[1] = luta[counter+1]

                    if self.estado_atual.tipo == 'End':
                        print(f'Os dois {Fore.CYAN}samurais{Fore.RESET} param... Guardando lentamente suas katanas.')
                        embainhar(samurai1, samurai2)
                        self.estado_atual = self.estados[0]
                        break
                    if prox == ['0', '0']:
                            # ---------------------------------------
                            # golpes
                            samurai2.ataques_mutuos(samurai1)
                            # ---------------------------------------
                            if len(self.estado_atual.transicoes) > 2:
                                dict = self.estado_atual.transicoes[2]
                            else:
                                dict = self.estado_atual.transicoes[1]
                            novo_estado_nome = dict['alvo']
                            for e in self.estados:
                                if novo_estado_nome == e.nome:
                                    print(f'{Fore.YELLOW}{e.nome}{Fore.RESET}')
                                    self.estado_atual = e
                                    counter += 2
                                    tamanho_palavra -= 2
                                else:
                                    continue
                    if prox == ['1', '0']:
                            # ---------------------------------------
                            # golpes
                            samurai1.recebe_ataque(samurai2)
                            # ---------------------------------------
                            if len(self.estado_atual.transicoes) > 2:
                                dict = self.estado_atual.transicoes[1]
                            else:
                                dict = self.estado_atual.transicoes[1]
                            novo_estado_nome = dict['alvo']
                            for e in self.estados:
                                if novo_estado_nome == e.nome:
                                    print(f'{Fore.YELLOW}{e.nome}{Fore.RESET}')
                                    self.estado_atual = e
                                    counter += 2
                                    tamanho_palavra -= 2
                                else:
                                    continue
                    if prox == ['1', '1']:
                            # ---------------------------------------
                            # golpes
                            samurai1.ataques_mutuos(samurai2)
                            # ---------------------------------------
                            if len(self.estado_atual.transicoes) > 2:
                                dict = self.estado_atual.transicoes[2]
                            else:
                                dict = self.estado_atual.transicoes[1]
                            novo_estado_nome = dict['alvo']
                            for e in self.estados:
                                if novo_estado_nome == e.nome:
                                    print(f'{Fore.YELLOW}{e.nome}{Fore.RESET}')
                                    self.estado_atual = e
                                    counter += 2
                                    tamanho_palavra -= 2
                                else:
                                    continue
                    if prox == ['0', '1']:
                            # ---------------------------------------
                            # golpes
                            samurai2.recebe_ataque(samurai1)
                            # ---------------------------------------
                            if len(self.estado_atual.transicoes) > 2:
                                dict = self.estado_atual.transicoes[3]
                            else:
                                dict = self.estado_atual.transicoes[1]
                            novo_estado_nome = dict['alvo']
                            for e in self.estados:
                                if novo_estado_nome == e.nome:
                                    print(f'{Fore.YELLOW}{e.nome}{Fore.RESET}')
                                    self.estado_atual = e
                                    counter += 2
                                    tamanho_palavra -= 2
                                else:
                                    continue
            if codigo_de_honra != True:
                break
            if samurai1.vida <= 0 or samurai2.vida <= 0:
                break
            else:
                inimigo = int(input(f'Vocês podem acabar com isso sem mais {Fore.RED}sangue{Fore.RESET}... \n0 - {Fore.GREEN}Acabar luta{Fore.RESET}\n1 - {Fore.RED}Atacar!{Fore.RESET}\n'))
                if inimigo == 0:
                    print(f'{Fore.CYAN}{samurai1.nome}{Fore.RESET}... {Fore.CYAN}{samurai2.nome}{Fore.RESET}... {Fore.MAGENTA}Vocês não tem inimigos{Fore.RESET}!')
                    break
                else:
                    print(f'{Fore.RED}Que assim seja...{Fore.RESET}')
                    continue


    def criaEstados(self):
        inicial = EstadoAFN('I1', 'Ini')
        self.addEstado(inicial)
        entrada = int(input(f'Insira a quantidade de estados internos da máquina (cada 1 a mais adiciona 3 estados)): {Fore.GREEN}'))
        print(f'{Fore.RESET}')
        total = entrada * 3
        for i in range(total):
            if i == 0 or i%3 == 0:
                nome = f'E{i}'
                tipo = 'SM1'
                estado = EstadoAFN(nome, tipo)
                self.addEstado(estado)
            if i == 1 or i%3 == 1:
                nome = f'E{i}'
                tipo = 'EMP'
                estado = EstadoAFN(nome, tipo)
                self.addEstado(estado)
            if i == 2 or i%3 == 2:
                nome = f'E{i}'
                tipo = 'SM2'
                estado = EstadoAFN(nome, tipo)
                self.addEstado(estado)

        final = EstadoAFN('F1', 'End')
        self.addEstado(final)
        return entrada
    
    def criaTransicoes(self):
        count = 0
        for e in self.estados:
            if e.tipo == 'Ini':
                t0 = {'alvo' : 'E1', 'valor' : '00'}
                t1 = {'alvo' : 'E0', 'valor' : '10'}
                t2 = {'alvo' : 'E1', 'valor' : '11'}
                t3 = {'alvo' : 'E2', 'valor' : '01'}
                e.addTransition(t0)
                e.addTransition(t1)
                e.addTransition(t2)
                e.addTransition(t3)
                count += 1
                
            elif e.nome == 'F1':
                t0 = {'alvo' : 'F1', 'valor' : '00'}
                t1 = {'alvo' : 'F1', 'valor' : '10'}
                t2 = {'alvo' : 'F1', 'valor' : '11'}
                t3 = {'alvo' : 'F1', 'valor' : '01'}
                count +=1
                
            elif int(e.nome[1]) % 3 == 0 and count+4 < len(self.estados):
                t0 = {'alvo' : f'{count+3}', 'valor' : '00'}
                t1 = {'alvo' : f'E{count+2}', 'valor' : '10'}
                t2 = {'alvo' : f'E{count+3}', 'valor' : '11'}
                t3 = {'alvo' : f'E{count+4}', 'valor' : '01'}
                e.addTransition(t0)
                e.addTransition(t1)
                e.addTransition(t2)
                e.addTransition(t3)
                count += 1
                
            elif int(e.nome[1]) % 3 == 1 and count+3 < len(self.estados):
                t0 = {'alvo' : f'{count+2}', 'valor' : '00'}
                t1 = {'alvo' : f'E{count+1}', 'valor' : '10'}
                t2 = {'alvo' : f'E{count+2}', 'valor' : '11'}
                t3 = {'alvo' : f'E{count+3}', 'valor' : '01'}
                e.addTransition(t0)
                e.addTransition(t1)
                e.addTransition(t2)
                e.addTransition(t3)
                count += 1
                
            elif int(e.nome[1]) % 3 == 2 and count+2 < len(self.estados):
                t0 = {'alvo' : f'{count+1}', 'valor' : '00'}
                t1 = {'alvo' : f'E{count}', 'valor' : '10'}
                t2 = {'alvo' : f'E{count+1}', 'valor' : '11'}
                t3 = {'alvo' : f'E{count+2}', 'valor' : '01'}
                e.addTransition(t0)
                e.addTransition(t1)
                e.addTransition(t2)
                e.addTransition(t3)
                count += 1
            
            elif int(e.nome[1]) % 3 == 0 and count+4 >= len(self.estados):
                t0 = {'alvo' : f'F1', 'valor' : '00'}
                t1 = {'alvo' : f'F1', 'valor' : '10'}
                t2 = {'alvo' : f'F1', 'valor' : '11'}
                t3 = {'alvo' : f'F1', 'valor' : '01'}
                e.addTransition(t0)
                e.addTransition(t1)
                e.addTransition(t2)
                e.addTransition(t3)
                count += 1
        
            elif int(e.nome[1]) % 3 == 1 and count+4 >= len(self.estados):
                t0 = {'alvo' : f'F1', 'valor' : '00'}
                t1 = {'alvo' : f'F1', 'valor' : '10'}
                t2 = {'alvo' : f'F1', 'valor' : '11'}
                t3 = {'alvo' : f'F1', 'valor' : '01'}
                e.addTransition(t0)
                e.addTransition(t1)
                e.addTransition(t2)
                e.addTransition(t3)
                count += 1
                
            elif int(e.nome[1]) % 3 == 2 and count+4 >= len(self.estados):
                t0 = {'alvo' : f'F1', 'valor' : '00'}
                t1 = {'alvo' : f'F1', 'valor' : '10'}
                t2 = {'alvo' : f'F1', 'valor' : '11'}
                t3 = {'alvo' : f'F1', 'valor' : '01'}
                e.addTransition(t0)
                e.addTransition(t1)
                e.addTransition(t2)
                e.addTransition(t3)
                count += 1
        
    def addEstado(self, novo:'EstadoAFN'):
        self.estados.append(novo)
                 
