def perfil_empresarial():
    print("\nPerfil Empresarial")
    razao_social = input("Razão Social: ")
    cnpj = input("CNPJ: ")
    segmento = input("Segmento da empresa: ")
    qtd_funcionarios = input("Quantidade de funcionários: ")

    clientes = []
    print("\nDigite o nome dos clientes (digite 'fim' para parar):")
    while True:
        cliente = input("Cliente: ")
        if cliente.lower() == 'fim':
            break
        clientes.append(cliente)

    print("\nDados do Perfil Empresarial")
    print(f"Razão Social: {razao_social}")
    print(f"CNPJ: {cnpj}")
    print(f"Segmento: {segmento}")
    print(f"Quantidade de Funcionários: {qtd_funcionarios}")
    print("Clientes:", ", ".join(clientes))

perfil_empresarial()
