class Pessoa():
    def __init__(self, nome, sexo):
        self._nome = nome
        self._sexo = sexo
        print(f'Criada pessoa "{self._nome}" com sexo "{self._sexo}"')

    def __del__(self):
        print(f'Liberada pessoa "{self._nome}" com sexo "{self._sexo}"')

if __name__ == '__main__':
    p1 = Pessoa('Roger', 'M')
    p2 = Pessoa('Alice', 'F')
