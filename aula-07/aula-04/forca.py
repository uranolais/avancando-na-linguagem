
def jogar():
    print("*"*32)
    print("Bem vindo no jogo de forca")
    print("*"*32)
    
    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip() 

        index = 0 
        
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar()