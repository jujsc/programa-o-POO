class Pessoa:
    def __init__(self, linha):
        self.deserializar(linha)

    def deserializar(self, linha):
        dados = linha.split(';')
        self._nome = dados[0]
        self._sexo = dados[1]
        self._idade = dados[2]
        self._altura = dados[3]

    def exibe_dados(self):
        print('Nome:', self._nome)
        print('Sexo:', self._sexo)
        print('Idade:', self._idade)
        print('Altura:', self._altura)

if __name__ == '__main__':
    arq = open('pessoa.txt')
    arq.readline() # Descarta o cabeçalho do arquivo
    p = Pessoa(arq.readline())
    p.exibe_dados()
    arq.close()
