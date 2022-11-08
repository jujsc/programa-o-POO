import os

class Carro:
    def __init__(self,codigo=0,fabricante=0,modelo=0,ano=0,cor=0,preco=0):
        self._codigo = codigo
        self._fabricante = fabricante
        self._modelo = modelo
        self._ano = ano
        self._cor = cor
        self._preco = preco
    
    def get_codigo(self):
        return self._codigo
    
    def get_fabricante(self):
        return self._fabricante
    
    def get_modelo(self):
        return self._modelo
    
    def get_ano(self):
        return self._ano
    
    def get_cor(self):
        return self._cor
    
    def get_preco(self):
        return self._preco
    
    def serializar(self):
        return f'\n{self._codigo}\t{self._fabricante}\t{self._modelo}\t{self._ano}\t{self._cor}\t{self._preco}'
    
    def deserializar(self,linha):
        dados = linha.split('\t')
        self._codigo = dados[0]
        self._fabricante = dados[1]
        self._modelo = dados[2]
        self._ano = dados[3]
        self._cor = dados[4]
        self._preco = dados[5]

    def exibe_dados(self):
        print('Código:', self._codigo)
        print('Fabricante:', self._fabricante)
        print('Modelo:', self._modelo)
        print('Ano:', self._ano)
        print('Cor:', self._cor)
        print('Preço:', self._preco)

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1 - Cadastrar")
    print("2 - Listar tudo")
    print("3 - Listar por cor")
    print("4 - Listar por preço")
    print("0 - Sair")
    item = input('\nDigite sua escolha: ')
    return item

if __name__ == '__main__':
    
    escolha = ""
    carros = list()
    arq = 'carros.txt'
    if os.path.isfile(arq):
        arq = open('carros.txt', 'r' )
        linha = arq.readline()
        linha = arq.readline()
        while linha != '':
                carro = Carro()
                carro.deserializar(linha)
                carros.append(carro)
                linha = arq.readline()
        arq.close()
        pass
    else: 
        # print('o arquivo não existe')
        arq = open('carros.txt', 'w')
        arq.write('codigo\tfabricante\tmodelo\tano\tcor\tpreco')
        arq.close()
    while escolha != '0':
        escolha = menu()
        if escolha == "1":

            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n1 - Cadastrar\n")
            codigo = input('Informe o código do veículo: ')
            fabricante = input('Informe o fabricante do veículo: ')
            modelo = input('Informe o modelo do veículo: ')
            ano = input('Informe o ano do veículo: ')
            cor = input('Informe a cor do veículo: ')
            preco = input('Informe o preço do veículo: ')
            carro = Carro(codigo,fabricante,modelo,ano,cor,preco)
            carros.append(carro)
            arq = open('carros.txt', 'a' )
            arq.write(carro.serializar())
            arq.close()

            os.system('cls' if os.name == 'nt' else 'clear')
            print('Veículo cadastrado!\n')
            input('\nENTER para continuar')


        elif escolha == "2":

            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n2 - Listar tudo\n")
            numero = 1
            for carro in carros:
                print(f'Carro {numero}\n')
                carro.exibe_dados()
                numero+=1
            input('\nENTER para continuar')

        elif escolha == "3":

            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n3 - Listar por cor\n")
            cor_filtro = input('Informe a cor que deseja buscar: ')
            print()
            numero = 1
            for carro in carros:
                if carro.get_cor() == cor_filtro:
                    print(f'Carro {numero}\n')
                    carro.exibe_dados()
                    numero+=1
            input('\nENTER para continuar')

        elif escolha == "4":

            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n4 - Listar por preço\n")
            preco_min = input('Informe o preço mínimo que deseja buscar: ')
            preco_max = input('Informe o preço máximo que deseja buscar: ')
            print()
            numero = 1
            for carro in carros:
                if carro.get_preco() > preco_min and carro.get_preco() < preco_max :
                    print(f'Carro {numero}\n')
                    carro.exibe_dados()
                    numero+=1
            input('\nENTER para continuar')
    
        elif escolha == "0":

            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nPrograma Encerrado\n')