from distutils import core


class Veiculo:
    def __init__(self, codigo, fabricante, modelo, ano, cor, preco ):
        self._codigo = codigo
        self._fabricante = fabricante
        self._ano = ano
        self._cor = cor
        self._modelo = modelo
        self._preco = preco
    
    def serializar(self):
        return f'\n{self._codigo}<tab>{self._fabricante}<tab>{self._modelo}<tab>{self._ano}<tab>{self._cor}<tab>{self._preco}'
    
    def deserializar(self, linha):
        dados = linha.split('   ')
        self._codigo = dados[0]
        self._fabricante = dados[1]
        self._ano = int(dados[2])
        self._cor = dados[3]
        self._modelo = dados[4]
        self._preco = dados[5]


    def menu(self):
        print("Menu")
        print("1 - Cadastrar")
        print("2 - Listar tudo")
        print("3 - Listar por cor")
        print("4 - Listar por preço")
        opcao = print(input("Insira sua opção: "))
        if opcao == "1":
            self.cadastrar()
        if opcao == "2":
            #listar tudo
            #mostra todos os veículos armazenados no arquivo, instanciando cada objeto e chamando o método exibe_dados()
        if opcao == "3":
            #listar por cor
            #Listar por cor: pede para o usuário informar uma cor, e exibe todos os dados dos veículos com a cor informada
        if opcao == "4":
            #Listar por preço: pede para o usuário informar um preço inicial e um final, e exibe todos os dados dos veículos com o preço dentro da faixa informada
        else:
            print("Opção Inválida, tente novamente!")
    
    def cadastrar(self):
        print("Vamos cadastrar seu veículo")
        codigo = input("Insira o código do veículo: ")
        fabricante = input("Insira o fabricante do veículo: ")
        ano = input("Insira o ano do veículo: ")
        cor = input("Insira a cor do veículo: ")
        modelo = input("Insira o modelo do veículo: ")
        preco = input("Insira o preço do veículo: ")
        v = Veiculo(codigo,fabricante,ano,cor,modelo,preco)
        arq = open('veiculos.txt', 'w')
        arq.write('codigo;fabricante;ano;cor;modelo;preco')
        arq.write(v.serializar())
        arq.close()

    def exibe_dados(self):
        print('Código:', self._codigo)
        print('Fabricante:', self._fabricante)
        print('Ano:', self._ano)
        print('Cor:', self._cor)
        print('Modelo:', self._modelo)
        print('Preço:', self._preco)

if __name__ == '__main__':
    