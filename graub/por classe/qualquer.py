from veiculo import Veiculo

class Qualquer:
    def calcularConsumo(tipo_transporte):
        if isinstance(tipo_transporte, Veiculo):
            print("Consumo:", tipo_transporte.consumo())