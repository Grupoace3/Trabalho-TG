# Ler as linhas do txt, e atribuit a matriz a uma variavel temporaria
from curses.ascii import isdigit

arquivo = open("Matrizes.txt","r")

#Funcão para checar se uma sequencia de chars pode ser convertido para inteiro ou não.
def ChecarDigit(palavra):
    result = True
    for i in range(0,len(palavra)):
        if isdigit(palavra[i]) == False:
            result = False
    return result

#   Essa função funciona em vários passos. Primeiro ela abre o arquivo e cria dois vetores.
#   Após isso ela roda um loop em todos os chars de uma linha por vez.
#   Nesse loop ele chega todos os chars, caso o char seja um inteiro uma variável aux receberá 
#o valor do char.
#   Caso o char seja uma vírgula, quer dizer que o primeiro valor da matriz já terminou e será adicionado
#a um vetor auxiliar. 
#   Caso o char for um " "(espaço), quer dizer que a linha já acabou e será adicionado um shallowcopy
#da matrix auxiliar a matriz principal. Quando adicionado a matriz principal, oque foi adicionado
#será um vetor. ex: vetorprincipal->[vetorquefoiadicionado->[]].
#   Importante ser uma shallowcopy pra que não seja apenas uma referencia ao objeto 
#   Quando adiciona o vetoraux ao vetorprincipal. zeramos o vetor aux e continuamos iterando sobre a linha
#caso haja mais valores o ciclo irá reiniciar.

def CriarVariavel():
    linha = arquivo.readline()
    matriz = []
    matrizaux = []
    aux = ""
    print("A linha é:",linha)
    for i in range(0,len(linha)):

        if isdigit(linha[i]):
            aux += str(linha[i])
            # print("Aux é:",aux)
        if linha[i] == ",":
            matrizaux.append(int(aux))
            aux = ""  
            # print("Matriz aux é:",matrizaux)
        if i == (len(linha)-1) and ChecarDigit(aux):
            matrizaux.append(int(aux))
            aux = ""
            matriz.append(matrizaux.copy())
            matrizaux.clear()
            # print("aaMatriz aux é:",matrizaux)

        if linha[i] == " ":
            matrizaux.append(int(aux))
            aux = ""
            # print("Matriz aux é:",matrizaux)
            matriz.append(matrizaux.copy())
            matrizaux.clear()

    print("a matriz é: ",matriz)
inicio = time.time()

for l in arquivo:
    CriarVariavel()
arquivo.close()
