import os
class Veiculo:
    def __init__(self,tipo,modelo,cor,ano_fabricacao):
        self._tipo=tipo
        self._modelo=modelo
        self._cor=cor
        self._ano_fabricacao=ano_fabricacao
    def get_tipo(self):
        return self._tipo
    def get_modelo(self):
        return self._modelo
    def get_cor(self):
        return self._cor
    def get_ano(self):
        return self._ano_fabricacao
    def idade(self):
        return 2022-self._ano_fabricacao
 
if __name__ == '__main__':
    veiculos=list()
    continuar=''
    contador_veiculos=1
    exercicios='N'
    # while continuar!='N':
    #     tipo=input('Informe o tipo do Veiculo: ').upper()
    #     modelo=input('Informe o modelo do Veiculo: ')
    #     cor=input('Informe a cor do Veículo: ').upper()
    #     ano=int(input('Informe o ano de fabricação do Veiculo: '))
    #     veiculos.append(Veiculo(tipo,modelo,cor,ano))
    #     continuar=input('Deseja continuar ?').upper()
       
    veiculos.append(Veiculo('M','XJ6','PRETO',2016))
    veiculos.append(Veiculo('M','HORNET','AZUL',1998))
    veiculos.append(Veiculo('M','TWISTER','VERMELHO',2017))
    veiculos.append(Veiculo('M','NINJA','PRATA',2022))
    veiculos.append(Veiculo('M','BIZ','PRETO',2003))
    veiculos.append(Veiculo('C','SENTRA','PRATA',2014))
    veiculos.append(Veiculo('C','KA','VERMELHO',2005))
    veiculos.append(Veiculo('C','GOL','BRANCO',2018))
    veiculos.append(Veiculo('C','VECTRA','PRETO',2011))
    veiculos.append(Veiculo('C','POLO','PRATA',2018))


    os.system('cls' if os.name == 'nt' else 'clear')
    while exercicios=='N':
        print('Lista de Veículos:')
        for veiculo in veiculos:
            print(f'Veiculo {contador_veiculos}')
            print(f'Tipo: {veiculo.get_tipo()}')
            print(f'Modelo: {veiculo.get_modelo()}')
            print(f'Cor: {veiculo.get_cor()}')
            print(f'Ano: {veiculo.get_ano()}')
            contador_veiculos+=1
        exercicios=input('Deseja mostrar os exercicios:')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Exercícios')

        print('\na) Mostre apenas o modelo dos veículos de cor azul\n')
        for veiculo in veiculos:
            if veiculo.get_cor()=='AZUL':
                print(veiculo.get_modelo())



        print('\nb) Calcule e mostre a idade média dos veículos\n')
        idade_total=0
        qtd=0
        for veiculo in veiculos:
            idade_total+=veiculo.idade()
            qtd+=1
        idade_media=idade_total/qtd
        print(f'{idade_media} anos')



        print('\nc) Mostre todos os dados dos veículos de um tipo específico informado pelo usuário\n')
        tipo_veiculo=input('Informe um tipo de Veículo para mostrar dados: ').upper()
        if tipo_veiculo=='M':
            print('\nMotos')
            print(f'Tipo: {veiculo.get_tipo()}\n')
            for veiculo in veiculos:
                if veiculo.get_tipo()=='M':
                    print(f'Modelo: {veiculo.get_modelo()}')
                    print(f'Cor: {veiculo.get_cor()}')
                    print(f'Ano: {veiculo.get_ano()}')
        elif tipo_veiculo=='C':
            print('\nCarros')
            print(f'Tipo: {veiculo.get_tipo()}\n')
            for veiculo in veiculos:
                if veiculo.get_tipo()=='C':
                    
                    print(f'Modelo: {veiculo.get_modelo()}')
                    print(f'Cor: {veiculo.get_cor()}')
                    print(f'Ano: {veiculo.get_ano()}')
        elif tipo_veiculo=='V':
            print('\nVans')
            print(f'Tipo: {veiculo.get_tipo()}\n')
            for veiculo in veiculos:
                if veiculo.get_tipo()=='V':
                    
                    print(f'Modelo: {veiculo.get_modelo()}')
                    print(f'Cor: {veiculo.get_cor()}')
                    print(f'Ano: {veiculo.get_ano()}')
        else:
            print('Esse tipo não existe')
        

        print('\nd) Mostre o modelo e idade dos veículos com 10 anos ou mais\n')
        for veiculo in veiculos:
            if veiculo.idade()>10:
                print('Modelo: ',veiculo.get_modelo())
                print('Idade: ',veiculo.idade())

        print('\ne)Mostre a quantidade de veículos por tipo: \n')
        qtd_motos=0
        qtd_carros=0
        qtd_vans=0
        for veiculo in veiculos:
            if veiculo.get_tipo()=='M':
                qtd_motos+=1
            if veiculo.get_tipo()=='C':
                qtd_carros+=1
            if veiculo.get_tipo()=='V':
                qtd_vans+=1
        print(f'Quantidade de motos: {qtd_motos}')
        print(f'Quantidade de carros: {qtd_carros}')
        print(f'Quantidade de vans: {qtd_vans}')

        print('\nf) Mostre todos os dados do veículo mais novo:  \n')
        menor_idade = 0 

        for veiculo in veiculos:
            if menor_idade == 0:
                menor_idade = veiculo
            if veiculo.idade() < menor_idade.idade():
                menor_idade = veiculo
        print(f'Tipo: {menor_idade.get_tipo()}')
        print(f'Modelo: {menor_idade.get_modelo()}')
        print(f'Cor: {menor_idade.get_cor()}')
        print(f'Ano: {menor_idade.get_ano()}')

        print('\ng)Mostre tipo e modelo dos veículos brancos com idade entre 3 e 5 anos')
        for veiculo in veiculos:
            if (veiculo.idade()>=3 and veiculo.idade()<=5) and veiculo.get_cor()=='BRANCO':
                print('Tipo:',veiculo.get_tipo())
                print('Modelo:',veiculo.get_modelo())

