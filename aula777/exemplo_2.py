class Pessoa:
  def __init__(self, linha):
    self.deserializar(linha)

  def deserializar(self, linha):
    dados = linha.split(';')
    self._id = int(dados[0])
    self._nome = dados[1]
    self._sexo = dados[2]
    self._pet = localiza_pet(int(dados[3]))

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
  def __init__(self, linha):
      self.deserializar(linha)

  def deserializar(self, linha):
    dados = linha.split(';')
    self._id = int(dados[0])
    self._nome = dados[1]
    self._sexo = dados[2]
    self._tipo = dados[3]

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

if __name__ == '__main__':
  pets = []
  pessoas = []

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