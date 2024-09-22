while True:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    while True:
        opcao1 = int(input("Selecione a operação: \n"
            "1. Para somar \n"
            "2. Subtração \n"
            "3. Multiplicação \n"
            "4. Divisão \n"
            "5. Para Digitar novo número \n"
            "6. Para sair do programa \n"))

        if opcao1 == 1:
            soma = n1 + n2
            print(f"A soma é: {soma}")
        elif opcao1 == 2:
            subtracao = n1 - n2
            print(f"A subtração dos números é: {subtracao}")
        elif opcao1 == 3:
            multiplicacao = n1 * n2
            print(f"A multiplicação dos números é: {multiplicacao}")
        elif opcao1 == 4:
            if n2 != 0:
                divisao = n1 / n2
                print(f"A divisão dos números é: {divisao}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        elif opcao1 == 5:
            break
        elif opcao1 == 6:
            print("Saindo do programa...")
            exit()
        else:
            print("Opção inválida, tente novamente.")










