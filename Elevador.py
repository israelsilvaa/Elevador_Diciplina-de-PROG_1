from random import randint
import time

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
    # Variação de grafico para cada andar.
def piso4x(pessoas, a=0):
    if pessoas == 0:
        a = 3
    elif pessoas == 1:
        a = 2
    print(
        '##### \n!   ! 4º Andar    \n!' + str(icone * pessoas) + str(" " * a) + '! \n##### ' + str(
            " " * 41) + "Localização do Elevador")
def piso4():
    print(
        '_____ \n!   ! 4º Andar \n!   !\n=====' + str(" " * 41) + "Localização do Elevador")
def piso3x(pessoas, s=0, s2=0, a=0):
    if localizacao_elevador == 0:
        s = 1
        s2 = 29
    elif localizacao_elevador == 1:
        s = 7
        s2 = 23
    elif localizacao_elevador == 2:
        s = 35
        s2 = 16
    elif localizacao_elevador == 3:
        s = 21
        s2 = 8
    elif localizacao_elevador == 4:
        s = 28
        s2 = 2
    if pessoas == 0:
        a = 3
    elif pessoas == 1:
        a = 2
    print('#####' + str(" " * 36) + '+===============================+\n!   ! 3º Andar ' + str(
        " " * 26) + '| T  -  1º  -  2º  -  3º  -  4º |' '\n!' + str(icone * pessoas) + str(" " * a) + '!' + str(
        " " * 36) + "|" + str(" " * s) + 'X' + str(" " * s2) + ' |' '\n##### ' + str(
        " " * 35) + '+===============================+')


def piso3(s=0, s2=0):
    if localizacao_elevador == 0:
        s = 1
        s2 = 29
    elif localizacao_elevador == 1:
        s = 7
        s2 = 23
    elif localizacao_elevador == 2:
        s = 14
        s2 = 16
    elif localizacao_elevador == 3:
        s = 21
        s2 = 7
    elif localizacao_elevador == 4:
        s = 28
        s2 = 2

    print('_____' + str(" " * 36) + '+===============================+ \n!   ! 3º Andar' + str(
        " " * 27) + '| T  -  1º  -  2º  -  3º  -  4º |' '\n!   ! ' + str(" " * 35) + '|' + str(" " * s) + 'X' + str(
        " " * s2) + '| '  '\n=====' + str(" " * 36) + '+===============================+')


def piso2x(pessoas, subidaP,decidaP,a=0):
    if pessoas == 0:
        a = 3
    elif pessoas == 1:
        a = 2
    print('#####\n!   ! 2º Andar '+str(" "*32)+"Solicitações: "+str(subidaP)+'\n!' + str(icone * pessoas) + str(" "*a) + '!'+str(" "*45)+"Destinos: " + str(decidaP) + '\n#####' + str(" "*37) + "pessoas no elevador atualmente: "+str(pessoas))


def piso2(pessoas, subidaP, decidaP):
    print('_____\n!   ! 2º Andar'+str(" "*32)+"Solicitações: "+str(subidaP)+'\n!   !'+str(" "*45)+"Destinos: "+str(decidaP)+'\n====='+str(" "*37)+"pessoas no elevador atualmente: "+str(pessoas))


def piso1x(pessoas, a=0):
    if pessoas == 0:
        a = 3
    elif pessoas == 1:
        a = 2
    print('#####\n!   ! 1º Andar    \n!' + str(icone * pessoas) + str(" " * a) + '! \n##### ')


def piso1():
    print('_____\n!   ! 1º Andar\n!   !\n=====')


def terreox(pessoas, a=0):
    if pessoas == 0:
        a = 3
    elif pessoas == 1:
        a = 2
    print('#####\n!   ! Terreo    \n!' + str(icone * pessoas) + str(
        " " * a) + '! \n#####                                    ## Express Elevadores ##' + str(versao))


def terreo():
    print(
        '_____\n!   ! Terreo    \n!   !\n=====                                    ## Express Elevadores ## ' + str(
            versao))


# essa função monta os graficos andar por andar, e mostra na tela
def grafico_atual(pessoas,localizacao_elevador, subidas, descidas):
    if elevador[4] == 1:
        piso4x(pessoas)
    else:
        piso4()
    if elevador[3] == 1:
        piso3x(pessoas)
    else:
        piso3(pessoas)
    if elevador[2] == 1:
        piso2x(pessoas, subidas, descidas)
    else:
        piso2(pessoas, subidas, descidas)
    if elevador[1] == 1:
        piso1x(pessoas)
    else:
        piso1()
    if elevador[0] == 1:
        terreox(pessoas)
    else:
        terreo()

elevador = [1, 0, 0, 0, 0]
pessoas_no_elevador = 0
verif_entrada_dequem_sobe = []
verif_saida_dequem_sobe = []
verif_entrada_dequem_desce = []
verif_saida_dequem_desce = []
destinos = [2, 3, 3, 0, 5]
localizacao_elevador = 0
comando_paradas_subidas = []
comando_paradas_descidas = []
sequencia_1 = []
sequencia_2 = []
subidas = ""
descidas = ""
icone = "\U0001F468"
versao = '\U00002699' + " V2.95 BETA"
x = "s"

print("\n", str(" " * 15) + "UNIVERSIDADE FERAL DO PARÁ \n " + str(
    " " * 7) + "Instituto de Ciências Exatas e Naturais\n" + str(
    " " * 6) + "Curso Bacharelado em Sistemas De Informação\n" + str(" " * 15) + "Programação de Computadores I \n")
print("Docente: Prof. Dr. Vinicius Augusto Carvalho de Abreu")
print("Discentes: Israel Pinheiro da Silva         Mat: 201911140005\n" + str(" " * 11) + "Inaldo da Silva Costa" + str(
    " " * 17) + "201911140036")  #+ str(" " * 11) + "Erick Andersen Guedes Cardoso         201911140012\n")

apresentar = str(input("      Pressione Enter p/ iniciar a apresentação!"))
if apresentar != "n" or apresentar != "N":
    for i in range(1, 101, 3):
        print("Carregando " + str(i) + "%." + 73 * " " + versao)
        print("." * i)
        time.sleep(0.1)
        print("\n" * 50)
        if i == 100:
            print("OK!")
            print("Carregamento bem sucedido!                 Seja Bem Vindo  :)" + 27 * " " + versao)
            print("." * i)
            time.sleep(5)
    print("\n" * 50)

    for d in range(1, 5):
        while True:
            destinos[d] = randint(0, 5)
            if destinos[d] != d:
                break
    for i in range(5):
        if destinos[i] != 5:
            subidas += str(i) + "º "
            descidas += str(destinos[i]) + "º "

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

    grafico_atual(pessoas_no_elevador,localizacao_elevador, subidas, descidas)
    time.sleep(3)
    print("\n" * 40)

    while x == "S" or x == "s":
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
                    grafico_atual(pessoas_no_elevador,localizacao_elevador, subidas, descidas)
                    time.sleep(3)
                    print("\n" * 40)

            elif comando_paradas_subidas[i] > localizacao_elevador:
                while comando_paradas_subidas[i] != localizacao_elevador:
                    faz_subir()
                    for cd in range(5):
                        if elevador[cd] == 1:
                            localizacao_elevador = cd
                    grafico_atual(pessoas_no_elevador, localizacao_elevador, subidas, descidas)
                    time.sleep(3)
                    print("\n" * 40)

            if localizacao_elevador == comando_paradas_subidas[i]:
                if comando_paradas_subidas[i] in verif_entrada_dequem_sobe:
                    pessoas_no_elevador += 1
                    verif_entrada_dequem_sobe.remove(comando_paradas_subidas[i])
                    grafico_atual(pessoas_no_elevador,localizacao_elevador, subidas, descidas)
                    time.sleep(3)
                    print("\n" * 40)

                if comando_paradas_subidas[i] in verif_saida_dequem_sobe:
                    pessoas_no_elevador -= 1
                    verif_saida_dequem_sobe.remove(comando_paradas_subidas[i])
                    grafico_atual(pessoas_no_elevador, localizacao_elevador, subidas, descidas)
                    time.sleep(3)
                    print("\n" * 40)

        for i in range(len(sequencia_2)):
            if comando_paradas_descidas[i] < localizacao_elevador:
                while localizacao_elevador != comando_paradas_descidas[i]:
                    faz_descer()
                    for cd in range(5):
                        if elevador[cd] == 1:
                            localizacao_elevador = cd
                    grafico_atual(pessoas_no_elevador, localizacao_elevador, subidas, descidas)
                    time.sleep(3)
                    print("\n" * 40)

            elif comando_paradas_descidas[i] > localizacao_elevador:
                while comando_paradas_descidas[i] != localizacao_elevador:
                    faz_subir()
                    for cd in range(5):
                        if elevador[cd] == 1:
                            localizacao_elevador = cd
                        grafico_atual(pessoas_no_elevador, localizacao_elevador, subidas, descidas)
                        time.sleep(3)
                        print("\n" * 40)

            if localizacao_elevador == comando_paradas_descidas[i]:
                if comando_paradas_descidas[i] in verif_entrada_dequem_desce:
                    pessoas_no_elevador += 1
                    verif_entrada_dequem_desce.remove(comando_paradas_descidas[i])
                    grafico_atual(pessoas_no_elevador, localizacao_elevador, subidas, descidas)
                    time.sleep(3)
                    print("\n" * 40)

                if comando_paradas_descidas[i] in verif_saida_dequem_desce:
                    pessoas_no_elevador -= 1
                    verif_saida_dequem_desce.remove(comando_paradas_descidas[i])
                    grafico_atual(pessoas_no_elevador, localizacao_elevador, subidas, descidas)
                    time.sleep(3)
                    print("\n" * 40)

        grafico_atual(pessoas_no_elevador, localizacao_elevador, subidas, descidas)
        time.sleep(3)

        x = str(input("quer dar mais muma volta?"))
        destinos = [5, 5, 5, 5, 5]
        subidas = ""
        descidas = ""
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
            if destinos[i] != 5:
                subidas += str(i) + "º "
                descidas += str(destinos[i]) + "º "
        grafico_atual(pessoas_no_elevador, localizacao_elevador, subidas, descidas)
        time.sleep(3)
        print("\n" * 40)

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
