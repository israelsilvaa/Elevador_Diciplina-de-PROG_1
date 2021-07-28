from random import randint
import time
elevador = [1, 0, 0, 0, 0]
pessoas_no_elevador = 0
verif_entrada_dequem_sobe = []
verif_saida_dequem_sobe = []
verif_entrada_dequem_desce = []
verif_saida_dequem_desce = []
destinos = [2, 3, 3, 0, 5]
status = 1
localizacao_elevador = 0
comando_paradas_subidas = []
comando_paradas_descidas = []
sequencia_1 = []
sequencia_2 = []

def faz_subir():
    if elevador[3] == 1:
        elevador[3] = 0
        elevador[4] = 1
    if elevador[2] == 1:
        elevador[2] = 0
        elevador[3] = 1
    if elevador[1] == 1:
        elevador[1] = 0
        elevador[2] = 1
    if elevador[0] == 1:
        elevador[0] = 0
        elevador[1] = 1
def faz_descer():
    if elevador[1] == 1:
        elevador[1] = 0
        elevador[0] = 1
    if elevador[2] == 1:
        elevador[2] = 0
        elevador[1] = 1
    if elevador[3] == 1:
        elevador[3] = 0
        elevador[2] = 1
    if elevador[4] == 1:
        elevador[4] = 0
        elevador[3] = 1
for d in range(1, 5):
    while True:
        destinos[d] = randint(0, 5)
        if destinos[d] != d:
            break
print(destinos)
for i in range(5):
    if destinos[i] != 5 and destinos[i] > i:
        comando_paradas_subidas.append(i)
        comando_paradas_subidas.append(destinos[i])
        verif_entrada_dequem_sobe.append(i)
        verif_saida_dequem_sobe.append(destinos[i])
    if destinos[i] != 5 and destinos[i] < i:
        comando_paradas_descidas.append(i)
        comando_paradas_descidas.append(destinos[i])
        verif_entrada_dequem_desce.append(i)
        verif_saida_dequem_desce.append(destinos[i])
comando_paradas_subidas = sorted(comando_paradas_subidas)
verif_entrada_dequem_sobe = sorted(verif_entrada_dequem_sobe)
verif_saida_dequem_sobe = sorted(verif_saida_dequem_sobe)
comando_paradas_descidas = sorted(comando_paradas_descidas, reverse=True)
verif_entrada_dequem_desce = sorted(verif_entrada_dequem_desce)
verif_saida_dequem_desce = sorted(verif_saida_dequem_desce)

print("subidas")
print(verif_entrada_dequem_sobe)
print("descidas")
print(verif_saida_dequem_sobe)
print("comando geral de subida:", comando_paradas_subidas)
print("==================")
print("subidas")
print(verif_entrada_dequem_desce)
print("descidas")
print(verif_saida_dequem_desce)
print("comando_paradas_descidas", comando_paradas_descidas)

x = "s"
while x == "S" or x == "s":
    print("COMEÇO DO COLCO")
    if localizacao_elevador == 2:
        sequencia_1 = comando_paradas_subidas
        sequencia_2 = comando_paradas_descidas
    elif localizacao_elevador <= 1:
        sequencia_1 = comando_paradas_subidas
        sequencia_2 = comando_paradas_descidas
    elif localizacao_elevador <= 3:
        sequencia_1 = comando_paradas_descidas
        sequencia_2 = comando_paradas_subidas

    for i in range(len(sequencia_1)):
        if comando_paradas_subidas[i] < localizacao_elevador:
            while localizacao_elevador != comando_paradas_subidas[i]:
                faz_descer()
                for cd in range(5):
                    if elevador[cd] == 1:
                        localizacao_elevador = cd
        elif comando_paradas_subidas[i] > localizacao_elevador:
            while comando_paradas_subidas[i] != localizacao_elevador:
                faz_subir()
                for cd in range(5):
                    if elevador[cd] == 1:
                        localizacao_elevador = cd

        print("localização do elevador:", localizacao_elevador)
        if localizacao_elevador == comando_paradas_subidas[i]:
            print("localização do elevador:", localizacao_elevador)
            if comando_paradas_subidas[i] in verif_entrada_dequem_sobe:
                pessoas_no_elevador += 1
                verif_entrada_dequem_sobe.remove(comando_paradas_subidas[i])
                print("entrou + um!")
            if comando_paradas_subidas[i] in verif_saida_dequem_sobe:
                pessoas_no_elevador -= 1
                verif_saida_dequem_sobe.remove(comando_paradas_subidas[i])
                print("desceu uma aqui!")
    print("pessoas:", pessoas_no_elevador)
    time.sleep(3)
    for i in range(len(sequencia_2)):
        if comando_paradas_descidas[i] < localizacao_elevador:
            while localizacao_elevador != comando_paradas_descidas[i]:
                faz_descer()
                for cd in range(5):
                    if elevador[cd] == 1:
                        localizacao_elevador = cd
        elif comando_paradas_descidas[i] > localizacao_elevador:
            while comando_paradas_descidas[i] != localizacao_elevador:
                faz_subir()
                for cd in range(5):
                    if elevador[cd] == 1:
                        localizacao_elevador = cd

        print("localização do elevador:", localizacao_elevador)
        if localizacao_elevador == comando_paradas_descidas[i]:
            print("localização do elevador:", localizacao_elevador)
            if comando_paradas_descidas[i] in verif_entrada_dequem_desce:
                pessoas_no_elevador += 1
                verif_entrada_dequem_desce.remove(comando_paradas_descidas[i])
                print("entrou + um!")
            if comando_paradas_descidas[i] in verif_saida_dequem_desce:
                pessoas_no_elevador -= 1
                verif_saida_dequem_desce.remove(comando_paradas_descidas[i])
                print("desceu uma aqui!")
    print("pessoas:", pessoas_no_elevador)
    time.sleep(3)
    x = str(input("quer dar mais muma volta?"))
    destinos = [5, 5, 5, 5, 5]
    comando_paradas_subidas.clear()
    comando_paradas_descidas.clear()
    verif_entrada_dequem_desce.clear()
    verif_entrada_dequem_sobe.clear()
    verif_saida_dequem_desce.clear()
    verif_saida_dequem_sobe.clear()
    for d in range(5):
        while True:
            destinos[d] = randint(0, 5)
            if destinos[d] != d:
                break
    for i in range(5):
        if destinos[i] != 5 and destinos[i] > i:
            comando_paradas_subidas.append(i)
            comando_paradas_subidas.append(destinos[i])
            verif_entrada_dequem_sobe.append(i)
            verif_saida_dequem_sobe.append(destinos[i])
        if destinos[i] != 5 and destinos[i] < i:
            comando_paradas_descidas.append(i)
            comando_paradas_descidas.append(destinos[i])
            verif_entrada_dequem_desce.append(i)
            verif_saida_dequem_desce.append(destinos[i])
    comando_paradas_subidas = sorted(comando_paradas_subidas)
    verif_entrada_dequem_sobe = sorted(verif_entrada_dequem_sobe)
    verif_saida_dequem_sobe = sorted(verif_saida_dequem_sobe)
    comando_paradas_descidas = sorted(comando_paradas_descidas, reverse=True)
    verif_entrada_dequem_desce = sorted(verif_entrada_dequem_desce)
    verif_saida_dequem_desce = sorted(verif_saida_dequem_desce)
    print(destinos)
    print("comando_paradas_subidas", comando_paradas_subidas)
    print("comando_paradas_descidas", comando_paradas_descidas)

print("terminou a volta!")
print("localizacao_elevador", localizacao_elevador)