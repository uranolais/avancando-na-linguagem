
def jogar():
    print("*"*32)
    print("Bem vindo no jogo de forca")
    print("*"*32)
    
    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    #enquanto não enforcou e não acertou
    # Not False = True
    while(not enforcou and not acertou):
        print("jogando ...")

    print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar()