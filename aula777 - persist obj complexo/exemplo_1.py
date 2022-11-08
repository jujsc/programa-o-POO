class Pessoa:
    def __init__(self, id, nome, sexo, pet):
        self._id = id
        self._nome = nome
        self._sexo = sexo
        self._pet = pet

    def serializar(self):
        return f'\n{self._id};{self._nome};{self._sexo};{self._pet.get_id()}'

class Pet:
    def __init__(self, id, nome, sexo, tipo):
        self._id = id
        self._nome = nome
        self._sexo = sexo
        self._tipo = tipo

    def get_id(self):
        return self._id

    def serializar(self):
        return f'\n{self._id};{self._nome};{self._sexo};{self._tipo}'

if __name__ == '__main__':
    pets = []
    pessoas = []

    pets.append(Pet(1, 'Zeca', 'M', 'Pássaro'))
    pets.append(Pet(2, 'Fred', 'M', 'Cão'))
    pets.append(Pet(3, 'Lua', 'F', 'Gato'))

    pessoas.append(Pessoa(1, 'Pedro', 'M', pets[1]))
    pessoas.append(Pessoa(2, 'Maria', 'F', pets[2]))
    pessoas.append(Pessoa(3, 'Roberto', 'M', pets[0]))

    arq = open('pessoas.txt', 'w')
    # Escreve o cabeçalho do arquivo
    arq.write('id;nome;sexo;pet')
    # Escreve os dados das pessoas
    for pessoa in pessoas:
        arq.write(pessoa.serializar())
    arq.close()

    arq = open('pets.txt', 'w')
    # Escreve o cabeçalho do arquivo
    arq.write('id;nome;sexo;tipo')
    # Escreve os dados dos pets
    for pet in pets:
        arq.write(pet.serializar())
    arq.close()