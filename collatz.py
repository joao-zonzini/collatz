#!/usr/bin/python3
# collatz_plot.py
# plota a trajetoria de um numero aplicado o problema 3n+1
# jaz 01/08/21

## importando bibliotecas
import sys
import matplotlib.pyplot as plt
import utils.collatz as cltz

if (len(sys.argv) < 2):
    print("Erro! Falta o argumento.")
    exit(0)


num = int(sys.argv[1])
passos = []
numero = []

passos, numero = cltz.collatz_passos(num)
maior_num = cltz.collatz_maximo(num)

print(maior_num)
plt.xlim([0, passos[-1]])
plt.ylim([0, maior_num])
plt.plot(passos, numero, "r")
plt.show()
