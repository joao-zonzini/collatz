#!/usr/bin/python3

import subprocess as subp
import numpy as np
import matplotlib.pyplot as plt

comando_programa = "./n_collatz "

passos = []
numero = []

for num in range(1, 101):
    comando_completo = comando_programa + str(num)
    result = subp.getstatusoutput(comando_completo)
    r_limpo = int(result[1])
    passos.append(r_limpo)
    numero.append(num)    



plt.plot(numero, passos, "r--")
plt.show()
