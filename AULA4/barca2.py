from msilib.schema import Class


class Balsa():
    def __init__(self, peso, qtd_veiculos) -> None:
        self._peso_max = peso
        self.qtd_vaga_max = qtd_veiculos
        
        self._num_moto = 0
        self._num_carro = 0
        self._num_vans = 0
        self._qtd_peso_moto = 0
        self._qtd_peso_carro = 0
        self._qtd_peso_van = 0

    def vagas_restantes(self):
        return self.qtd_vaga_max - self._num_moto - self._num_carro - self._num_vans

    def peso_restante(self):
        return (self._peso_max * 1000)  - self._qtd_peso_moto - self._qtd_peso_carro - self._qtd_peso_van

    def embarcar_veiculo(self, veiculo):
        if(self.vagas_restantes() == self.qtd_vaga_max): print("Vagas esgotadas na barca")
        if(veiculo.get_peso() > self.peso_restante()): print("peso excede o limite da balsa")

        tipo_veiculo = veiculo.get_tipo()
        if(tipo_veiculo == 'M'): 
            self._qtd_peso_moto = self._qtd_peso_moto + veiculo.get_peso()
            self._num_moto = self._num_moto + 1
        if(tipo_veiculo == 'C'): 
            self._qtd_peso_carro = self._qtd_peso_carro + veiculo.get_peso()
            self._num_carro = self._num_carro + 1
        if(tipo_veiculo == 'V'): 
            self._qtd_peso_van = self._qtd_peso_van + veiculo.get_peso()
            self._num_vans = self._num_vans + 1

    def exibe_dados(self):
        print("Peso máximo kg: " + str(self._peso_max * 1000))
        print("Peso de motos: " + str(self._qtd_peso_moto))
        print("Peso de carros: " + str(self._qtd_peso_carro))
        print("Peso de vans: " + str(self._qtd_peso_van))
        print("Peso total: " + str(self._qtd_peso_moto + self._qtd_peso_carro + self._qtd_peso_van))
        print("Peso restante: " + str(self.peso_restante()))
        print("Vagas na balsa: " + str(self.qtd_vaga_max))
        print("Quantidade de motos: " + str(self._num_moto))
        print("Quantidade de carros: " + str(self._num_carro))
        print("Quantidade de vans: " + str(self._num_vans))
        print("Vagas ocupadas: " + str(self._num_moto + self._num_carro + self._num_vans))
        print("Vagas restantes: " + str(self.vagas_restantes()))

class Veiculo():
    def __init__(self, tipo, peso) -> None:
        self._tipo = tipo.upper()
        self._peso = peso

    def get_tipo(self):
        return self._tipo
    
    def get_tipo_str(self):
        if(self._tipo == 'M'): return 'Moto'
        elif(self._tipo == 'C'): return 'Carro'
        elif(self._tipo == 'V'): return 'Van'
        else: return 'Indefinido'
            
    def get_peso(self):
        return self._peso

if __name__ == '__main__':
    balsa = Balsa(10, 10)

    moto = Veiculo('M',50)
    carro = Veiculo('C',60)
    vans = Veiculo('V',70)

    balsa.embarcar_veiculo(moto)
    balsa.embarcar_veiculo(carro)
    balsa.embarcar_veiculo(vans)

    balsa.exibe_dados()