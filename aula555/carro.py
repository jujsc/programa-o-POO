class Carro:
    def __init__(self, fabricante, modelo, ano):
        self._fabricante = fabricante
        self._modelo = modelo
        self._ano = ano

    def get_fabricante(self):
        return self._fabricante

    def get_modelo(self):
        return self._modelo

    def get_ano(self):
        return self._ano

    def exibe_dados(self):
        print('Fabricante:', self._fabricante)        
        print('Modelo:', self._modelo)
        print('Ano:', self._ano)
        print()