from random import randint
import time

#funções "faz Subir" e "faz descer" basicamente movimentam no elevador!.
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

#Esse são as variações de grafico p/ cada andar(existe duas variações p/ cada).
#2 funções p/ cada Grafico.
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

# essa função monta os graficos andar por andar, e mostra na tela.
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

elevador = [1, 0, 0, 0, 0]  #os indices repesentão os andares.Por aqui rastreamos o elevador.
pessoas_no_elevador = 0    #quantidade de pessoas no elevador(usado p integagir com a interface).
verif_entrada_dequem_sobe = [] #andar atual das pessoas q vão subir(entram no elevador, p/ subir).
verif_saida_dequem_sobe = []  #andar onde as pessoas q querem subir vão sair(saem do elevador apos ele ter descido).
verif_entrada_dequem_desce = []  #andar atual das pessoas q querem descer(entram no elevador p/ descer).
verif_saida_dequem_desce = []  #andar onde as pessoas q querem descer vão sair(saem do elevador apos ele descer).
destinos = [5, 0, 0, 0, 0] # onde é armazenado os requisitos que foram gerados aleatoriamente.
localizacao_elevador = 0 #Localização atual do elevador(precisa ser atualizada apos alteração na lista "elevador").
comando_paradas_subidas = []  #paradas onde elevador vai tanto p alguem entrar ou sair(só p pessoas q estão subindo).
comando_paradas_descidas = []  #paradas onde elevador vai tanto p alguem entrar ou sair(só p pessoas q estão descendo).
sequencia_1 = [] # pode conter "comando_paradas_subidas" ou "comando_paradas_descidas",mas numca sera igual a Sequencia2.
sequencia_2 = [] # pode conter "comando_paradas_subidas" ou "comando_paradas_descidas",mas numca sera igual a Sequencia1.
subidas = "" #armazena TODOS os andares onde as pessoas entram, tanto de subida quando de descida.
descidas = ""  #armazena TODOS os andares onde as pessoas saem, tanto de subida quando de descida.
icone = "\U0001F468" # icone q aparece no grafico.
versao = '\U00002699' + "V3.0 GOLD" # icone de engrenagem e nº de versão. :)
mais_uma_volta = "s"  # usado p/ descidir se o codigo rodará mais uma vez.

#Abaixo está apenas o calheçalho.
print("\n", str(" " * 15) + "UNIVERSIDADE FERAL DO PARÁ \n " + str(
    " " * 7) + "Instituto de Ciências Exatas e Naturais\n" + str(
    " " * 6) + "Curso Bacharelado em Sistemas De Informação\n" + str(" " * 15) + "Programação de Computadores I \n")
print("Docente: Prof. Dr. Vinicius Augusto Carvalho de Abreu")
print("Discentes: Israel Pinheiro da Silva         Mat: 201911140005\n" + str(" " * 11) + "Inaldo da Silva Costa" + str(
    " " * 17) + "201911140036")
apresentar = str(input("      Pressione Enter p/ iniciar a apresentação!"))


if apresentar != "n" or apresentar != "N":
    #esse for é um bloco de interface de carregamento(só p/ ficar mais interessante).
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

    #esse for geram pessoas requisitando o elevador(sendo q não é posivel ter alguem no terroe nessa 1º rodada).
    #tambem nao é possivel alguem pedir p/ ir em um andar q já está.
    for d in range(1, 5):
        while True:
            destinos[d] = randint(0, 5)
            if destinos[d] != d:
                break

    #esse for pega todos os andares onde as pessoa vao antrar e sair do elevador p/ depois informar na interface.
    for i in range(5):
        if destinos[i] != 5:
            subidas += str(i) + "º "
            descidas += str(destinos[i]) + "º "

    #esse for minera os dados e separa onde otimiza a rotina do elevador.
    # EX: ele não vai colocar uma pessoa q quer descer na fila das q estão subindo.
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

    # nas proximas linhas nos aorganizamos em orde crescente.
    # SENDO QUE pela lógica a lista das pessoas q vao descer deve ser invertida.
    comando_paradas_subidas = sorted(comando_paradas_subidas)
    verif_entrada_dequem_sobe = sorted(verif_entrada_dequem_sobe)
    verif_saida_dequem_sobe = sorted(verif_saida_dequem_sobe)
    comando_paradas_descidas = sorted(comando_paradas_descidas, reverse=True)
    verif_entrada_dequem_desce = sorted(verif_entrada_dequem_desce)
    verif_saida_dequem_desce = sorted(verif_saida_dequem_desce)

    # aqui monstro o elevador a 1º vez antes de se movimenta, e ja aproveito p mostrar tbm os andes q ele vai.
    # e tambem passa informaçoes p interagir na interface.
    grafico_atual(pessoas_no_elevador,localizacao_elevador, subidas, descidas)
    time.sleep(3)
    print("\n" * 40)

    #aqui começa a rodada.
    while mais_uma_volta == "S" or mais_uma_volta == "s":

        #esse IF's antes do for descidem se é melhor pegar 1º a galera q vai subir ou q vai descer.
        #EX: se ele tiver no 4º é melhor ir pegando a galera q quer descer.
        # SE ele tiver no meio tanto faz, mas setei assim: 1º a galera q sobe e 2º a galera q desce.
        if localizacao_elevador == 2:
            sequencia_1 = comando_paradas_subidas
            sequencia_2 = comando_paradas_descidas
        elif localizacao_elevador <= 1:
            sequencia_1 = comando_paradas_subidas
            sequencia_2 = comando_paradas_descidas
        elif localizacao_elevador <= 3:
            sequencia_1 = comando_paradas_descidas
            sequencia_2 = comando_paradas_subidas

        #neste 1º FOR o elevador se desloca p/ o seu primro destinos da lista, e atualiza isso na tela.
        # OBS: ele só sai do IF quando chega no destino em questão.
        for i in range(len(sequencia_1)):

            #OBS: CASO O ELEVADOR JÁ ESTEJA NO ANDAR ONDE ALGUEM VAI SUBIR, O "IF" E O "ELIF" A SEGUIR SÃO IGUINORADOS
            #     E A EXEUÇÃO DO COFIGO PARTE P/ VERIFICAÇÃO DE ENTRADA DE PESSOAS.

            #esse IF se trata de quando o elevador esta acima do destino e prescisa descer.
            if comando_paradas_subidas[i] < localizacao_elevador:
                while localizacao_elevador != comando_paradas_subidas[i]:
                    faz_descer()
                    for cd in range(5):
                        if elevador[cd] == 1:
                            localizacao_elevador = cd
                    #chamando função de garfico atual ele atualiza o elevador na tela.
                    # e tambem passa informaçoes p interagir na interface.
                    grafico_atual(pessoas_no_elevador,localizacao_elevador, subidas, descidas)
                    time.sleep(0.85)
                    print("\n" * 40)

            #esse ELIF se trata de quando o elevadoe esta abaixo do seu destino e ele prescisa subir)
            elif comando_paradas_subidas[i] > localizacao_elevador:
                while comando_paradas_subidas[i] != localizacao_elevador:
                    faz_subir()
                    for cd in range(5):
                        if elevador[cd] == 1:
                            localizacao_elevador = cd
                    # chamando função de garfico atual ele atualiza o elevador na tela.
                    #e tambem passa informaçoes p interagir na interface.
                    grafico_atual(pessoas_no_elevador, localizacao_elevador, subidas, descidas)
                    time.sleep(0.85)
                    print("\n" * 40)

            #aqui é onde verificamos nos nossos dados se é o andar de entrada ou de saida das pessoas.
            #Se for a pessoas entra ou desce, e essa informção é excluida do banco de dados p evitar confução em
            # consultas futuras.
            #OBS: depois de cada entrada ou saida, o grafico é atualizado na tela p mostrar a ação da pessoas.
            if localizacao_elevador == comando_paradas_subidas[i]:

                #IF de verificação de entrada de pessoas.
                if comando_paradas_subidas[i] in verif_entrada_dequem_sobe:
                    pessoas_no_elevador += 1
                    verif_entrada_dequem_sobe.remove(comando_paradas_subidas[i])
                    grafico_atual(pessoas_no_elevador,localizacao_elevador, subidas, descidas)
                    time.sleep(3)
                    print("\n" * 40)
                #IF de verificação de saida des pessoas.
                if comando_paradas_subidas[i] in verif_saida_dequem_sobe:
                    pessoas_no_elevador -= 1
                    verif_saida_dequem_sobe.remove(comando_paradas_subidas[i])
                    grafico_atual(pessoas_no_elevador, localizacao_elevador, subidas, descidas)
                    time.sleep(3)
                    print("\n" * 40)

        #A logica do bloco a segui é basicamente a mesma do anterior. porem o elevador sempre faz o movimento contrario.
        #EXEMPLO: se antes ele estava pegando a galera q iria subir, agora ele vai pegar a galera q quer descer.
        for i in range(len(sequencia_2)):

            # OBS: CASO O ELEVADOR JÁ ESTEJA NO ANDAR ONDE ALGUEM VAI SUBIR, O "IF" E O "ELIF" A SEGUIR SÃO IGUINORADOS
            #     E A EXEUÇÃO DO COFIGO PARTE P/ VERIFICAÇÃO DE ENTRADA DE PESSOAS.

            #esse IF se trata de quando o elevador esta acima do destino e precisa descer.
            if comando_paradas_descidas[i] < localizacao_elevador:
                while localizacao_elevador != comando_paradas_descidas[i]:
                    faz_descer()
                    for cd in range(5):
                        if elevador[cd] == 1:
                            localizacao_elevador = cd
                    grafico_atual(pessoas_no_elevador, localizacao_elevador, subidas, descidas)
                    time.sleep(0.85)
                    print("\n" * 40)
            #esse ELIF se trata de quando o elevador esta abaixo do destino e precisa subir.
            elif comando_paradas_descidas[i] > localizacao_elevador:
                while comando_paradas_descidas[i] != localizacao_elevador:
                    faz_subir()
                    for cd in range(5):
                        if elevador[cd] == 1:
                            localizacao_elevador = cd
                        grafico_atual(pessoas_no_elevador, localizacao_elevador, subidas, descidas)
                        time.sleep(0.85)
                        print("\n" * 40)

            if localizacao_elevador == comando_paradas_descidas[i]:
                # IF de verificação de entrada de pessoas.
                if comando_paradas_descidas[i] in verif_entrada_dequem_desce:
                    pessoas_no_elevador += 1
                    verif_entrada_dequem_desce.remove(comando_paradas_descidas[i])
                    grafico_atual(pessoas_no_elevador, localizacao_elevador, subidas, descidas)
                    time.sleep(3)
                    print("\n" * 40)

                # IF de verificação de saida des pessoas.
                if comando_paradas_descidas[i] in verif_saida_dequem_desce:
                    pessoas_no_elevador -= 1
                    verif_saida_dequem_desce.remove(comando_paradas_descidas[i])
                    grafico_atual(pessoas_no_elevador, localizacao_elevador, subidas, descidas)
                    time.sleep(3)


        #Nesse momento a rodada terminou, todo mundo fou p seus lugares, e o usurio descidira se vai rodar mais uma vez.
        mais_uma_volta = str(input("quer dar mais muma volta?"))

        #Aqui é a preparação p a proxima rodada, essa preparação so é feita se for mesmo ter uma proxima(isso otipmiza
        # o codigo, evitando geração de dados q nao seram usados).
        if mais_uma_volta != "n" or mais_uma_volta != "N":
            #Aqui se zera variaves, para serem usadas na proxima rodada.
            destinos = [5, 5, 5, 5, 5]
            subidas = ""
            descidas = ""
            comando_paradas_subidas.clear()
            comando_paradas_descidas.clear()
            verif_entrada_dequem_desce.clear()
            verif_entrada_dequem_sobe.clear()
            verif_saida_dequem_desce.clear()
            verif_saida_dequem_sobe.clear()

            #E aqui eu gero os dados p/ proxima rodada e faço tambem todo a mineração e seleção das informações.
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

print("ENCERRADO")
