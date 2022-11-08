from veiculo import Veiculo

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