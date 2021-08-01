#!/usr/bin/python3
# collatz_maiores.py
# plota os maiores numeros de uma sequencia
# aplicados a conjectura de collatz
# jaz 01/08/21

## importando as bibliotecas
import sys
import matplotlib.pyplot as plt

import utils.collatz as cltz

if (len(sys.argv) < 2): ## se nao tiver os argumentos, para
    print("Erro! Falta o argumento.")
    exit(0)


## usando os argumentos
num_comeca = int(sys.argv[1])
num_final = int(sys.argv[2])

l_maior_numero = []                 ## vetor dos maiores numeros
l_numeros = []                      ## vetor dos numeros em si
maior_dos_numeros = 0               ## pra descobrir o maior dos numeros

for num in range(num_comeca, num_final+1):      ## percorrendo o range dado nos args
    l_numeros.append(num)                       ## salvando o num da iteracao
    l_maior_numero.append(cltz.collatz_maximo(num))            ## so entra depois de chegar em 1, maior verdadeiro

for j in range(0, len(l_maior_numero)):             ## percorre o vetor l_maior_numero para o maior de todos
    if (l_maior_numero[j] > maior_dos_numeros):
        maior_dos_numeros = l_maior_numero[j]


plt.xlim([l_numeros[0], l_numeros[-1]])                    ## limite do eixo x
plt.ylim([l_maior_numero[0], l_maior_numero[-1]])               ## limite do eixo y ja nao cabe tudo
plt.scatter(l_numeros, l_maior_numero, s=0.75)   ## plot grafico
plt.show()

## salvando dados em csv
dados = open("dados.csv", "w")
for i in range(0, len(l_numeros)):
    concat = str(l_numeros[i]) + ", " + str(l_maior_numero[i]) + "\n"
    dados.write(concat)

dados.close()
