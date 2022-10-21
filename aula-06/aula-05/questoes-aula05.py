#Atividade 01
total = 0
palavra = "python rocks!"
acabou = False
while (not acabou):
    acabou = (total == len(palavra))
    total = total + 1
print(total - 1)

#Atividade 02
passos = 0
while (passos<10):
  passos += 1
print(passos)

#Atividade 03
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "maça".upper()
    letras_acertadas = ["_", "_", "_", "_"]


    erros = 0
    print(len(palavra_secreta))
    print(letras_acertadas)

    while(True):

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

        if (erros == 6):
            break
        if ("_" not in letras_acertadas):
            break
        print(letras_acertadas)


    if("_" not in letras_acertadas):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")

#Atividade 04
frutas = ["maçã", "banana", "laranja", "melancia"]
lista = []
for fruta in frutas:
    lista.append(fruta.upper())
lista = [fruta.upper() for fruta in frutas]

#Atividade 05
inteiros = [1,3,4,5,7,8]
quadrados = [i*i for i in inteiros]

#Atividade 06
inteiros = [1,3,4,5,7,8,9]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)
pares = [i for i in inteiros if i % 2 == 0]