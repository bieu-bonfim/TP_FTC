from colorama import init, Fore, Back, Style
import time
import os

def fmt(name):
    dict = {
        'rst' : '\x1b[0m',
        'b' : '\x1b[1m',
        'i' : '\x1b[3m',
        'u' : '\x1b[4m', 
        'sblk' : '\x1b[5m',
        'rlk' : '\x1b[6m',
        'rev' : '\x1b[7m',
        'crss' : '\x1b[9m',
        'fb' : '\x1b[30m',
        'fr' : '\x1b[31m',
        'fg' : '\x1b[32m',
        'fy' : '\x1b[33m',
        'fu' : '\x1b[34m',
        'fm' : '\x1b[35m',
        'fc' : '\x1b[36m',
        'fw' : '\x1b[37m',
        'fd' : '\x1b[39m',
        'bb' : '\x1b[40m',
        'br' : '\x1b[41m',
        'bg' : '\x1b[42m',
        'by' : '\x1b[43m',
        'bu' : '\x1b[44m',
        'bm' : '\x1b[45m',
        'bc' : '\x1b[46m',
        'bw' : '\x1b[47m',
        'bd' : '\x1b[49m',
    }

    return dict[name]

def is_fmt(code):
    vector = ['\x1b[0m', '\x1b[1m', '\x1b[3m', '\x1b[4m', '\x1b[5m', '\x1b[6m', '\x1b[7m', '\x1b[9m', '\x1b[30m',
                '\x1b[31m', '\x1b[32m', '\x1b[33m', '\x1b[34m', '\x1b[35m', '\x1b[36m', '\x1b[37m', '\x1b[39m', 
                '\x1b[40m', '\x1b[41m', '\x1b[42m', '\x1b[43m', '\x1b[44m', '\x1b[45m', '\x1b[46m', '\x1b[47m', 
                '\x1b[49m']
    return code in vector

def clear_terminal(delay):
    time.sleep(delay)
    os.system("clear || cls")

def print_slow(text, endc):
    os.system("tput civis") # Cursor do terminal invisível

    flag = -1
    fd = -1
    for i in range(len(text)):
        if is_fmt(text[i:i+5]):
            flag = i
            print(text[i:i+5], end="")

        
        if flag != -1:
            if i == flag + 5:
                flag = -1
                fd = -1
            else:
                continue

        print(text[i], end="")
        if text[i] != " ":
            time.sleep(0.02)
    print(end=endc)
    os.system("tput cvvis") # Cursor do terminal visível

def input_p(text):
    os.system("printf '\033[5 q'")
    print_slow(text, "")
    inserted = input()
    os.system("printf '\033[1 q'")
    return inserted

# t1 = '\x1b[91m\x1b[1m Seja bem vindo ao combate que definirá o destino dos reinos! \x1b[0m'
# t2 = '\x1b[1m O conselho dos lordes requisita que cada reino inscreva um \
# dos seus guerreiros para lutar pela liberdade e pela honra. \x1b[0m'
# t3 = '\x1b[1m Escreva o nome de seu \x1b[32mpergaminho de inscrição\x1b[39m e \
# detalhe as características de seu guerreiro logo abaixo. \x1b[0m'


# print_slow(t1.center(180,"-"), "\n")
# print_slow(t2.center(175), "\n")
# print_slow(t3.center(185), "\n")
# print_slow(t4.center(167), "\n")

                         
                        