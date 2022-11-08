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