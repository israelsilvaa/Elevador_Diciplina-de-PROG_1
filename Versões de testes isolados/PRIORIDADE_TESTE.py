from random import randint

requisitos_stts_subida = []  #galera q vai subir.   ex: ir do 1º p 3º
destinos_stts_subida = []    #destino de descida da galera q vai subir.  ex: ele vai p 3º
requisitos_stts_descida = []  #galera q vai descer.  ex: ir do 2º p 1º.
destinos_stts_descida = []   #destino de decida da galera q vai descer. ex: ele vai p 1º.
elevador = [1, 0, 0, 0, 0]
pessoas_no_elevador = 0

destinos = [5, 0, 0, 0, 0]
for d in range(1, 5):
    while True:
        destinos[d] = randint(0, 5)
        if destinos[d] != d:
            break
print(destinos)

for i in range(5):
    if destinos[i] != 5 and destinos[i] > i:
        requisitos_stts_subida.append(i)
        destinos_stts_subida.append(destinos[i])
    if destinos[i] != 5 and destinos[i] < i:
        requisitos_stts_descida.append(i)
        destinos_stts_descida.append(destinos[i])

print("subidas")
print(requisitos_stts_subida)
print("destino dessas pessoa q vão subir(respectivamente)")
print(destinos_stts_subida)
print("=========================================")
print("descidas")
print(requisitos_stts_descida)
print("destino das pessoas q vão descer(respectivamente)")
print(destinos_stts_descida)


