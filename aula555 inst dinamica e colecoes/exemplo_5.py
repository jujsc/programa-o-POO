from carro import Carro

carros = list()

carros.append(Carro('VW', 'Up', 2020))
carros.append(Carro('Fiat', 'Mobi', 2019))
carros.append(Carro('Ford', 'Ka', 2016))

modelo = input('Informe o modelo desejado: ')

sel = [c for c in carros if c.get_modelo() == modelo]
if len([c.exibe_dados() for c in sel]) == 0:
    print(f'\nModelo "{modelo}" não localizado!\n')