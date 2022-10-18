class Pessoa:
    def __init__(self, linha):
        self.deserializar(linha)

    def deserializar(self, linha):
        dados = linha.split(';')
        self._nome = dados[0]
        self._sexo = dados[1]
        self._idade = int(dados[2])
        self._altura = float(dados[3])

    def exibe_dados(self):
        print('Nome:', self._nome)
        print('Sexo:', self._sexo)
        print('Idade:', self._idade)
        print('Altura:', self._altura)

if __name__ == '__main__':
    arq = open('pessoa.txt')
    arq.readline() # Descarta o cabeçalho do arquivo
    linha = arq.readline()
    while linha != "":
        p = Pessoa(linha)
        p.exibe_dados()
        linha = arq.readline()
        print("")
        # ou dentro do while: pessoas.append(Pessoa(linha)
        # linha = arq.readline()
    arq.close()
