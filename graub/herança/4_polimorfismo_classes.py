# Polimorfismo de Classes

class Pessoa:
  def __init__(self, nome, endereco):
      self._nome = nome
      self._endereco = endereco

  def exibe_dados(self):
      print()
      print('Nome:', self._nome)
      print('Endereco:', self._endereco)

class PessoaFisica(Pessoa):
  def __init__(self, nome, endereco, cpf, dt_nascimento):
      super().__init__(nome, endereco)
      self._cpf = cpf
      self._dt_nascimento = dt_nascimento

  def exibe_dados(self):
      super().exibe_dados()
      print('CPF:', self._cpf)
      print('Nascimento:', self._dt_nascimento)

class PessoaJuridica(Pessoa):
  def __init__(self, nome, endereco, cnpj, dt_fundacao):
      super().__init__(nome, endereco)
      self._cnpj = cnpj
      self._dt_fundacao = dt_fundacao

  def exibe_dados(self):
      super().exibe_dados()
      print('CNPJ:', self._cnpj)
      print('Fundação:', self._dt_fundacao)

if __name__ == '__main__':
  pessoas = []
  pessoas.append(Pessoa('Nome Geral', 'Endereço Geral'))
  pessoas.append(PessoaFisica('Fulano de Tal', 'Rua A, 123', '458.245.123-47', '03/08/2000'));
  pessoas.append(PessoaJuridica('Acme Corp.', 'Rua B, 456', '93.479.720/0001-73', '15/10/2012'));

  for pessoa in pessoas:
    if isinstance(pessoa, Pessoa):
      pessoa.exibe_dados()