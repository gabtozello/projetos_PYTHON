nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()
if idade >= 65 :
    print("Paciente COM prioridade.")
    if doenca_infectocontagiosa == "SIM":
        print("Encaminhe o paciente para SALA AMARELA.")
    elif doenca_infectocontagiosa == "NÃO":
        print("Encaminhe o paciente para SALA BRANCA.")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NÃO.")
else:
    print("Paciente SEM prioridade.")
    if doenca_infectocontagiosa == "SIM":
        print("Encaminhe o paciente para SALA AMARELA.")
    elif doenca_infectocontagiosa == "NÃO":
        print("Encaminha o paciente para SALA BRANCA.")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NÃO.")   