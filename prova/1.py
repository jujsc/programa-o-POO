class TrianguloRetangulo:
    def set_cat1(self, cat1):
        self.cat1 = cat1
    
    def get_cat1(self):
        if self.cat1 > 0 and self.cat2 > 0:
            return self.cat1
        if type(self.cat1) == str and type(self.cat2) == str:
            print("valor deve ser numérico")
            return 0
        else:
            print("Valor do cateto 1 é inválido!")
            return 0

    def set_cat2(self, cat2):
        self.cat2 = cat2

    def get_cat2(self):
        if self.cat2 > 0 and self.cat1 > 0:
            return self.cat2
        if type(self.cat1) == str and type(self.cat2) == str:
            print("valor deve ser numérico")
            return 0
        else:
            print("Valor do cateto 2 é inválido!")
            return 0

    def area(self):
        if self.cat2 > 0 and self.cat1 > 0:
            return self.cat1 * self.cat2 /2
        else:
            return 0

tr1 = TrianguloRetangulo()
tr1.set_cat1(10.5)
tr1.set_cat2(8.75)
print(f'A área do triângulo retângulo é {tr1.get_cat1()} x {tr1.get_cat2()} / 2 = {tr1.area():.3f}')
print("-"*20)
tr2 = TrianguloRetangulo()
tr2.set_cat1(10)
tr2.set_cat2(8)
print(f'A área do triângulo retângulo é {tr2.get_cat1()} x {tr2.get_cat2()} / 2 = {tr2.area():.3f}')
print("-"*20)
tr3 = TrianguloRetangulo()
tr3.set_cat1(0)
tr3.set_cat2(0)
print(f'A área do triângulo retângulo é {tr3.get_cat1()} x {tr3.get_cat2()} / 2 = {tr3.area():.3f}')
