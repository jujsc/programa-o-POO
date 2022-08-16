class Pessoa():
    def __init__(self):
        self._nome = 'Desconhecido'
        self._sexo = '?'
    
    def set_nome(self, nome):
        if len(nome) < 3:
            print('Nome deve conter pelo menos 3 letras')
        else:
            self._nome = nome

    def set_sexo(self, sexo):
        sexo = sexo.upper()
        if sexo in 'MF':
            self._sexo = sexo
        else:
            print("Sexo deve ser 'M' ou 'F'")

    def get_nome(self):
        return self._nome
    
    def get_sexo(self):
        return self._sexo

    def get_sexo_extenso(self):
        if self._sexo == 'F':
            return 'Feminino'
        elif self._sexo == 'M':
            return 'Masculino'
        else:
            return 'Indefinido'

if __name__ == '__main__':
    p = Pessoa()

    p.set_nome('A') # Nome curto demais
    print('Nome:', p.get_nome())

    p.set_nome('Ana') # Nome correto
    print('Nome:', p.get_nome())

    p.set_sexo('X') # Sexo desconhecido
    print('Sexo:', p.get_sexo_extenso())
    
    p.set_sexo('F') # Sexo válido
    print('Sexo:', p.get_sexo_extenso())
