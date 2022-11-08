import os

class Veiculo:
    def __init__(self, codigo=0, fabricante=0, ano=0, cor=0, modelo=0, preco=0):
        self._codigo = codigo
        self._fabricante = fabricante
        self._ano = ano
        self._cor = cor
        self._modelo = modelo
        self._preco = preco
    
    def serializar(self):
        return f'\n{self._codigo}    {self._fabricante}    {self._modelo}    {self._ano}    {self._cor}    {self._preco}'
    
    def deserializar(self, linha):
        dados = linha.split('    ')
        self._codigo = dados[0]
        self._fabricante = dados[1]
        self._ano = int(dados[2])
        self._cor = dados[3]
        self._modelo = dados[4]
        self._preco = float(dados[5])
    
    def get_preco(self):
        return self._preco
    
    def get_cor(self):
        return self._cor

    def exibe_dados(self):
        print('Código:', self._codigo)
        print('Fabricante:', self._fabricante)
        print('Ano:', self._ano)
        print('Cor:', self._cor)
        print('Modelo:', self._modelo)
        print('Preço:', self._preco)

def menu():
        print("Menu")
        print("1 - Cadastrar")
        print("2 - Listar tudo")
        print("3 - Listar por cor")
        print("4 - Listar por preço")
        print("5 - Sair")
        opcao = input("Insira sua opção: ")
        return opcao

if __name__ == '__main__':
    opcao = ''
    carros = list()
    arq = "veiculos.txt"
    if os.path.isfile(arq):
        arq = open('veiculos.txt', 'r' )
        linha = arq.readline()
        linha = arq.readline()
        while linha != '':
            carro = Veiculo()
            carro.deserializar(linha)
            carros.append(carro)
            linha = arq.readline()
        arq.close()
        pass
    else:
        arq = open('veiculos.txt', 'w')
        arq.write('codigo    fabricante    ano    cor    modelo    preco')
        arq.close()
    while opcao != "5":
        opcao = menu()
        if opcao == "1":
            print("Vamos cadastrar seu veículo")
            codigo = input("Insira o código do veículo: ")
            fabricante = input("Insira o fabricante do veículo: ")
            ano = int(input("Insira o ano do veículo: "))
            cor = input("Insira a cor do veículo: ")
            modelo = input("Insira o modelo do veículo: ")
            preco = float(input("Insira o preço do veículo: "))
            carro = Veiculo(codigo,fabricante,ano,cor,modelo,preco)
            carros.append(carro)
            arq = open('carros.txt', 'a' )
            arq.write(carro.serializar())
            arq.close()
            print("Veículo cadastrado com sucesso")
        if opcao == "2":
            car =1
            for carro in carros:
                print(f'Carro n° {car}\n')
                carro.exibe_dados()
                car+=1
        if opcao == "3":
            cont=0
            color = str(input("Insira a cor de sua preferência: "))
            for carro in carros:
                if carro.get_cor() == color:
                    print("Carros com cor", color)
                    carro.exibe_dados()
                    cont+=1
            if cont==0:
                print("Nos registros não há veículos com esta cor!")
        if opcao == "4":
            cont=0
            preco_min = float(input("Insira o valor mínimo na sua busca de carros: R$"))
            preco_max = float(input("Insira o valor máximo na sua busca de carros: R$"))
            for carro in carros:
                if (carro.get_preco() >= preco_min) & (carro.get_preco() <= preco_max):
                    cont+=1
                    carro.exibe_dados()
            if cont==0:
                print("Nos registros não há veículos entre essa faixa de valores")
