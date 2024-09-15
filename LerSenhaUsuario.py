senhaV = input("Digite uma senha para salvar: ")

for c in range(0,  1):

        senha = input("Digite a senha: ")
        if senha == senhaV:
            print("Senha correta!")
        elif senha != senhaV:
                for i in range(1, 3):
                    print("SENHA INVALIDA! \n"
                          "você tem 3 tentativas")
                    print(f"Tentativas:{i}")
                    senha = input("Digite a senha: ")
                print("Senha Bloqueada")
