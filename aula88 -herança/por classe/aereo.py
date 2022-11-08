from veiculo import Veiculo

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
