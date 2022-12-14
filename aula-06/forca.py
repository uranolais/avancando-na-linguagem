import random
def jogar():
    print("*"*32)
    print("Bem vindo no jogo de forca")
    print("*"*32)
    

    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()#Retirando o \n no final das palavras
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

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
        enforcou = erros == 6 
        acertou = "_" not in letras_acertadas 
        print(letras_acertadas)

    
    if(acertou):
        print("Você Ganhou!!")
    else:
        print("Você Perdeu!!")
    print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar()