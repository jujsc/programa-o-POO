from ast import Num


class Pessoa():
    def __init__(self, altura, peso, sexo): #self referencia ao objeto que está disparando 
        self._altura = altura
        self._peso = peso
        self._sexo = sexo
    
    def get_altura(self):
        return self._altura
    
    def get_peso(self):
        return self._peso

    def set_sexo(self, sexo):
        sexo = sexo.upper()
        if sexo in 'MF':
            self._sexo = sexo
        else:
            print("Sexo deve ser 'M' ou 'F'")
    
    def get_sexo_str(self):
        if self._sexo == 'F':
            return 'Feminino'
        elif self._sexo == 'M':
            return 'Masculino'
        else:
            return 'Indefinido'
    
    def peso_ideal(self):
        if self._sexo == 'F':
            ideal = (62.1 * self._altura) - 44.7
            return ideal
        if self._sexo == "M":
            ideal = (72.7 * self._altura) - 44.7
            return ideal

    def faixa_peso(self):
        faixa_mais = self.peso_ideal() + (5/100 * self.peso_ideal())
        faixa_menos = self.peso_ideal() - (5/100 * self.peso_ideal())
        if self._peso <= faixa_mais and self._peso >= faixa_menos:
            return "tem peso na faixa."
        if self._peso > faixa_mais:
            return "tem peso a cima da faixa."
        if self._peso < faixa_menos:
            return "tem peso abaixo da faixa."

    def imprime_dados(self):
        print("Sexo:", self.get_sexo_str())
        print("Altura:", self._altura,"m")
        print("Peso:", self._peso,"kg")
        print("Peso ideal:", self.peso_ideal(),"kg")
        print("Pessoa",self.faixa_peso())
        
if __name__ == '__main__':
    p1 = Pessoa(1.75, 45, "M")
    p1.imprime_dados()
    print("-"*30)
    p2 = Pessoa(1.50, 48, "F")
    p2.imprime_dados()
    print("-"*30)
    p3 = Pessoa(1.50, 80.5, "F")
    p3.imprime_dados()
    print("-"*30)

    
