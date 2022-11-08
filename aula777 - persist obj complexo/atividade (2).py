import os
class Pessoa:
  def __init__(self,id=None,nome=None,sexo=None):
    self._id = id
    self._nome = nome
    self._sexo = sexo


  def deserializar(self, linha):
    dados = linha.split(';')
    self._id = int(dados[0])
    self._nome = dados[1]
    self._sexo = dados[2]
    self._pet = localiza_pet(int(dados[3]))
    return self

  def exibe_dados(self):
    print('* Pessoa *')
    print('Id:', self._id)
    print('Nome:', self._nome)
    print('Sexo:', self._sexo)
    print('* Pet *')
    if self._pet:
      self._pet.exibe_dados()
    else:
        print('Desconhecido')
    print()

class Pet:
  def __init__(self, id=None,nome=None,sexo=None,tipo=None):
        self._id = id
        self._nome = nome
        self._sexo = sexo
        self._tipo = tipo

  def deserializar(self, linha):
    dados = linha.split(';')
    self._id = int(dados[0])
    self._nome = dados[1]
    self._sexo = dados[2]
    self._tipo = dados[3]
    return self

  def get_id(self):
    return self._id

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

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('1 - Cadastrar pet')
    print('2 - Cadastrar pessoa')
    print('3 - Adotar')
    print('4 - Listar tudo')
    print('5 - Listar por tipo de pet')
    print('6 - Salvar')
    print('7 - Carregar')
    print('0 - Sair')
    item = input("\nDigite sua escolha: ")
    return item

if __name__ == '__main__':
    pets = []
    pessoas = []
    escolha = 0
    while escolha != "0":
        escolha = menu()
        if escolha == '1':
            print('Informe os dados do pet')
            nome = input('Nome: ')
            sexo = input('Sexo: ')
            tipo = input('Tipo: ')
            arq = open('pets.txt','r')
            linha = arq.readline()
            while linha != '':
                linha = arq.readline()
                id = linha[0]
            id += 1
            pet = Pet(id,nome,sexo,tipo)
            pets.append(pet)

        if escolha == '2':
            print('Informe os dados do pet')
            nome = input('Nome: ')
            sexo = input('Sexo: ')
            arq = open('pessoas.txt','r')
            linha = arq.readline()
            while linha != '':
                linha = arq.readline()
                id = linha[0]
            id += 1
            pessoa = Pessoa(id,nome,sexo,tipo)
            pessoas.append(pessoa)

        if escolha == '3':
            pass
        if escolha == '4':
            pass
        if escolha == '5':
            pass
        if escolha == '6':
            pass
        if escolha == '7':
            pass
        if escolha == '0':
            pass








# pets.append(Pet().deserializar(linha))




#   arq = open('pets.txt')
#   arq.readline()            # Descarta o cabeçalho do arquivo
#   for linha in arq:         # Instancia os objetos
#     pets.append(Pet(linha.strip()))
#   arq.close()

#   arq = open('pessoas.txt')
#   arq.readline()            # Descarta o cabeçalho do arquivo
#   for linha in arq:         # Instancia os objetos
#     pessoas.append(Pessoa(linha.strip()))
#   arq.close()

#   for pessoa in pessoas:
#       pessoa.exibe_dados() # Exibe os dados dos objetos