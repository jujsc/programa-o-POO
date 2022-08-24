
class Pessoa():
    def __init__(self, nome, sexo, cor_olhos, pai = None, mae = None): #self referencia ao objeto que está disparando 
        self._nome = nome
        self._sexo = sexo
        self._cor_olhos = cor_olhos
        self._pai = pai
        self._mae = mae 

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
        if self._sexo == "F" and pai._sexo == "M":
            if self._cor_olhos == "C" and pai._cor_olhos == "C":
                cor_olhos = "C"
            if self._cor_olhos == "C" and pai._cor_olhos == "A":
                cor_olhos = "C"
            if self._cor_olhos == "C" and pai._cor_olhos == "V":
                cor_olhos = "C"
            if self._cor_olhos == "V" and pai._cor_olhos == "C":
                cor_olhos = "C"
            if self._cor_olhos == "A" and pai._cor_olhos == "C":
                cor_olhos = "C"
            if self._cor_olhos == "A" and pai._cor_olhos == "A":
                cor_olhos = "A"
            if self._cor_olhos == "V" and pai._cor_olhos == "V":
                cor_olhos = "V"
            if self._cor_olhos == "V" and pai._cor_olhos == "A":
                cor_olhos = "V"
            if self._cor_olhos == "A" and pai._cor_olhos == "V":
                cor_olhos = "V"
            p3 = Pessoa(nome,sexo,cor_olhos,pai._nome,self._nome)
            p3._nome = nome
            p3._sexo = sexo
            p3._pai = pai
            p3._cor_olhos = cor_olhos
            p3.imprime_dados()
        else:
            print("Impossível gerar pessoa.")
        
if __name__ == '__main__':
    p1 = Pessoa('Roger', 'M', "C")
    p1.imprime_dados()
    print("-"*30)
    p1.gera_pessoa('José', 'M',p1)
    print("-"*30)
    p2 = Pessoa('Maria', 'F', 'C')
    p2.imprime_dados()
    print("-"*30)
    p2.gera_pessoa('José', 'M', p1)
    print("-"*30)
    p2.gera_pessoa('Rafaela', 'F', p1)

    