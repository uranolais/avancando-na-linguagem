import forca 
import advinhacao
def escolhe_jogo():
    print("*"*32)
    print("*******Escola o seu Jogo!*******")
    print("*"*32)

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual Jogo?"))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando advinhação")
        advinhacao.jogar()

if(__name__=="__main__"):
    escolhe_jogo()