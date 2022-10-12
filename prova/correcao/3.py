class Produto:
    def __init__(self,nome,valor):
        self._nome = nome
        self._valor = valor

    def get_nome(self):
         return self._nome

    def get_valor(self):
        return self._valor

class Compra:
    def __init__(self):
        self._quantidade = 0
        self._valor_total = 0.0
        self._produto_mais_caro = None

    def adicionar(self,produto):
        if self._produto_mais_caro == None:
            self._produto_mais_caro = produto
        elif produto.get_valor() > self._produto_mais_caro.get_valor():
            self._produto_mais_caro = produto

        self._quantidade +=1
        self._valor_total += produto.get_valor()
    
    def extrato(self):
        print("-"*30)
        print("Sua Compra:")
        print("-"*30)
        print(f'Quantidade de produtos comprados: {self._quantidade}')
        print("-"*30)
        print(f'Valor total da compra: R${self._valor_total:.2f}')
        print("-"*30)
        print(f'Produto mais caro foi {self._produto_mais_caro.get_nome()} com o valor de R${self._produto_mais_caro.get_valor():.2f}')
        print("-"*30)

if __name__ == "__main__":
    continuar = 's'
    c = Compra()
    while continuar in 'Ss':
        nome = input("Insira o nome do produto: ")
        valor = float(input("Insira o valor do produto: R$"))
        c.adicionar(Produto(nome,valor))
        continuar = input("Deseja continuar? S ou N  \n")
    c.extrato()
    