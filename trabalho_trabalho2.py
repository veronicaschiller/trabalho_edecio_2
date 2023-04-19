import random

NUM_LINHAS= 5
NUM_COLUNAS =5
NUM_BOMBAS = 3

jogo = []

def cria_csv ():
    pass

def cria_tabuleiro ():
    tabuleiro = []
    for i in range(NUM_COLUNAS):
        i.appende(NUM_LINHAS)
        for n in range(NUM_COLUNAS):
            n.append(NUM_COLUNAS(0))
    tabuleiro.append(NUM_LINHAS)
    minas = []
    while len(minas) < NUM_BOMBAS:
        mina = [random.randint(0, NUM_LINHAS-1), random.randint(0, NUM_COLUNAS-1)]
        if mina not in minas:
            minas.append(mina)
            tabuleiro[mina[0]][mina[1]] = "x"
    return tabuleiro 


def cria_jogo():
    pass

cria_tabuleiro()