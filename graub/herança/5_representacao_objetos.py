# Representação de Objetos

class Pessoa:
  def __init__(self, nome, endereco):
      self._nome = nome
      self._endereco = endereco

  def __repr__(self):
      return f'{self._nome};{self._endereco}'

  def __str__(self):
      return f'Nome: {self._nome}\nEndereco: {self._endereco}'

class PessoaFisica(Pessoa):
  def __init__(self, nome, endereco, cpf, dt_nascimento):
      super().__init__(nome, endereco)
      self._cpf = cpf
      self._dt_nascimento = dt_nascimento

  def __repr__(self):
    return f'{super().__repr__()};{self._cpf};{self._dt_nascimento}'

  def __str__(self):
    return f'{super().__str__()}\nCPF: {self._cpf}\nNascimento: {self._dt_nascimento}'

class PessoaJuridica(Pessoa):
  def __init__(self, nome, endereco, cnpj, dt_fundacao):
      super().__init__(nome, endereco)
      self._cnpj = cnpj
      self._dt_fundacao = dt_fundacao

  def __repr__(self):
    return f'{super().__repr__()};{self._cnpj};{self._dt_fundacao}'

  def __str__(self):
    return f'{super().__str__()}\nCNPJ: {self._cnpj}\nFundação: {self._dt_fundacao}'

if __name__ == '__main__':
  pessoa = Pessoa('Nome Geral', 'Endereço Geral')
  print()
  print(pessoa)
  print()
  print(repr(pessoa))
  print()

  # pessoas = []
  # pessoas.append(Pessoa('Nome Geral', 'Endereço Geral'))
  # pessoas.append(PessoaFisica('Fulano de Tal', 'Rua A, 123', '458.245.123-47', '03/08/2000'));
  # pessoas.append(PessoaJuridica('Acme Corp.', 'Rua B, 456', '93.479.720/0001-73', '15/10/2012'));

  # for pessoa in pessoas:
  #   print(repr(pessoa))