from carro import Carro

carros = list()

continuar = 's'
while continuar in 'Ss':
    fab = input('Informe o fabricante: ')
    mod = input('Informe o modelo: ')
    ano = int(input('Informe o ano: '))
    carros.append(Carro(fab, mod, ano))
    continuar = input('Continuar? S/N: ')

print('\n** Carro(s) informado(s) **')
for carro in carros:
    print('Modelo:', carro.get_modelo())