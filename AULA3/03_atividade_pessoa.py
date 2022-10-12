class Pessoa:
    def __init__(self, nome, sexo, cor_olhos, pai=None, mae=None):
        # Código de inicialização do objeto
        self.nome = nome
        self.sexo = sexo
        self.cor_olhos = cor_olhos
        self.pai = pai
        self.mae = mae

    def gera_pessoa(self, nome, sexo, pai):
        if pai == None:
            print('Parâmetro "Pai" não informado')
            return None

        if pai.get_sexo() != 'M':
            print('Parâmetro "Pai" deve ser do sexo masculino\n')
            return None

        if self.sexo != 'F':
            print('Somente pessoas do sexo feminino podem gerar novas pessoas\n')
            return None

        if self.cor_olhos == 'C' or pai.cor_olhos == 'C':
            cor_olhos = 'C'
        elif self.cor_olhos == 'V' or pai.cor_olhos == 'V':
            cor_olhos = 'V'
        else:
            cor_olhos = 'A'

        return Pessoa(nome, sexo, cor_olhos, pai, self)

    def set_sexo(self, sexo):
        if sexo == 'M' or sexo == 'F':
            self.sexo = sexo
        else:
            print("Sexo deve ser 'M' ou 'F'")

    def set_cor_olhos(self, cor_olhos):
        if cor_olhos in 'CVA':
            self.cor_olhos = cor_olhos
        else:
            print("Cor dos olhos deve ser 'C', 'V' ou 'A'")

    def get_nome(self):
        return self.nome

    def get_sexo(self):
        return self.sexo

    def get_sexo_str(self):
        if self.sexo == 'M':
            return 'Masculino'
        else:
            return 'Feminino'

    def get_cor_olhos_str(self):
        if self.cor_olhos == 'C': return 'Castanho'
        if self.cor_olhos == 'V': return 'Verde'
        if self.cor_olhos == 'A': return 'Azul'
        return 'Desconhecido'

    def imprime_dados(self):
        print('Nome:', self.nome)
        print('Sexo:', self.get_sexo_str())
        print('Olhos:', self.get_cor_olhos_str())

        if self.pai == None:
            print('Pai: não informado')
        else:
            print('Pai:', self.pai.get_nome())

        if self.mae == None:
            print('Mãe: não informada')
        else:
            print('Mãe:', self.mae.get_nome())

        print()

if __name__ == '__main__':
    pai = Pessoa("Homer", 'M', 'C')
    mae = Pessoa("Marge", 'F', 'V')

    pai.imprime_dados()
    mae.imprime_dados()

    filho = mae.gera_pessoa("Bart", 'M', pai)
    if filho:
        filho.imprime_dados()

    filha = mae.gera_pessoa("Lisa", 'F', pai);
    if filha:
        filha.imprime_dados()