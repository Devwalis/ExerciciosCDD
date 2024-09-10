hora1 = int(input("Hora 1:"))
min1 = int(input("Min 2:"))
hora2 = int(input("Hora 2:"))
min2 =  int(input("Min 2:"))
horaExecedente = (min1 + min2) // 60
minutos = (min1 + min2) % 60
horas = hora1 + hora2  + horaExecedente + 24
if horas < 0:
    horas = horas + -1
if horas  > 12:
    horas = horas - 12
print(f"{horas}:{minutos}")
