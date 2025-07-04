usuarios = {} 

def cadastrar_usuario():
    print("\n Cadastro de Usuário")
    usuario = input("Escolha um nome de usuário: ")

    if usuario in usuarios:
        print("Usuário já existe! Tente outro.")
        return

    senha = input("Digite uma senha: ")

    print("\nEscolha o tipo de perfil:")
    print("1. Perfil Pessoal")
    print("2. Perfil Empresário")

    while True:
        perfil_opcao = input("Digite 1 ou 2: ")
        if perfil_opcao == "1":
            perfil = "Pessoal"
            print("\n Dados do Perfil Pessoal:")
            email = input("Email: ")
            cpf = input("CPF: ")
            telefone = input("Telefone: ")
            dados = {
                "email": email,
                "cpf": cpf,
                "telefone": telefone
            }
            break

        elif perfil_opcao == "2":
            perfil = "Empresário"
            print("\nDados do Perfil Empresário:")
            email = input("Email: ")
            cnpj = input("CNPJ: ")
            telefone = input("Telefone: ")
            cpf = input("CPF do responsável: ")
            dados = {
                "email": email,
                "cnpj": cnpj,
                "telefone": telefone,
                "cpf": cpf
            }
            break
        else:
            print("Opção inválida! Tente novamente.")

    usuarios[usuario] = {"senha": senha, "perfil": perfil, "dados": dados}
    print(f"Cadastro realizado com sucesso como perfil '{perfil}'!\n")

def fazer_login():
    print("\nLogin")
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    user = usuarios.get(usuario)

    if user and user["senha"] == senha:
        perfil = user["perfil"]
        dados = user["dados"]
        print(f"\nLogin bem-sucedido! Bem-vindo, {usuario}!")
        print(f"Perfil: {perfil}")
        print(" Dados do usuário:")
        print(f"Email: {dados.get('email')}")
        print(f"CPF: {dados.get('cpf')}")
        print(f" Telefone: {dados.get('telefone')}")
        if perfil == "Empresário":
            print(f" CNPJ: {dados.get('cnpj')}")
        print()
    else:
        print("Usuário ou senha incorretos.\n")

def menu():
    while True:
        print("1. Cadastrar novo usuário")
        print("2. Fazer login")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            fazer_login()
        else:
            print("Opção inválida!\n")

menu()
