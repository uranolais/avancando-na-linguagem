
def jogar():
    print("*"*32)
    print("Bem vindo no jogo de forca")
    print("*"*32)
    
    palavra_secreta = "maça".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    '''for letra in palavra_secreta:
        letras_acertadas.append("_")'''   

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        
        if(chute in palavra_secreta):
            index = 0 
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))
        enforcou = erros == 6 #Enforcou é "True" se o valor de erros for igual a 6
        acertou = "_" not in letras_acertadas #Verdadeiro no momento que não existir mais na lista de letras acertadas o "_"
        print(letras_acertadas)

    
    if(acertou):
        print("Você Ganhou!!")
    else:
        print("Você Perdeu!!")
    print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar()