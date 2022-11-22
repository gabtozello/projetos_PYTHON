from Funcoes.Funcoes_Boston import *
# CHAMAR MENU
opcao = chamarMenu()
# VERIFICACAO
while opcao > -1 and opcao < 4 :
# QUESTAO RESOLVIDA
    if opcao == 0:
        with open("economic-indicators.csv", "r") as boston:
            total = 0
            for linha in boston.readlines()[1:-1]:
                total = total + float(linha.split(",")[3])
            print("O total de voos é: ", total)
            opcao = chamarMenu()

# QUESTAO 1 = Qual o total de voos internacionais que partiram do aeroporto de Logan no ano de 2014?
    elif opcao == 1:
        with open("economic-indicators.csv", "r") as boston:
            total = 0
            for linha in boston.readlines()[1:-1]:
                separacao = linha.split(",")[0]
                print(separacao)
                total = total + 1
                voos_Ano = 0
                soma_Voos = []
                if separacao == "2014":
                    voos_Ano = float(linha.split(",")[3])
                soma_Voos.append(voos_Ano)
                print("voos: ", voos_Ano)
                print("soma voos: ", soma_Voos)
            print(total)
            opcao = chamarMenu()