#!/usr/bin/python3

import sys
import numpy as np
import matplotlib.pyplot as plt

if (len(sys.argv) < 2):
    print("Erro! Falta o argumento.")
    exit(0)

def collatz(num, passo):
    if(num % 2 == 0):
        num = (num / 2)
    else:
        num = ((num * 3) + 1)
    
    passo = passo + 1
    return num, passo



num = int(sys.argv[1])
passo = 0
maior_num = num

passos = [passo]
numero = [num]

while (num != 1):
    num, passo = collatz(num, passo)
    passos.append(passo)
    numero.append(num)
    if (num > maior_num):
        maior_num = num


print(maior_num)
plt.xlim([0, passos[-1]])
plt.ylim([0, maior_num])
plt.plot(passos, numero, "r")
plt.show()
