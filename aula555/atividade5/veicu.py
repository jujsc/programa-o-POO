class Veiculo:
    def __init__(self, tipo, peso, ano, modelo, cor ):
        self._tipo = tipo
        self._peso = peso
        self._ano = ano
        self._cor = cor
        self._modelo = modelo

    def set_tipo(self, tipo):
        tipo = tipo.upper()
        if tipo in 'CMV':
            self._tipo = tipo
        else:
            print("Veículo inapropriado! Os veículos apropriados são carro, moto e van.")
    
    def get_tipo_str(self):
        if self._tipo == 'C':
            return 'Carro'
        elif self._tipo == 'V':
            return 'Van'
        elif self._tipo == 'M':
            return 'Moto'
        else:
            return 'Veículo inválido!'

    def get_tipo(self):
         return self._tipo

    def get_peso(self):
        return self._peso
    
    def get_cor(self):
        return self._cor 

    def get_modelo(self):
        return self._modelo

    def get_ano(self):
        return self._ano
    
    def idade(self):
        return 2022 - self._ano

    def exibe_dados(self):
        print("Tipo:", self.get_tipo_str())
        print("Peso", self._peso)
        print('Cor:', self._cor)        
        print('Modelo:', self._modelo)
        print('Ano:', self._ano)
        print()

veiculos = list()

continuar = 's'
while continuar in 'Ss':
    tipo = input("Tipo: (c/m/v) ")
    peso = float(input("Peso (kg): "))
    ano = int(input('Informe o ano: '))
    mod = input('Informe o modelo: ')
    cor = input('Cor: ')
    veiculos.append(Veiculo(tipo, peso, ano, mod, cor))
    continuar = input('Continuar? S/N: ')

print('\n** Veiculos(s) informado(s) **')
idadeMedia = qtM = qtC = qtV = 0
tipoespecifico = input("Qual tipo você gostaria de saber os dados: (c/m/v) ")
for veiculo in veiculos:
    menor = veiculo.idade()
    if veiculo.get_tipo().upper() == "M":
        qtM +=1
    if veiculo.get_tipo().upper() == "C":
        qtC +=1
    if veiculo.get_tipo().upper() == "V":
        qtV +=1
    
    if tipoespecifico.upper() == veiculo.get_tipo().upper():
        veiculo.exibe_dados()
    
    if veiculo.idade() >= 10:
        print("Veiculo possui mais de 10 anos")
        print("Veiculo:", veiculo.get_tipo_str(),"Modelo:", veiculo.get_modelo(), "Idade:", veiculo.idade())
    
    if (veiculo.idade >= 3 and veiculo.idade <= 5) and veiculo.get_cor.lower == "branco":
        print("veiculo entre 3 e 5 anos branco:")
        print("Veiculo:", veiculo.get_tipo_str(),"Modelo:", veiculo.get_modelo())


    idadeMedia += veiculo.idade()

    if veiculo.get_cor().lower() == "azul":
        print("Veículos azuis:")
        print('Modelo:', veiculo.get_modelo(), "é azul")
    
    if veiculo.idade() < menor:
        menor = veiculo.idade()

print("A idade média dos veiculos informados é", idadeMedia)
print("A quantidade de carros é ", qtC)
print("a quantidade de motos é ", qtM)
print("a quantidade de van é ", qtV)


    