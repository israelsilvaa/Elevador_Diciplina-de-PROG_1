from random import randint
import time


# Variação de grafico para cada andar.
def piso4x(n):
    print(
        '_____ \n!   ! 4º Andar    (VOCÊ ESTÁ AQUI!)\n!' + str(
            '\U0001F574' * n) + '! \n===== ')


def piso4():
    print(
        '_____ \n!   ! 4º Andar \n!   !\n=====')


def piso3x(n):
    print('_____\n!    ! 3º Andar    (VOCÊ ESTÁ AQUI!)\n!' + str('\U0001F574' * n) + '! \n===== ')


def piso3():
    print('_____\n!   ! 3º Andar        \n!   !\n=====')


def piso2x(n):
    print('_____\n!    ! 2º Andar    (VOCÊ ESTÁ AQUI!)\n!' + str('\U0001F574' * n) + '! \n===== ')


def piso2():
    print('_____\n!   ! 2º Andar\n!   !\n=====')


def piso1x(n):
    print('_____\n!    ! 1º Andar    (VOCÊ ESTÁ AQUI!)\n!' + str('\U0001F574' * n) + '! \n===== ')


def piso1():
    print('_____\n!   ! 1º Andar\n!   !\n=====')


def terreox(n):
    print('_____\n!    ! Terreo    (VOCÊ ESTÁ AQUI!)\n!' + str('\U0001F574' * n) + '! \n=====                                    ## Express Elevadores ##' + str(v))


def terreo():
    print('_____\n!   ! Terreo    \n!   !\n=====                                    ## Express Elevadores ## ' + str(v))


# essa função monta os graficos andar por andar, e mostra na tela
def grafico_atual(n):
    if elevador[4] == 1:
        piso4x(n)
    else:
        piso4()
    if elevador[3] == 1:
        piso3x(n)
    else:
        piso3()
    if elevador[2] == 1:
        piso2x(n)
    else:
        piso2()
    if elevador[1] == 1:
        piso1x(n)
    else:
        piso1()
    if elevador[0] == 1:
        terreox(n)
    else:
        terreo()


pessoas_no_elevador = 0  # usado para interagir com os graficos de andares
n = 0  # usado para interagir com as funções
elevador = [1, 0, 0, 0, 0]
loc_e = int(0)  # localização do elevador exata.
dc = 0  # estas são variaveis p/ controlar a entrada de pessoas no elevador
dc2 = 0  # estas são variaveis p/ controlar a entrada de pessoas no elevador
pedidos = 0  # Quatidade de vezes que o elevador foi requisitado.
andar_vazio = 0
v = "V1.075 Alpha"
# Este bloco localiza onde está o elevador na minha lista "elevador".
for i in range(5):
    if elevador[i] == 1:
        loc_e = i

# Gera os destinos para losta de destinos, mas ainda não sao comandos, exatamente.
# OBS:esse bloco nao permite que alguem peça p/ ir do 4º p/ 4º. Pois é incoerente.
destinos = [5, 0, 0, 0, 0]
for d in range(1, 5):
    while True:
        destinos[d] = randint(0, 5)
        if destinos[d] != d:
            break

# Este bloco seleciona os andares onde o elevador foi chamado.
dest_elevador = []
dest_pessoas = []
for i in range(5):
    if destinos[i] != 5:
        dest_elevador.append(i)
        dest_pessoas.append(destinos[i])
        pedidos += 1

for i in range(1, 101, 3):
    print("Carregando " + str(i) + "%." + 73 * " " + v)
    print("." * i)
    time.sleep(0.1)
    print("\n" * 50)
if i == 100:
    print("OK!")
    print("Carregamento bem sucedido!                 Seja Bem Vindo  :)" + 27 * " " + v)
    print("." * i)
    time.sleep(5)
print("\n" * 50)

grafico_atual(n)  # esta função mostra o grafico atual dos andares
print("Andares solicitados:" + str(dest_elevador))
print("Pessoas no elevador:" + str(pessoas_no_elevador))
time.sleep(3)
print("\n" * 40)

# Aqui começa o processo de subir ou descer , para cada destino da lista "des_elevador".
uma_volta = "s"
while uma_volta == "s":
    for i in range(len(dest_elevador)):
        # esse 2º while roda um bloco ate o elevador chegar ao destino dele, seja p/ cima ou baixo.

        if loc_e == dest_elevador[i]:
            pessoas_no_elevador += 1

        while loc_e != dest_elevador[i]:

            # Essse if se trata de quando e elevador presisa subir.
            if loc_e < dest_elevador[i]:
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

                # apos subir ele mostra o grafico dele.
                grafico_atual(pessoas_no_elevador)
                print("destinos do elevador:" + str(dest_elevador))
                print("Pessoas no elevador:" + str(pessoas_no_elevador))
                time.sleep(0.85)

                # esse bloco atualiza a posição exata do elevador p/ ser comparado depois na proxima rodada.Pois caso ele
                for ab in range(5):  # nao tenha chegado no seu destino , vai ter q subir um andar ate chegar.
                    if elevador[ab] == 1:
                        loc_e = ab

                # ===================================================
                print("Localização atual do elevador:" + str(loc_e))
                # depois podemos fazer um painel p mostrar a localização p pessoas, utilizando essa variavel.
                # aqui so é executado quando o elevador chega no seu destino, entao a pessoa q o chamou pode subir.
                # Coloquei um time de maior p pessoa poder subir, e assim fica mis facil de entender oq ta
                # contecendo, e + realista tbm!
                # ==================================================

                if loc_e == dest_elevador[i]:
                    time.sleep(3)
                    pessoas_no_elevador += 1
                    print(" " * 50)

            # Aqui ja é SE CASO ele tenha q DESCER! o resto repete praticamente.
            elif loc_e > dest_elevador[i]:
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
                grafico_atual(pessoas_no_elevador)

                # essa variavel "dc" , é p autorizar uma pessoa a subir
                # Tive q deixar mais rigiroso , POIS AS VEZES DUAS PESSOAS SUBIAM DE UMA VEZ(oq nao pode acontecer)
                if loc_e == dest_elevador[i]:
                    dc = 1

                print("destinos do elevador:" + str(dest_elevador))
                print("Pessoas no elevador:" + str(pessoas_no_elevador))
                time.sleep(0.85)

                # Aqui é sobre atualização exata do elevador, de novo
                # eu tive q usar a "cd" p/ controlar o for, p diferenciar uns dos outros.
                for cd in range(5):
                    if elevador[cd] == 1:
                        loc_e = cd

                print("Localização atual do elevador:" + str(loc_e))

                # ESSA É A PARTE Q EU FALEI SOBRE SER RIGOROSO NA SUBIDA DE PESSOAS.
                if loc_e == dest_elevador[i]:
                    if dc > 0 or loc_e == 1 or dc2 == 1:
                        pessoas_no_elevador += 1
                        time.sleep(3)

    grafico_atual(pessoas_no_elevador)
    if (len(dest_elevador)) == False:
        print("Todos os andadres vazios no momento!")
    print("Pessoas no elevador:" + str(pessoas_no_elevador))
    uma_volta = str(input("Quer dar mais uma volta(s/n)?"))  # AQUI TERMINA A VOLTA

    # aqui tenho q zerar algumas variaveis p/ usar na proxima volta.
    if uma_volta == "s":
        dc = 0
        dc2 = 0
        reverso = 0
        print("\n" * 50)

    # Aqui eu já gero os destinos da proxima rodada.
    dest_elevador = []
    for d in range(0, 5):
        destinos[d] = randint(0, 5)
        while True:
            destinos[d] = randint(0, 5)
            if destinos[d] != d:
                break

    # Aqui eu seleciono os destinos DO elevador.
    for i in range(5):
        if destinos[i] != 5:
            dest_elevador.append(i)
            pedidos += 1

    if loc_e == 4:
        dest_elevador = sorted(dest_elevador, reverse=True)

print("Localização final do elevador:" + str(loc_e))
print("Quantidade de pessoas no elevador:" + str(pessoas_no_elevador))
