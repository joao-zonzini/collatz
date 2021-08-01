#!/usr/bin/python3
# collatz_maiores.py
# plota os maiores numeros de uma sequencia
# aplicados a conjectura de collatz
# jaz 01/08/21

## importando as bibliotecas
import sys
import matplotlib.pyplot as plt

if (len(sys.argv) < 2): ## se o nao tiver os argumentos, para
    print("Erro! Falta o argumento.")
    exit(0)

def collatz(num): ## definindo a funcao collatz
    if(num % 2 == 0):
        return (num / 2)
    else:
        return ((num * 3) + 1)


## usando os argumentos
num_comeca = int(sys.argv[1])
num_final = num_comeca + 1          ## caso o segundo arg nao seja dado
num_final = int(sys.argv[2])

l_maior_numero = []                 ## vetor dos maiores numeros
l_numeros = []                      ## vetor dos numeros em si
maior_dos_numeros = 0               ## pra descobrir o maior dos numeros

for num in range(num_comeca, num_final+1):      ## percorrendo o range dado nos args
    maior_num = num                             ## por enquanto o maior eh o propio num
    l_numeros.append(num)                       ## salvando o num da iteracao
    while (num != 1):                           ## condicao de collatz
        num = collatz(num)                      ## testando num
        if (num > maior_num):                   ## se o numero out maior do que o in, salvar como maior
            maior_num = num
    l_maior_numero.append(maior_num)            ## so entra depois de chegar em 1, maior verdadeiro

for j in range(0, len(l_maior_numero)):             ## percorre o vetor l_maior_numero para o maior de todos
    if (l_maior_numero[j] > maior_dos_numeros):
        maior_dos_numeros = l_maior_numero[j]


plt.xlim([0, l_numeros[-1]])                    ## limite do eixo x
plt.ylim([0, l_maior_numero[-1]])               ## limite do eixo y ja nao cabe tudo
plt.scatter(l_numeros, l_maior_numero, s=0.5)   ## plot grafico
plt.show()

## salvando dados em csv
dados = open("dados.csv", "w")
for i in range(0, len(l_numeros)):
    concat = str(l_numeros[i]) + ", " + str(l_maior_numero[i]) + "\n"
    dados.write(concat)

dados.close()
