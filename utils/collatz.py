#!/usr/bin/python3
# collatz.py
# descrip
# jaz 08/01/21

## para importar, fazer:
## import utils.collatz as collatz

def collatz(num: int):
    if (num % 2 == 0):
        return (num / 2)
    else:
        return ((num * 3) + 1)


def n_passos_de_collatz(num: int):
    n_passos = 0
    while (num != 1):
        num = collatz(num)
        n_passos = n_passos + 1
    return n_passos


def collatz_passos(num: int):
    passo = 0
    l_passos = [passo]
    l_numeros = [num]
    while (num != 1):
        num = collatz(num)
        passo = passo + 1
        l_passos.append(passo)
        l_numeros.append(num)

    return l_passos, l_numeros


def collatz_maximo(num: int):
    maior = num
    while (num != 1):
        num = collatz(num)
        if (num > maior):
            maior = num

    return maior
