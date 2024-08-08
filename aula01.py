class Carro:
    def __init__(self, cor, marca, modelo):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        
    def imprimir(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, cor: {self.cor}')
        
carro1 = Carro('Prata', 'GM', 'Onix') 
carro1.imprimir()

carro2 = Carro('Vermelho', 'Hyundai', 'HB20') 
carro2.imprimir()





