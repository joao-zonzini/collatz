#!/usr/bin/python3
# hist_collatz.py
# compara os passos de valores aplicados ao problema de 3n+1
# jaz 01/08/21

import sys
import matplotlib.pyplot as plt

import utils.collatz as cltz

if (len(sys.argv) < 2): ## se nao tiver os argumentos, para
    print("Erro! Falta o argumento.")
    exit(0)

num_final = int(sys.argv[1])
passos = []
numero = []
maior_passos = 0

for num in range(1, num_final+1):
    passos.append(cltz.n_passos_de_collatz(num))
    numero.append(num)


#plt.xlim([0, num_final])                    ## limite do eixo x
#plt.ylim([0, maior_passos])               ## limite do eixo y ja nao cabe tudo
plt.scatter(numero, passos, s=1)   ## plot grafico
plt.show()
