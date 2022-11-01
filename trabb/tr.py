class Locacadora():







#class Veiculo():

#class Locacao():

def menu():
    print("1 - Consultar veículos")
    print("2 - Realizar locação")
    print("3 - Realizar devolução")
    print("4 - Consultar locações")
    print("5 - Resumo")
    print("6 - Salvar")
    print("7 - Sair")
    choice = int(input("Insira sua escolha: (1-7) \n"))
    return choice

if __name__ == '__main__':
    cont = True
    while cont:
        print("bem vindo ao sistema de locações da locadora segura")
        alugar = input("Você deseja alugar um carro: \n")
        if alugar in "Nn":
            cont = False
        cidade = input("Informe sua cidade de origem: \n")
        #implementar lista de veiculos disponiveis
        #Cliente escolhe qual veiculo quer 
        days = int(input("Informe a quantidade de dias que você deseja ficar o veículo: \n"))
        #mostra valor total estimado das diárias e faz confimação da reserva
        reservar = input("Deseja confirmar a reserva: \n")
        # if sim sistema registra a reserva
        #implementar sistema reverso
          