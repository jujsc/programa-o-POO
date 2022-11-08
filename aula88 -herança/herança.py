# atividade veiculo superclasse e sub classes aereo, terrestre e aquatico

class Veiculo: 
    def __init__(self, ano, peso, tanque, modelo):
        self.__ano = ano
        self.__peso = peso
        self.__tanque = tanque
        self.__modelo = modelo
    
    def get_peso(self):
        return self.__peso
    
    def get_tanque(self):
        return self.__tanque
    
    def info(self):
        print("Ano:", self.__ano)
        print("Peso:", self.__peso)
        print("Tanque:",self.__tanque)
        print("Modelo:", self.__modelo)

class Aereo(Veiculo):
    def __init__(self, ano, peso, tanque, modelo, qt_asa, qt_motor):
        super().__init__(ano, peso, tanque, modelo)
        self.__qt_asa = qt_asa
        self.__qt_motor = qt_motor
    
    def info(self):
        print("\n AÉREO")
        super().info()
        print("Quantidade de asas", self.__qt_asa)
        print("Quantidade de MOTORES", self.__qt_motor)
        print("Consumo:", self.consumo(), "km/l")
        print("Autonomia", self.autonomia())
    
    def consumo(self):
        return 1/((self.get_peso()* 0.00003) + self.__qt_motor * 0.01)
    
    def autonomia(self):
        return self.get_tanque() * self.consumo()

class Aquatico(Veiculo):
    def __init__(self, ano, peso, tanque, modelo, qt_conves, qt_motor):
        super().__init__(ano, peso, tanque, modelo)
        self.__qt_conves = qt_conves
        self.__qt_motor = qt_motor
    
    def info(self):
        print("\n AQUÁTICO")
        super().info()
        print("Quantidade de motores", self.__qt_motor)
        print("Quantidade de Conves", self.__qt_conves)
        print("Consumo:", self.consumo(), "km/l")
        print("Autonomia", self.autonomia())
    
    def consumo(self):
        return 1/((self.get_peso()* 0.00002) + self.__qt_motor * 0.02)
    
    def autonomia(self):
        return self.get_tanque() * self.consumo()

class Terrestre(Veiculo):
    def __init__(self, ano, peso, tanque, modelo, qt_roda, qt_porta):
        super().__init__(ano, peso, tanque, modelo)
        self.__qt_roda = qt_roda
        self.__qt_porta = qt_porta
    
    def info(self):
        print("\n AQUÁTICO")
        super().info()
        print("Quantidade de rodas", self.__qt_roda)
        print("Quantidade de portas", self.__qt_porta)
        print("Consumo:", self.consumo(), "km/l")
        print("Autonomia", self.autonomia())
    
    def consumo(self):
        return 1/((self.get_peso()* 0.00005) + self.__qt_roda * 0.005)
    
    def autonomia(self):
        return self.get_tanque() * self.consumo()
        

if __name__ == '__main__':
    veiculo = Veiculo(1,2,3,"Carro")
    veiculo.info()
    aquatico = Aquatico(2008, 100, 10, "Submarino", 2, 1)
    aquatico.info()
    terrestre = Terrestre(123, 10, 30, "Carro", 1, 4)
    terrestre.info()
    aereo = Aereo(456, 16, 12, "Aviâo", 2, 7)
    aereo.info()