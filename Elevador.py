from random import randint
import time

print("\n", str(" " * 15) + "UNIVERSIDADE FERAL DO PARÁ \n " + str(
    " " * 7) + "Instituto de Ciências Exatas e Naturais\n" + str(
    " " * 6) + "Curso Bacharelado em Sistemas De Informação\n" + str(" " * 15) + "Programação de Computadores I \n")
print("Docente: Vinicius Augusto Carvalho de Abreu")
print("Discentes: Israel Pinheiro da Silva         Mat: 201911140005\n" + str(" " * 11) + "Inaldo da Silva Costa" + str(
    " " * 17) + "201911140036 \n" + str(" " * 11) + "Erick Andersen Guedes Cardoso         201911140012\n")

x = str(input("      Pressione Enter p/ iniciar a apresentação!"))

if x != "n" or "N":

    # Variação de grafico para cada andar.
    def piso4x(n, a=0):
        if n == 0:
            a = 3
        elif n == 1:
            a = 2
        print(
            '##### \n!   ! 4º Andar    \n!' + str(icone * n) + str(" " * a) + '! \n##### ' + str(
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


    def piso2x(pessoas, a=0):
        if pessoas == 0:
            a = 3
        elif pessoas == 1:
            a = 2
        print('#####\n!   ! 2º Andar    \n!' + str(icone * pessoas) + str(" " * a) + '! \n##### ')


    def piso2():
        print('_____\n!   ! 2º Andar\n!   !\n=====')


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
    def grafico_atual(pessoas, p):
        if elevador[4] == 1:
            piso4x(pessoas)
        else:
            piso4()
        if elevador[3] == 1:
            piso3x(pessoas)
        else:
            piso3(pessoas)
        if elevador[2] == 1:
            piso2x(pessoas)
        else:
            piso2()
        if elevador[1] == 1:
            piso1x(pessoas)
        else:
            piso1()
        if elevador[0] == 1:
            terreox(pessoas)
        else:
            terreo()


    pessoas_no_elevador = 0  # usado para interagir com os graficos de andares
    elevador = [1, 0, 0, 0, 0]  # Usado p/ identificar localização so elevador.
    localizacao_elevador = int(0)  # localização do elevador exata.
    dc = 0  # estas são variaveis p/ controlar a entrada de pessoas no elevador
    dc2 = 0  # estas são variaveis p/ controlar a entrada de pessoas no elevador
    aux = 0  # usado p/ troca de valores quando a lista é invertida.
    icone = "\U0001F468"
    versao = '\U00002699' + " V2.46 BETA"

    # Este bloco localiza onde está o elevador na minha lista "elevador".
    for i in range(5):
        if elevador[i] == 1:
            localizacao_elevador = i

    # Gera os destinos para losta de destinos, mas ainda não sao comandos, exatamente.
    # OBS:esse bloco nao permite que alguem peça p/ ir do 4º p/ 4º. Pois é incoerente.
    destinos = [5, 0, 0, 0, 0]
    for d in range(1, 5):
        while True:
            destinos[d] = randint(0, 5)
            if destinos[d] != d:
                break

    # Este bloco seleciona os andares onde o elevador foi chamado.
    destino_elevador = []
    destino_pessoas = []
    subidas = ""
    descidas = ""
    for i in range(5):
        if destinos[i] != 5:
            destino_elevador.append(i)
            subidas += str(i) + "º "
            destino_elevador.append(destinos[i])
            descidas += str(destinos[i]) + "º "

    # Bloco de interface.
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
    # esta função mostra o grafico atual dos andares
    grafico_atual(pessoas_no_elevador, localizacao_elevador)
    print("Andares solicitados:" + str(subidas))
    print("Andares de descida:" + str(descidas))
    print("Pessoas no elevador:" + str(pessoas_no_elevador))
    time.sleep(3)
    print("\n" * 40)

    # Aqui começa o processo de subir ou descer , para cada destino da lista "des_elevador".
    uma_volta = "s"
    while uma_volta == "s":
        for i in range(len(destino_elevador)):

            # aqui é verificado se tem uma pessoa no andar q o elevador parou depois da 1º volta.
            if localizacao_elevador == destino_elevador[i] and i % 2 == 0:
                pessoas_no_elevador += 1
                time.sleep(3)
                if localizacao_elevador == destino_elevador[i] and i % 2 != 0:
                    pessoas_no_elevador -= 1
                time.sleep(3)

            # esse 2º while roda um bloco ate o elevador chegar ao destino dele, seja p/ cima ou baixo.
            while localizacao_elevador != destino_elevador[i]:

                # Essse if se trata de quando e elevador presisa subir.
                if localizacao_elevador < destino_elevador[i]:
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
                    # esse bloco atualiza a posição exata do elevador p/ ser comparado depois na proxima rodada.Pois
                    # caso ele nao tenha chegado no seu destino , vai ter q subir um andar ate chegar.
                    for ab in range(5):
                        if elevador[ab] == 1:
                            localizacao_elevador = ab
                    # apos subir ele mostra o grafico dele.
                    grafico_atual(pessoas_no_elevador, localizacao_elevador)
                    print("Andares solicitados:" + str(subidas))
                    print("Andares de descida:" + str(descidas))
                    print("Pessoas no elevador:" + str(pessoas_no_elevador))
                    time.sleep(0.85)

                    # Aqui se decide se alguem sobre ou desce.
                    # Lembrando q na lista de comando, os indices pares são destinos de subida
                    # e os impares são destinos de descida.
                    if localizacao_elevador == destino_elevador[i] and i % 2 == 0:
                        time.sleep(3)
                        pessoas_no_elevador += 1
                    if localizacao_elevador == destino_elevador[i] and i % 2 != 0:
                        pessoas_no_elevador -= 1
                        time.sleep(3)
                    print(" " * 50)

                # Aqui ja é SE CASO ele tenha q DESCER! o resto repete praticamente.
                elif localizacao_elevador > destino_elevador[i]:
                    print(" " * 50)
                    dc2 = 1
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
                    # Aqui é sobre atualização exata do elevador, de novo
                    # eu tive q usar a "cd" p/ controlar o for, p diferenciar uns dos outros.
                    for cd in range(5):
                        if elevador[cd] == 1:
                            localizacao_elevador = cd

                    grafico_atual(pessoas_no_elevador, localizacao_elevador)

                    # essa variavel "dc" , é p autorizar uma pessoa a subir
                    # Tive q deixar mais rigiroso , POIS AS VEZES DUAS PESSOAS SUBIAM DE UMA VEZ(oq nao pode acontecer)
                    if localizacao_elevador == destino_elevador[i] and i % 2 == 0:
                        dc = 1

                    print("Andares solicitados:" + str(subidas))
                    print("Andares de descida:" + str(descidas))
                    print("Pessoas no elevador:" + str(pessoas_no_elevador))
                    time.sleep(0.85)

                    # ESSA É A PARTE Q EU FALEI SOBRE SER RIGOROSO NA SUBIDA DE PESSOAS.
                    if localizacao_elevador == destino_elevador[i] and i % 2 == 0:
                        if dc > 0 or localizacao_elevador == 1 or dc2 == 1:
                            pessoas_no_elevador += 1
                            time.sleep(3)
                    if localizacao_elevador == destino_elevador[i] and i % 2 != 0:
                        pessoas_no_elevador -= 1
                        time.sleep(3)

                print(" " * 50)

        grafico_atual(pessoas_no_elevador, localizacao_elevador)
        if not (len(destino_elevador)):
            print("Todos os andadres vazios no momento!")
        print("Andares solicitados:" + str(subidas))
        print("Andares de descida:" + str(descidas))
        print("Pessoas no elevador:" + str(pessoas_no_elevador))
        uma_volta = str(input("Quer dar mais uma volta(s/n)?"))  # AQUI TERMINA A VOLTA

        # aqui tenho q zerar algumas variaveis p/ usar na proxima volta.
        if uma_volta == "s":
            dc = 0
            dc2 = 0
            reverso = 0
            subidas = ""
            descidas = ""
            print("\n" * 50)

        # Aqui eu já gero os destinos da proxima rodada.
        destino_elevador = []
        for d in range(0, 5):
            while True:
                destinos[d] = randint(0, 5)
                if destinos[d] != d:
                    break

        # Aqui eu seleciono os destinos DO elevador.
        for i in range(5):
            if destinos[i] != 5:
                destino_elevador.append(i)
                subidas += str(i) + "º "
                destino_elevador.append(destinos[i])
                descidas += str(destinos[i]) + "º "

        if localizacao_elevador == 4:
            # comando abaixo inverte a lista de comandos de paradas, p/ que ele nao começe a pegar pessoas do andar
            # mais baixo.
            destino_elevador = destino_elevador[::-1]

            # Comando abaixo troca de lugar destino das pessoas e destinos do elevador(JA QUE O COMANDO ACIMA OD
            # INVERTEU ANTãO AGPRA ESTOU AGEITANDO isso prq , indices pares da lista, se referem a subida de pessoas
            # e indices impares a descida de pessoas
            for i in range(len(destino_elevador)):
                if i % 2 == 0:
                    aux = destino_elevador[i]
                    destino_elevador[i] = destino_elevador[i + 1]
                    destino_elevador[i + 1] = aux

    print("Quantidade de pessoas no elevador:" + str(pessoas_no_elevador))
