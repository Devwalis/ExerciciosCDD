hora = int(input("Digite a hora atual: "))
minuto = int(input("Digite o minuto atual: "))
segundo = int(input("Digite o segundo atual: "))
horaCorrespondente = 3600 * hora + 60 * minuto + segundo
print("O tempo correpondente de:  " + str(hora)+  ":" + str(minuto) + ":" + str(segundo) + ":"+ " em segundos sera de: " + str(horaCorrespondente))