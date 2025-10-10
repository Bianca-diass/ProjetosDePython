import random

numero = random.randint(1, 100)
tentativas = 0
print("=== Jogo da Adivinhação ===")

while True:
    palpite = int(input("Adivinhe o número (1-100): "))
    tentativas += 1
    if palpite == numero:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif palpite < numero:
        print("Tente um número maior!")
    else:
        print("Tente um número menor!")
