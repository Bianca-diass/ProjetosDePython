def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Erro: divisão por zero"

while True:
    print("\n=== Calculadora Simples ===")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")
    opc = input("Escolha: ")

    if opc == "0":
        break

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if opc == "1":
        print("Resultado:", soma(a, b))
    elif opc == "2":
        print("Resultado:", subtrai(a, b))
    elif opc == "3":
        print("Resultado:", multiplica(a, b))
    elif opc == "4":
        print("Resultado:", divide(a, b))
    else:
        print("Opção inválida!")
