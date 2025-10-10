import random

palavras = ["python", "computador", "programacao", "jogos", "java"]
palavra = random.choice(palavras)
letras_certas = []
tentativas = 6

print("=== Jogo da Forca ===")

while tentativas > 0:
    display = ""
    for letra in palavra:
        if letra in letras_certas:
            display += letra + " "
        else:
            display += "_ "
    print(display)

    if "_" not in display:
        print("Parabéns! Você ganhou!")
        break

    palpite = input("Digite uma letra: ").lower()
    if palpite in palavra:
        letras_certas.append(palpite)
    else:
        tentativas -= 1
        print(f"Errado! Restam {tentativas} tentativas.")

if tentativas == 0:
    print("Você perdeu! A palavra era:", palavra)
