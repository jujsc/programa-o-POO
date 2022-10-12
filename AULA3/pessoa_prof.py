class Pessoa():
    def __init__(self, altura, peso, sexo): #self referencia ao objeto que está disparando 
        self._altura = altura
        self._altura = altura
        self._sexo = sexo

    def set_sexo(self, sexo):
        sexo = sexo.upper()
        if sexo in 'MF':
            self._sexo = sexo
        else:
            print("Sexo deve ser 'M' ou 'F'")

    def set_cor_olhos(self, cor_olhos):
        cor_olhos = cor_olhos.upper()
        if cor_olhos in 'CVA':
            self._cor_olhos = cor_olhos
        else:
            print("Cor dos olhos deve ser 'C', 'V' ou 'A'.")

    def set_nome(self, nome):
        if len(nome) < 3:
            print('Nome deve conter pelo menos 3 letras')
        else:
            self._nome = nome

    def get_nome(self):
        return self._nome
    
    def get_cor_olhos_str(self):
        if self._cor_olhos == 'C':
            return 'Castanho'
        elif self._cor_olhos == 'V':
            return 'Verde'
        elif self._cor_olhos == 'A':
            return 'Azul'
        else:
            return 'Cor dos olhos inválida.'
    
    def get_sexo_str(self):
        if self._sexo == 'F':
            return 'Feminino'
        elif self._sexo == 'M':
            return 'Masculino'
        else:
            return 'Indefinido'
    
    def imprime_dados(self):
        print("Nome:", self._nome)
        print("Sexo:", self.get_sexo_str())
        print("Cor dos olhos:", self.get_cor_olhos_str())
        if self._pai == None:
            print("Pai: Desconhecido")
        else:
            print("Pai:", self._pai._nome)
        if self._mae == None:
            print("Mãe: Desconhecido")
        else:
            print("Mãe:", self._mae)
    
    def gera_pessoa(self, nome, sexo, pai):
        if pai == None:
            print("Pai não informado")
            return None
        if pai._sexo != "M":
            print("Pai obrigatoriamente deve ser do sexo masculino\n")
            return None
        if self._sexo != "F":
            print("Somente pessoas do sexo feminino podem gerar novas pessoas")
            return None

        if self._cor_olhos == "C" or pai._cor_olhos == "C":
            cor_olhos = "C"
        elif self._cor_olhos == "V" and pai._cor_olhos == "V":
            cor_olhos = "V"
        else:
            cor_olhos = "A"
        
        return Pessoa(nome, sexo, cor_olhos, pai, self._nome)

        
if __name__ == '__main__':
    pai = Pessoa('Roger', 'M', "C")
    pai.imprime_dados()
    print("-"*30)
    filho = pai.gera_pessoa('José', 'M',pai)
    if filho:
        filho.imprime_dados()
    print("-"*30)
    mae = Pessoa('Maria', 'F', 'C')
    mae.imprime_dados()
    print("-"*30)
    
    filho = mae.gera_pessoa('José', 'M', pai)
    if filho:
        filho.imprime_dados()
    print("-"*30)
    filha = mae.gera_pessoa('Rafaela', 'F', pai)
    if filha:
        filha.imprime_dados()
