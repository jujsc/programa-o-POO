# Sobrecarga com parâmetros padrão
def calcula_area(base=None, altura=None):
    print()
    print('Parâmetro base:', base)
    print('Parâmetro altura:', altura)

    if base == None:
        base = float(input('Informe a base: '))
        
    if altura == None:
        altura = float(input('Informe a altura: '))

    print('Area:', base * altura)

# Nenhum parâmetro informado
calcula_area()

# Parâmetro informado: base
calcula_area(2)

# Parâmetro informado: altura
calcula_area(altura=3)

# Parâmetros informados: base e altura
calcula_area(3, 4)

# Parâmetros informados: altura e base
calcula_area(altura=3, base=4)
