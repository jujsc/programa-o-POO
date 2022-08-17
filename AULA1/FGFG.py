class Pessoa():
    def __init__(self, nome, sexo, cor_olhos, pai = None, mae = None): #self referencia ao objeto que está disparando 
        self._nome = nome
        self._sexo = sexo
        self._cor_olhos = cor_olhos
        self._pai = pai
        self._mae = mae 
        #print(f'Criada pessoa "{self._nome}" com sexo "{self._sexo}"')

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

    '''def set_nome(self, nome):
        if len(nome) < 3:
            print('Nome deve conter pelo menos 3 letras')
        else:
            self._nome = nome'''

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
        print("Nome: ", self._nome())
        print("Sexo: ", self._sexo())
        print("Cor dos olhos: ", self._cor_olhos())
        if self._pai == None:
            print("Pai: Desconhecido")
        else:
            print("Pai: ", self._pai())
        if self._mae == None:
            print("Mãe: Desconhecido")
        else:
            print("Mãe: ", self.mãe())
        
#PESSOA NÃO TEM PAI E MÃE, POR COMO DESCONHECIDO (IFS)
if __name__ == '__main__':
    p1 = Pessoa("Julia","F","C")
    p1.imprime_dados()