class Pessoa:
  def __init__(self, linha):
    self.deserializar(linha)

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
    if self._pet:
      self._pet.exibe_dados()
    else:
        print('Desconhecido')
    print()

class Pet:
  def __init__(self, linha):
    self.deserializar(linha)

  def deserializar(self, linha):
    dados = linha.split(';')
    self._id = int(dados[0])
    self._nome = dados[1]
    self._sexo = dados[2]
    self._tipo = dados[3]

  def get_id(self):
    return self._id+1

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

if __name__ == '__main__':
    pets = []
    pessoas = []
    cont = True
    print("Vamos cadastrar seus pets!")
    while cont:
        nome_pet = input("Informe o nome do seu pet: \n")
        nome_sexo = input("Informe o sexo do seu pet: \n")
        nome_tipo = input("Informe o tipo do seu pet (Ex.: cão): \n")
        continuar = input("Você tem outros pets para cadastrar: (S ou N) ")
        arq = open('pets.txt')
        arq.readline()            # Descarta o cabeçalho do arquivo
        for linha in arq:         # Instancia os objetos
            pets.append(Pet(linha.strip("-")))
        # chama metodo para cadastrar o pet
        if continuar in "Nn":
            cont = 0
        arq.close()
    
    nome_pessoa = ("Informe seu nome: \n")
    sexo_pessoa = input("Informe seu sexo: \n")
    # associação entre pet e pessoa, adoção do pet pela pessoa

    arq = open('pets.txt')
    arq.readline()            # Descarta o cabeçalho do arquivo
    for linha in arq:         # Instancia os objetos
        pets.append(Pet(linha.strip()))
    arq.close()

    arq = open('pessoas.txt')
    arq.readline()            # Descarta o cabeçalho do arquivo
    for linha in arq:         # Instancia os objetos
        pessoas.append(Pessoa(linha.strip()))
    arq.close()

    for pessoa in pessoas:
        pessoa.exibe_dados() # Exibe os dados dos objetos
