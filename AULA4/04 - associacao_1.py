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

if __name__ == '__main__':
    # Instancia um objeto "Carro"
    carro = Carro('Ford', 'Bigode', 1938)
    
    # Exibe os dados do carro
    print('\nCarro:',
        carro.get_fabricante(),
        carro.get_modelo(),
        carro.get_ano())

    # Instancia um objeto "Pessoa" sem "Carro"
    pessoa = Pessoa('Dick Vigarista', 'Masculino', 42)

    # Exibe os dados da pessoa
    print('\nPessoa:',
        pessoa.get_nome(),
        pessoa.get_sexo(),
        pessoa.get_idade(),
        pessoa.get_carro())

    print()