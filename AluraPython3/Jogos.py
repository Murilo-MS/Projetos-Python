import Forca
import Adivinhação

def escolhe_jogo():
    print("*********************************")
    print("***Bem vindo ao menu de jogos!***")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("jogando Forca!")
        Forca.jogar()
    elif(jogo == 2):
        print("jogando Adivinhação")
        Adivinhação.jogar()

if(__name__="__main__"):
    escolhe_jogo()