class Carro:
    def __init__(self, fabricante, modelo, ano):
        self._fabricante = fabricante
        self._modelo = modelo
        self._ano = ano

    def get_fabricante(self):
            return self._fabricante

    def get_modelo(self):
            return self._modelo

    def get_ano(self):
            return self._ano

    def exibe_dados(self):
        # Exibe os dados do carro
        print('Carro:',
            self.get_fabricante(),
            self.get_modelo(),
            self.get_ano())


class Pessoa:
    def __init__(self, nome, sexo, idade, carro=None):
        self._nome = nome
        self._sexo = sexo
        self._idade = idade
        # Associação - Pessoa "tem um" Carro
        self._carro = carro
    
    def get_nome(self):
        return self._nome

    def get_sexo(self):
        return self._sexo
    
    def get_idade(self):
        return self._idade

    def get_carro(self):
        return self._carro

    def set_carro(self, carro):
        self._carro = carro

    def exibe_dados(self):
        # Exibe os dados da pessoa
        print('\nPessoa:',
            self.get_nome(),
            self.get_sexo(),
            self.get_idade())

        # Exibe os dados do carro da pessoa, caso exista
        if self._carro:
            self._carro.exibe_dados()
        else:
            print('Carro: não definido')


if __name__ == '__main__':
    # Instancia um objeto "Carro"
    carro = Carro('Ford', 'Bigode', 1938)
    
    # Exibe os dados do carro
    carro.exibe_dados()

    # Instancia um objeto "Pessoa" sem "Carro"
    pessoa = Pessoa('Dick Vigarista', 'Masculino', 42)
    
    # Exibe os dados da pessoa e do carro, caso exista
    pessoa.exibe_dados()

    # Associa o carro à pessoa
    pessoa.set_carro(carro)

    # Exibe os dados da pessoa e do carro, caso exista
    pessoa.exibe_dados()

    print()