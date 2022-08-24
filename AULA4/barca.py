#a barca que tem conexão com o veiculo, na barca ter a variavel veiculo

class Veiculo:
    def __init__(self, tipo, peso):
        self._tipo = tipo
        self._peso = peso

    def set_tipo(self, tipo):
        tipo = tipo.upper()
        if tipo in 'CMV':
            self._tipo = tipo
        else:
            print("Veículo inapropriado! Os veículos apropriados são carro, moto e van.")
    
    def set_peso(self, peso):
        print("Insira o peso do veículo em kg!")
        self._peso = peso

    def get_tipo(self):
         return self._tipo

    def get_peso(self):
            return self._peso

   


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
    
    # Instancia um objeto "Pessoa" com "Carro"
    pessoa = Pessoa('Dick Vigarista', 'Masculino', 42, carro)
    
    # Exibe os dados da pessoa e do carro
    pessoa.exibe_dados()

    # Altera dados do carro diretamente no objeto
    carro.set_fabricante('Chevrolet')
    carro.set_modelo('Chevette')

    # Altera dados do carro através da associação
    pessoa.get_carro().set_ano(1979)

    # Exibe os dados da pessoa e do carro
    pessoa.exibe_dados()

    print()