

gasolina = 5.80
etenol = 4.90

opcao = int(input("-------------------------------------------\n"
      "Digite (1) para escolher gasolina\n"
      "Digite (2) para escolher etenol\n"
                "-------------------------------------------\n:"))
if(opcao==1):
    qtdLitros = float(input("Informe a quantidade de litros: "))
    valorGasolina = qtdLitros * gasolina
    print(f"O valor do litro da gasolina está custando R$5,80 e você vai comprar {qtdLitros}L e vai pagar o total de: \n R$:{valorGasolina:.2f}")
else:
    if(opcao==2):
        qtdLitros = float(input("Informe a quantidade de litros: "))
        valorEtenol = qtdLitros * etenol
        print(f"O valor do litro do etenol está custando R$4,90 e você vai comprar{qtdLitros}L e vai pagar o total de: \n R$:{valorEtenol:.2f}")

    else:
        print("opcao invalida")










