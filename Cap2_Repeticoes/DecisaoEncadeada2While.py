resposta = "SIM"
while resposta == "SIM":
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()
# PRIMEIRO PROBLEMA
    while doenca_infectocontagiosa != "SIM" and doenca_infectocontagiosa != "NAO":
        print("Digite SIM ou NAO: ")
        doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()
        if doenca_infectocontagiosa == "SIM":
            print("Encaminhe o paciente para SALA AMARELA.")
        else:
            print("Encaminha o paciente para SALA BRANCA.")
# SEGUNDO PROBLEMA
    if idade >= 65 :
        print("Paciente COM prioridade.")
    else:
        gravidez = input("O paciente está gestante?").upper()
        if gravidez == "SIM":
            print("Paciente COM prioridade.")
        else:
            print("Paciente SEM prioridade.")
    resposta = input("Recomeçar? SIM/NAO").upper()