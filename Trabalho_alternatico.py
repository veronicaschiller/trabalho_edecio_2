import random
import os

NUM_COLUNA = 6
NUM_LINHAS = 7
bombas = 3
jogo = []


def tabuleiro():
    print()
    print("+----------------+")
    for i, linhas in enumerate(jogo, start=1):
        print(f"{i} | ", end=" ")
        for casa in linhas:
            print(f"{casa}", end=" ")
        print("|")
    print("+----------------+")
    for i in range(bombas):
        i, b = random.randint(0, NUM_LINHAS-1), random.randint(0, NUM_COLUNA-1)
    while tabuleiro[i][b] == -1:
        i, b = random.randint(0, NUM_LINHAS-1), random.randint(0, NUM_COLUNA-1)
        tabuleiro[i][b] = -1
    for i in range(NUM_LINHAS):
        for b in range(NUM_COLUNA):
            if tabuleiro[i][b] == -1:
                continue
            for bomb in [-1, 0, 1]:
                for bombs in [-1, 0, 1]:
                    if i+bomb < 0 or i+bomb >= NUM_LINHAS or b+bombs < 0 or b+bombs >= NUM_COLUNA:
                        continue
                    if tabuleiro[i+bomb][b+bombs] == -1:
                        tabuleiro[i][b] += 1


def cria_jogo():
    for i in range(NUM_LINHAS):
        jogo.append([])
        for _ in range(NUM_COLUNA):
            jogo[i].append("#")

    


def cria_csv():
    if not os.path.isfile("Ranking.csv"):
        return


with open('Ranking.csv', 'r') as arq:
    linhas = arq.readlines()

cria_jogo()
tabuleiro()
