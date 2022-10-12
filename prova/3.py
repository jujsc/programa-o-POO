class Produto:
    def __init__(self,nome,valor):
        self._nome = nome
        self._valor = valor

    def get_nome(self):
         return self._nome

    def get_valor(self):
        return self._valor

class Compra:
    def __init__(self,quantidade,valor_total):
        self._quantidade = quantidade
        self._valor_total = valor_total
        self._valor_maximo =0
        self._nome_max = ""

    def adicionar(self,produto):
        self._quantidade +=1
        self._valor_total = self._valor_total + produto.get_valor()
    
    def valor_maximo(self, produto):
        self._valor_maximo = produto.get_valor()
        self._nome_max = produto.get_nome()
        if produto.get_valor() > self._valor_maximo:
            self._valor_maximo = produto.get_valor() 
            self._nome_max = produto.get_nome()
    
    def extrato(self):
        print("-"*30)
        print("Sua Compra:")
        print("-"*30)
        print(f'Quantidade de produtos comprados: {self._quantidade}')
        print("-"*30)
        print(f'Valor total da compra: R${self._valor_total:.2f}')
        print("-"*30)
        print(f'Produto mais caro foi {self._nome_max} com o valor de R${self._valor_maximo:.2f}')
        print("-"*30)

if __name__ == "__main__":
    comprar = True
    c = Compra(0,0)
    while comprar:
        nome = input("Insira o nome do produto: ")
        valor = float(input("Insira o valor do produto: R$"))
        p = Produto(nome,valor)
        c.adicionar(p)
        c.valor_maximo(p)
        continuar = input("Deseja continuar: S ou N  \n")
        if continuar.upper() != "S":
            c.extrato()
            comprar = False
    