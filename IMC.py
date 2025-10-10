def calcula_imc(peso, altura):
    return peso / (altura ** 2)

print("=== Calculadora de IMC ===")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = calcula_imc(peso, altura)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")
