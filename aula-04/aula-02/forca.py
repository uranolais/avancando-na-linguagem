
def jogar():
    print("*"*32)
    print("Bem vindo no jogo de forca")
    print("*"*32)
    
    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip() #Tirar os espaços antes e depois da palavra

        index = 0 #posição da letra)
        
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print("jogando ...")

    print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar()