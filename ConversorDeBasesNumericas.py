num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('sua opção: '))

if opcao == 1:
    print(f'{num}convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para octal é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f' {num} convertido para hexadecimal')
else:
    print('Opção inválida')

