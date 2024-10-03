class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        print(self.marca, self.modelo, self.cor)

        def acelerar(self):
            print('Acelerando...')
        def frear(self):
            print('Freando...')
        def re(self):
            print('Dando Ree')
marca = input('Marca: ')
modelo = input('Modelo: ')
cor = input('Cor: ')
carro = Carro(marca, modelo, cor)

print(carro)
