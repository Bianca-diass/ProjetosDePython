contatos = []

def listar():
    if not contatos:
        print("Nenhum contato cadastrado.")
    for i, c in enumerate(contatos):
        print(f"{i+1}. {c['nome']} - {c['telefone']} - {c['email']}")

def adicionar():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    print("Contato adicionado!")

def remover():
    listar()
    if contatos:
        i = int(input("Número do contato para remover: ")) - 1
        if 0 <= i < len(contatos):
            contatos.pop(i)
            print("Contato removido!")

while True:
    print("\n=== Agenda de Contatos ===")
    print("1. Listar contatos")
    print("2. Adicionar contato")
    print("3. Remover contato")
    print("0. Sair")
    opc = input("Escolha: ")

    if opc == "0":
        break
    elif opc == "1":
        listar()
    elif opc == "2":
        adicionar()
    elif opc == "3":
        remover()
    else:
        print("Opção inválida!")
