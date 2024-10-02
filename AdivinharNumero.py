import random

print("Dia de dorte ou não!")

for chance in range(5):
    numeroSorteado = random.randrange(1, 101)
    numeroUsuario = int(input(f"Chance({chance +1}) - Digite um número: "))
    if numeroUsuario == numeroSorteado:
        print("Você ganhou!")
    else:
        print(f"Errou o número foi: {numeroSorteado}")
print("Acabou as chances e você perdeu não foi seu dia de sorte!")
