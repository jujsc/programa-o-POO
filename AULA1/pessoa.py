class Pessoa:
    def tamanho_do_nome(self):
        return len(self.nome)

    def tamanho_do_sobrenome(self):
        return len(self.sobrenome)

    def set_nome(self, nome):
        self.nome = nome
        
    def get_nome(self):
        return self.nome

    def set_sobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def get_sobrenome(self):
        return self.sobrenome

    def set_sexo(self, sexo):
        self.sexo = sexo

    def get_sexo(self):
        return self.sexo

    def set_idade(self, idade):
        self.idade = idade

    def get_idade(self):
        return self.idade

    def tamanho_do_nome_completo(self):
        return self.tamanho_do_nome() + self.tamanho_do_sobrenome()

nome = input('Qual o seu nome? ')
sobrenome = input('Qual o seu sobrenome? ')
sexo = input('Qual o seu sexo? ')
idade = int(input('Qual a sua idade? '))

p = Pessoa()
p.set_nome(nome)
p.set_sobrenome(sobrenome)
p.set_sexo(sexo)
p.set_idade(idade)

print('Nome:', p.get_nome())
print('Sobrenome:', p.get_sobrenome())
print('Sexo:', p.get_sexo())
print('Idade:', p.get_idade())
print('Tamanho do nome:', p.tamanho_do_nome_completo())