from veiculo import Veiculo


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