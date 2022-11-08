from veiculo import Veiculo
from aqatico import Aquatico
from aereo import Aereo
from terrestre import Terrestre

if __name__ == '__main__':
    veiculo = Veiculo(1,2,3,"Carro")
    veiculo.info()
    aquatico = Aquatico(2008, 100, 10, "Submarino", 2, 1)
    aquatico.info()
    terrestre = Terrestre(123, 10, 30, "Carro", 1, 4)
    terrestre.info()
    aereo = Aereo(456, 16, 12, "Aviâo", 2, 7)
    aereo.info()