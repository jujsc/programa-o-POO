class Veiculo:
    def __init__(self, tipo, peso):
        self._tipo = tipo
        self._peso = peso

    def set_tipo(self, tipo):
        tipo = tipo.upper()
        if tipo in 'CMV':
            self._tipo = tipo
        else:
            print("Veículo inapropriado! Os veículos apropriados são carro, moto e van.")
    
    def set_peso(self, peso):
        print("Insira o peso do veículo em kg!")
        self._peso = peso

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

class Balsa: #a barca que tem conexão com o veiculo, na barca ter a variavel veiculo
    def __init__(self, quantidadeVeiculos, pesoMaximo):
        self._veiMax = quantidadeVeiculos
        self._pesoMax = pesoMaximo * 1000
        self._quantCarro = 0
        self._quantVan = 0
        self._quantMoto = 0
        self._pesoCarro = 0
        self._pesoMoto = 0
        self._pesoVan = 0

    def vagas_restantes(self):
        self._vagas_rest = self._veiMax - self._quantCarro - self._quantVan - self._quantMoto
        return self._vagas_rest
    
    def peso_restante(self):
        self._peso_rest = self._pesoMax - self._pesoCarro - self._pesoVan - self._pesoMoto
        return self._peso_rest

    def embarca_veiculo(self, Veiculo):
        if self.vagas_restantes() == 0:
            print("Barca não possui vagas disponíveis!")
        if self.peso_restante() > self._pesoMax:
            print("O peso limite da barca foi execido, impossível embarcar veículo!")
        else:
            if Veiculo.get_tipo() == "M":
                self._quantMoto +=1
                self._pesoMoto += Veiculo.get_peso()
            if Veiculo.get_tipo() == "C":
                self._quantCarro +=1
                self._pesoCarro += Veiculo.get_peso()
            if Veiculo.get_tipo() == "V":
                self._quantVan +=1
                self._pesoVan += Veiculo.get_peso()

    def exibe_dados(self):
        print("Peso máximo suportado pela balsa:", pesoMaximo, "tol")
        print("Peso total de motos:", self._pesoMoto, "kg")
        print("Peso total de carros:", self._pesoCarro, "kg")
        print("Peso total de vans:", self._pesoVan, "kg")
        print("Peso total de veículos na balsa", self._pesoMax - self.peso_restante(), "kg")
        print("Peso restante da barca:", self.peso_restante(), "kg")
        print("Quantidade de vagas na balsa:", self._veiMax, "vagas")
        print("Quantidade total de motos:", self._quantMoto, "vagas")
        print("Quantidade total de carros:", self._quantCarro, "vagas")
        print("Quantidade total de vans:", self._quantVan, "vagas")
        print("Quantidade total de veículos na balsa", self._veiMax - self.vagas_restantes(), "vagas")
        print("Quantidade restante de vagas na balsa:", self.vagas_restantes(), "vagas")

if __name__ == '__main__':
    quantidadeVeiculos = int(input("Quantidade máxima de veículos:"))
    pesoMaximo = float(input("Peso máximo suportado pela barca:"))
    balsa = Balsa(quantidadeVeiculos,pesoMaximo)
    moto = Veiculo('M',70)
    carro = Veiculo('C',150)
    van = Veiculo('V',300)
    balsa.embarca_veiculo(moto)
    balsa.embarca_veiculo(carro)
    balsa.embarca_veiculo(van)
    balsa.exibe_dados()