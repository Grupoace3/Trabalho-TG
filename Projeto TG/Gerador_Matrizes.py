from curses.ascii import isdigit
import random

# Gerar matrizes com linhas e colunas de tamanho distintos usando a lib random
def gerarMatriz():
    rows = random.randrange(1,5)
    columns = random.randrange(1,5)
    #print("É uma matrix de ordem "+str(rows)+" x "+str(columns))
    matriz = []
    for r in range(0,rows):
        matrizAux = []
        for c in range(0,columns):
            matrizAux.append(random.randrange(1,100))
        matriz.append(matrizAux)
    return matriz

#Escrever cada matriz em uma linha de um txt.  

arquivo = open("Matrizes.txt","w")

#Obs : ao criar uma matriz, converta-a pra str antes de tentar escreve-la em um txt.
def EscreverLinha():
    for x in range(0,len(teste)-2):
        if teste[x] == "]":
            arquivo.write(" ")
        if teste[x] == "," and teste[x-1] != "]":
            arquivo.write(",")
        if isdigit(teste[x]):
            arquivo.write(teste[x])
    arquivo.write('\n')

#Escolhe a quantidade de matrizes a serem escritas.
i = 0
while i < 100000:
    teste = str(gerarMatriz())
    EscreverLinha()
    i+= 1
arquivo.close()

