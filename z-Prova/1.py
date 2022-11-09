from cmath import pi

class Geometria:
    def __init__(self, dim_1, dim_2 =None):
        self._dim_1 = dim_1
        self._dim_2 = dim_2
    
    def tipo(self):
        if self._dim_2 == None:
            return "Círculo"
        if self._dim_2 == self._dim_1:
            return "Quadrado"
        if self._dim_2 != self._dim_1:
            return "Retângulo"
    
    def area(self):
        if self.tipo() == "Círculo":
            area = (self._dim_1 ** 2) * pi
            return area
        if self.tipo() == "Quadrado" or self.tipo() == "Retângulo":
            area = self._dim_1 * self._dim_2
            return area
    
    def exibe_dados(self):
        print("Tipo:", self.tipo())
        if self.tipo() == "Círculo":
            print("Dimensão: Raio", self._dim_1)
        else:
            print("Dimensões:")
            print("Lado 1", self._dim_1)
            print("Lado 2", self._dim_2)
        print("Área:", round(self.area(),2))

if __name__ == '__main__':
    g1 = Geometria(4.37)
    g2 = Geometria(3.9,3.9)
    g3 = Geometria(2.1,5.8)
    g1.exibe_dados()
    print()
    g2.exibe_dados()
    print()
    g3.exibe_dados()