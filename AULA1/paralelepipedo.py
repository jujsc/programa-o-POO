class Paralelepipedo:
    def set_base(self, base):
        self.base = base

    def get_base(self):
        return self.base

    def set_altura(self, altura):
        self.altura = altura

    def get_altura(self):
        return self.altura
    
    def set_profundidade(self, profundidade):
        self.profundidade = profundidade

    def get_profundidade(self):
        return self.profundidade

    def volume(self):
        return self.base * self.altura * self.profundidade

p1 = Paralelepipedo()
p1.set_base(10.0)
p1.set_altura(8.5)
p1.set_profundidade(2.0)
print(f'{p1.get_base()} x {p1.get_altura()} x {p1.get_profundidade()} = {p1.volume()}')

p2 = Paralelepipedo()
p2.set_base(12.2)
p2.set_altura(6.8)
p2.set_profundidade(5.5)
print(f'{p2.get_base()} x {p2.get_altura()} x {p2.get_profundidade()} = {p2.volume()}')