class Veiculo:
    def __init__(self ):
        self._codigo = ""
        self._fabricante = ""
        self._ano = 0
        self._cor = ""
        self._modelo = ""
        self._preco = 0.0
    
    
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


    def menu(self):
        print("Menu")
        print("1 - Cadastrar")
        print("2 - Listar tudo")
        print("3 - Listar por cor")
        print("4 - Listar por preço")
        opcao = input("Insira sua opção: ")
        if opcao == "1":
            self.cadastrar()
            print("Veículo cadastrado com sucesso")
        if opcao == "2":
            self.listar_tudo()
            #mostra todos os veículos armazenados no arquivo, instanciando cada objeto e chamando o método exibe_dados()
        if opcao == "3":
            self.listar_cor()
            #Listar por cor: pede para o usuário informar uma cor, e exibe todos os dados dos veículos com a cor informada
        if opcao == "4":
            self.listar_preco()
        
    
    def cadastrar(self):
        print("Vamos cadastrar seu veículo")
        self._codigo = input("Insira o código do veículo: ")
        self._fabricante = input("Insira o fabricante do veículo: ")
        self._ano = int(input("Insira o ano do veículo: "))
        self._cor = input("Insira a cor do veículo: ")
        self._modelo = input("Insira o modelo do veículo: ")
        self._preco = float(input("Insira o preço do veículo: "))
        with open('veiculos.txt','a') as arquivo:
            arquivo.write(self.serializar())
    
    def listar_tudo(self):
        # lendo tudo porém n sei se está lendo oobjeto
        arq = open('veiculos.txt')
        arq.readline() # Descarta o cabeçalho do arquivo
        linha = arq.readline()
        while linha != "":
            self.deserializar(linha)
            self.exibe_dados()
            linha = arq.readline()
            print("")
        arq.close()
    
    def listar_cor(self):
        cont=0
        color = str(input("Insira a cor de sua preferência: "))
        arq = open('veiculos.txt')
        arq.readline() # Descarta o cabeçalho do arquivo
        linha = arq.readline()
        while linha != "":
            self.deserializar(linha)
            if color in linha:
                cont+=1
                self.exibe_dados()
            linha = arq.readline()
            print("")
        arq.close()
        if cont==0:
            print("Nos registros não há veículos com esta cor!")

    def listar_preco(self):
        cont=0
        preco_min = float(input("Insira o valor mínimo na sua busca de carros: R$"))
        preco_max = float(input("Insira o valor máximo na sua busca de carros: R$"))
        arq = open('veiculos.txt')
        arq.readline() # Descarta o cabeçalho do arquivo
        linha = arq.readline()
        while linha != "":
            self.deserializar(linha)
            if (self._preco >= preco_min) & (self._preco <= preco_max):
                cont+=1
                self.exibe_dados()
            linha = arq.readline()
            print("")
        arq.close()
        if cont==0:
            print("Nos registros não há veículos entre essa faixa de valores")


    def exibe_dados(self):
        print('Código:', self._codigo)
        print('Fabricante:', self._fabricante)
        print('Ano:', self._ano)
        print('Cor:', self._cor)
        print('Modelo:', self._modelo)
        print('Preço:', self._preco)

if __name__ == '__main__':
    V= True
    arq = open('veiculos.txt', 'w')
    arq.write('codigo    fabricante    ano    cor    modelo    preco')
    arq.close()
    while V:
        v = Veiculo()
        v.menu()
        cont = input("Deseja continuar: (S/N) ")
        if cont in "Nn":
            V = False
    '''arq = open('veiculos.txt')
    arq.readline() # Descarta o cabeçalho
    v = Veiculo(arq.readline())
    arq.close()
    v.exibe_dados()'''