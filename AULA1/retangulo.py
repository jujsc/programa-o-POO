class Retangulo:
    def set_base(self, base):
        self.base = base

    def get_base(self):
        return self.base

    def set_altura(self, altura):
        self.altura = altura

    def get_altura(self):
        return self.altura

    def area(self):
        return self.base * self.altura

r1 = Retangulo()
r1.set_base(10.0)
r1.set_altura(8.5)
print(f'{r1.get_base()} x {r1.get_altura()} = {r1.area()}')

r2 = Retangulo()
r2.set_base(12.2)
r2.set_altura(6.8)
print(f'{r2.get_base()} x {r2.get_altura()} = {r2.area()}')