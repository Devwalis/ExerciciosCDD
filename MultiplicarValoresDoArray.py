array1 = [0]*10
array2 = [0]*10
tam = (len(array1))
for x in range(tam):
    array1[x]= int(input("Digite os números: "))
mult = int(input("Digite o multiplicador: "))
for i in range(tam):
    array2[i] = array1[i]*mult
print(array1)
print(mult)
print(array2)

