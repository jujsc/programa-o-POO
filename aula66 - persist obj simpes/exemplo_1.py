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
    p2 = Pessoa('Marcio', 'M', 50, 1.86)
    p3 = Pessoa('Maria', 'F', 32, 1.70) #ou
    #pessoas = list()
    #pessoas.append(Pessoa('Pedro', 'M', 42, 1.76))
    #pessoas.append(Pessoa('Pedro', 'M', 42, 1.76)
    #for i in pessoas:
    #    arq.write(i.serializar())
    arq = open('pessoa.txt', 'w')
    # Escreve o cabeçalho do arquivo
    arq.write('nome;sexo;idade;altura')
    # Escreve os dados da pessoa
    arq.write(p1.serializar())
    arq.write(p2.serializar())
    arq.write(p3.serializar())
    #COMO EM UMA CLASSE EU POSSO LER E ESCREVER DO ARQUIVO, COMO FAZ A COMPATIBLIDADE

    arq.close()
