import os


class Pessoa:
    def __init__(self, id=None, nome=None, sexo=None, pets=None):
        self._id = id
        self._nome = nome
        self._sexo = sexo
        self._pets = []
    
    def get_id(self):
        return self._id
    
    def set_pet(self,pet):
        self._pets.append(pet)
    #faze akgo como se fosse um for para pets, #pets append in the set pets
    def get_name(self):
        return self._nome

    def serializar(self):
        return f'\n{self._id()};{self._nome};{self._sexo};{self._pets}'

    def deserializar(self, linha):
        dados = linha.split(';')
        self._id = int(dados[0])
        self._nome = dados[1]
        self._sexo = dados[2]
        self._pet = list(localiza_pet(int(dados[3])))

    def exibe_dados(self):
        print('* Pessoa *')
        print('Id:', self._id)
        print('Nome:', self._nome)
        print('Sexo:', self._sexo)
        print('* Pets *')
        cont=0
        for pet in self._pets:
            pet.exibe_dados()
            cont+=1
            print()
        if cont==0:
            print('Desconhecido')
        print()

class Pet:
    def __init__(self, id, nome, sexo, tipo):
        self._id = id
        self._nome = nome
        self._sexo = sexo
        self._tipo = tipo

    def serializar(self):
        return f'\n{self._id()};{self._nome};{self._sexo};{self._tipo}'

    def deserializar(self, linha):
        dados = linha.split(';')
        self._id = int(dados[0])
        self._nome = dados[1]
        self._sexo = dados[2]
        self._tipo = dados[3]

    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self._nome
    
    def get_tipo(self):
        return self._tipo

    def exibe_dados(self):
        print('Id:', self._id)
        print('Nome:', self._nome)
        print('Sexo:', self._sexo)
        print('Tipo:', self._tipo)

def localiza_pet(id):
    for pet in pets:
        if pet.get_id() == id:
            return pet
    return None

def localiza_pett(nome):
    for pet in pets:
        if pet.get_nome() == nome:
            return pet
    return None

def localiza_pessoa(nome):
    for pessoa in pessoas:
        if pessoa.get_nome() == nome:
            return pessoa
    return None


def menu():
    print("Menu")
    print("1 - Cadastrar Pet")
    print("2 - Cadastrar Pessoa")
    print("3 - Adotar")
    print("4 - Listar tudo")
    print("5 - Listar por tipo de Pet")
    print("6 - Salvar")
    print("7 - Carregar")
    print("8 - Sair")
    opcao = input("Insira sua opção: ")
    return opcao

if __name__ == '__main__':
    pets = pessoas = []
    id1 = id2 = 0
    escolha = ''
    while escolha != "8":
        escolha = menu()
        if escolha == "1":
            nome_pet = input("Informe o nome do pet: \n")
            sexo_pet = input("Informe o sexo do pet: \n")
            tipo_pet = input("Informe o tipo do pet (Ex.: cão): \n")
            id1 +=1
            pet = Pet(id1, nome_pet, sexo_pet, tipo_pet)
            pets.append(pet)
        if escolha == "2":
            nome = input("Informe o nome da pessoa: \n")
            sexo = input("Informe o sexo da pessoa: \n")
            id2 +=1
            pessoa = Pessoa(id2, nome, sexo)
            pessoas.append(pessoa)
        if escolha == "3":
            print("Adoção")
            dog = people= False
            #associacao pet e pessoa1
            nome_pessoa = input("Informe o nome da pessoa: \n")
            nome_do_pet = input("Informe o nome do pet: \n")
            pet = localiza_pett(nome_do_pet)
            pessoa = localiza_pessoa(nome_pessoa)
            if pet != None and pessoa != None:
                pessoa.set_pet(pet)
                print("Adoção realizada com sucesso")
                print()
            else:
                print("Não foi possível fazer a adoção")
        if escolha == "4":
            for pessoa in pessoas:
                pessoa.exibe_dados()
                print()
        if escolha == "5":
            tipo_informado = input("Qual tipo de pet deseja ver: \n")
            for pessoa in pessoas:
                if tipo_informado == pet.get_tipo():
                    print("Tipo de pet", tipo_informado)
                    print("Nome pet:", pet.get_nome()," - Nome pessoa", pessoa.get_name())
        if escolha == "6":
            arq = open('veiculos.txt', 'w')
            arq.write('Nome;Sexo;Pet')
            for pessoa in pessoas:
                arq.write(pessoa.serializar())
            arq.close()
        if escolha == "7":
            if os.path.isfile(arq):
                arq = open('veiculos.txt', 'r' )
                linha = arq.readline()
                linha = arq.readline()
                while linha != '':
                    pessoa = Pessoa()
                    pessoa.deserializar(linha)
                    pessoas.append(pessoa)
                    linha = arq.readline()
                arq.close()
        