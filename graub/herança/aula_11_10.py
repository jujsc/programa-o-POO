class Pessoa:
    def __init__(self, nome, endereco):
        self._nome = nome
        self.__endereco = endereco

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_endereco(self):
        return self.__endereco
    
    def set_endereco(self, endereco):
        self.__endereco = endereco

    def salvar(self):
        print('[SALVANDO]\nNome:',self._nome,'\nEndereço:',self.__endereco)

class PessoaFisica(Pessoa):
    def __init__(self, nome, endereco, cpf, dtNascimento):
        super().__init__(nome, endereco)
        self.__cpf = cpf
        self.__dtNascimento = dtNascimento
    
    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_dtNascimento(self):
        return self.__dtNascimento

    def set_dtNascimento(self, dtNascimento):
        self.__dtNascimento = dtNascimento

    def salvar(self):
        #print('[SALVANDO]\nNome:',self._nome,'\nEndereço:',self.get_endereco())
        super().salvar()
        print('[SALVANDO PESSOA FÍSICA]\nCPF:',self.__cpf,'\nData de nascimento:',self.__dtNascimento)

if __name__ == '__main__':
    p = Pessoa('Mateus', 'Endereco do Mateus')
    p.salvar()
    pf = PessoaFisica('Petronio', 'Endereco do Petronio', 'CPF do Petronio', 'Nascimento do Petronio')
    pf.salvar()

    pessoas = []
    pessoas.append(
        Pessoa('Nome Geral', 'Endereço Geral'))
    pessoas.append(
        PessoaFisica('Fulano de Tal', 'Rua A, 123', '458.245.123-47', '03/08/2000'))
    pessoas.append(
        PessoaFisica('Acme Corp.', 'Rua B, 456', '93.479.720/0001-73', '15/10/2012'))
    pessoas.append(
        Pessoa('Nome da segunda pessoa', 'Endereço da segunda pessoa'))

    for pessoa in pessoas:
        if isinstance(pessoa, Pessoa):
            print(pessoa.get_cpf())
            print()
