
# 2 implemntar somente getters. consulta lisat n mais arquivo e apresenta o relatorio final
'''Uma casa de apostas quer automatizar a avaliação dos resultados dos jogos
do campeonato brasileiro, importando e processando um arquivo csv (anexo) com os jogos
da rodada. Cada jogo possui as seguintes informações: nome do time da casa, quantidade
de gols do time da casa, nome do time visitante, e quantidade de gols do time visitante.
Implemente a classe “Jogo”, que recebe no seu construtor uma linha do arquivo csv, separe
os dados e os armazene nos atributos do objeto. Implemente também os métodos getter.
Todos os objetos “Jogo” devem ser instanciados dinamicamente e armazenados em uma
lista. Ao finalizar a importação dos dados, o programa deverá processar a lista de objetos e
mostrar automaticamente na tela o relatório da rodada, contendo as informações abaixo, e
encerrar sua execução:
a) Quantidade de jogos realizados;
b) Quantidade total de gols da rodada;
c) Média de gols por partida;
d) Quantidade de empates;
e) Jogo com maior quantidade total de gols (nomes dos times e total de gols);
f) Time que fez mais gols (nome do time e quantos gols);'''

class Jogo:
    def __init__(self, linha):
        self.deserializar(linha)

    def deserializar(self, linha):
        dados = linha.split(',')
        self._time_casa = dados[0]
        self._gols_casa = int(dados[1])
        self._time_visitante = dados[2]
        self._gols_visitante = int(dados[3])
    
    def get_time_casa(self):
        return self._time_casa
    
    def get_gols_casa(self):
        return self._gols_casa
    
    def get_time_visitante(self):
        return self._time_visitante
    
    def get_gols_visitante(self):
        return self._gols_visitante
    

def relatorio(jogos):
    tot_jogos = gols_visit = gols_casa = empates = jogo_mais_gols = time_mais_gols =0 
    times = []

    for jogo in jogos:
        tot_jogos+=1
        gols_visit += jogo.get_gols_visitante()
        gols_casa +=jogo.get_gols_casa()
        gols_total = gols_visit + gols_casa

        if jogo.get_gols_visitante() == jogo.get_gols_casa():
            empates +=1
        
        gols_por_jogo = jogo.get_gols_visitante() + jogo.get_gols_casa()
        if gols_por_jogo > jogo_mais_gols:
            jogo_mais_gols = gols_por_jogo
            nome_casa = jogo.get_time_casa()
            nome_vist = jogo.get_time_visitante()

        if jogo.get_time_visitante() and jogo.get_time_casa() not in times:
            times.append(jogo.get_time_visitante())
            times.append(jogo.get_time_casa())
        
        gols1 = jogo.get_gols_visitante() 
        gols2 = jogo.get_gols_casa() 
        
        if gols1 > time_mais_gols:
            time_mais_gols = gols1
            nome_time = jogo.get_time_visitante()
        if gols2 > time_mais_gols:
            time_mais_gols = gols2
            nome_time = jogo.get_time_casa()

    media_gols = gols_total/tot_jogos
    print("RELATÓRIO DE JOGOS")
    print("A quantidade de jogos na realizados foi", tot_jogos)
    print("A quantidade total de gols foi", gols_total)
    print("A média de gols por partida foi de", media_gols, "gols")
    print("A quantidade de empates foi", empates)
    print("O jogo com mais gols foi entre", nome_casa,"e", nome_vist,"com um total de", jogo_mais_gols,"gols")
    print("O time que fez mais gols foi",nome_time,"com",time_mais_gols,"gols")

if __name__ == '__main__':
    jogos = []
    arq = open("jogos.csv")
    arq.readline()            # Descarta o cabeçalho do arquivo
    for linha in arq:         # Instancia os objetos
        jogos.append(Jogo(linha.strip()))
    arq.close()
    relatorio(jogos)
