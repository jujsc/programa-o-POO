class contribuinte:
    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_ano(self, ano):
        self.ano = ano

    def get_ano(self):
        return self.ano
    
    def set_renda(self, renda):
        self.renda = renda

    def get_renda(self):
        return self.renda

    def set_dependentes(self, dependentes):
        self.dependentes = dependentes

    def get_dependentes(self):
        return self.dependentes

    def idade(self):
        return int(2022) - int(self.ano)
    
    def renda_ano(self):
        return self.renda * 13
    
    def renda_per(self):
        if self.dependentes > 0: 
            self.dependentes+=1
            return self.renda / self.dependentes
        else:
            return self.renda 

    def base(self):
        return self.renda - self.dependentes * 189.59
    
    def aliquota(self):
        if self.renda >= 0 and self.renda <=1903.98:
            return 0
        if self.renda >= 1903.99 and self.renda <=2826.65:
            return 0.075
        if self.renda >= 2826.66 and self.renda <=3751.05:
            return 0.15
        if self.renda >= 3751.06 and self.renda <=4664.68:
            return 0.225
        if self.renda >= 4664.69:
            return 0.275
    
    def deducao(self):
        if self.renda >= 0 and self.renda <=1903.98:
            return 0
        if self.renda >= 1903.99 and self.renda <=2826.65:
            return 142.80
        if self.renda >= 2826.66 and self.renda <=3751.05:
            return 354.80
        if self.renda >= 3751.06 and self.renda <=4664.68:
            return 636.13
        if self.renda >= 4664.69:
            return 869.36
    
    def imposto(self):
        if self.renda <=1903.98:
            return 0
        else: 
            return self.base() * self.aliquota() - self.deducao()

c = contribuinte()
c.set_nome(input("Insira seu nome: "))
c.set_ano(input("Insira seu ano de nascimento: "))
c.set_renda(float(input("Insira sua renda mensal: R$")))
c.set_dependentes(int(input("Insira o número de dependentes: ")))

print(50*"-")
print(f'Seu nome é {c.get_nome()}. Você nasceu em {c.get_ano()}. Sua renda mensal é R${c.get_renda()} e você possui {c.get_dependentes()} dependente(s).')
print(50*"-")
print(f'Você tem {c.idade()} anos. Sua renda anual é R${c.renda_ano()} e per capita mensal de R${c.renda_per()}.')
print(50*"-")
print(f'Sua base de cálculo é R${c.base():.2f}. Sua aliquota é {c.aliquota() * 100:.2f}%. Sua Dedução é R${c.deducao()}')
print(50*"-")
print(f'Sua contribuição IR é R${c.imposto():.2f}')