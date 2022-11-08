from carro import Carro

carros = list()

carros.append(Carro('VW', 'Up', 2020))
carros.append(Carro('Fiat', 'Mobi', 2019))
carros.append(Carro('Ford', 'Ka', 2016))

for carro in carros:
    print('Modelo:', carro.get_modelo())