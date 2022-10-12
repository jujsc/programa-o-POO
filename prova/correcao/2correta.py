from ast import Num


class Pessoa():
    def __init__(self, altura, peso, sexo): #self referencia ao objeto que está disparando 
        self._altura = altura
        self._peso = peso
        self._sexo = sexo

    
    def peso_ideal(self):
        if self._sexo in 'Ff':
            return (62.1 * self._altura) - 44.7
        if self._sexo in 'Mm':
            return (72.7 * self._altura) - 58
        else:
            return 0

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
        peso_min = self.peso_ideal() * 0.95
        peso_max = self.peso_ideal() * 1.05
        print("Sexo:", self._sexo)
        print(f'Altura: {self._altura:.2f} m')
        print(f'Peso: {self._peso:.2f} kg')
        print(f'Peso ideal: {self.peso_ideal():.2f} kg')
        print(f'Faixa de peso ideal: {peso_min:.2f} kg até {peso_max:.2f} kg')

        if self._peso < peso_min:
            print("Está abaixo do peso ideal.")
        if self._peso > peso_max:
            print("Está acima do peso ideal.")
        else:
            print("Está dentro da faixa de peso ideal.")
        
if __name__ == '__main__':
    altura = float(input("Informe a altura (m): "))
    peso = float(input("Informe o peso (kg): "))
    sexo = input("Informe o sexo (M/F): ")
    p1 = Pessoa(altura,peso,sexo)
    p1.imprime_dados()
