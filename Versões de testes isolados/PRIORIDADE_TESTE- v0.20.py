from random import randint
from typing import List, Any, Union

requisitos_stts_subida = []  #galera q vai subir.   ex: ir do 1º p 3º
destinos_stts_subida = []    #destino de descida da galera q vai subir.  ex: ele vai p 3º
requisitos_stts_descida = []  #galera q vai descer.  ex: ir do 2º p 1º.
destinos_stts_descida = []   #destino de decida da galera q vai descer. ex: ele vai p 1º.
elevador = [1, 0, 0, 0, 0]
pessoas_no_elevador = 0

geral_subida = []
geral_descida = []

destinos = [5, 0, 0, 0, 0]
for d in range(1, 5):
    while True:
        destinos[d] = randint(0, 5)
        if destinos[d] != d:
            break
print(destinos)

for i in range(5):
    if destinos[i] != 5 and destinos[i] > i:
        geral_subida.append(i)
        geral_subida.append(destinos[i])
    if destinos[i] != 5 and destinos[i] < i:
        geral_descida.append(i)
        geral_descida.append(destinos[i])

geral_subida = sorted(geral_subida)
geral_descida = sorted(geral_descida, reverse=True)
print("subidas")
print(geral_subida)
print("=========================================")
print("descidas")
print(geral_descida)


