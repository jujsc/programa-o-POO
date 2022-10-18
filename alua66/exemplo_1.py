class Pessoa:
    def __init__(self, nome, sexo, idade, altura):
        self._nome = nome
        self._sexo = sexo
        self._idade = idade
        self._altura = altura

    def serializar(self):
        return f'\n{self._nome};{self._sexo};{self._idade};{self._altura}'

if __name__ == '__main__':
    p1 = Pessoa('Pedro', 'M', 42, 1.76)
    p2 = Pessoa('Pedro', 'M', 42, 1.76)
    p3 = Pessoa('Pedro', 'M', 42, 1.76) #ou
    pessoas = list()
    pessoas.append(Pessoa('Pedro', 'M', 42, 1.76))
    pessoas.append(Pessoa('Pedro', 'M', 42, 1.76)
)
    for i in pessoas:
        arq.write(i.serializar())
    arq = open('pessoa.txt', 'w')
    # Escreve o cabeçalho do arquivo
    arq.write('nome;sexo;idade;altura')
    # Escreve os dados da pessoa
    arq.write(p.serializar())
    arq.close()
