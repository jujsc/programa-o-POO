from carro import Carro

carros = list()

carros.append(Carro('VW', 'Up', 2020))
carros.append(Carro('Fiat', 'Mobi', 2019))
carros.append(Carro('Ford', 'Ka', 2016))

modelo = input('Informe o modelo desejado: ')

for carro in carros:
    if carro.get_modelo() == modelo:
        carro.exibe_dados()
        break
else:
    print(f'\nModelo "{modelo}" não localizado!\n')