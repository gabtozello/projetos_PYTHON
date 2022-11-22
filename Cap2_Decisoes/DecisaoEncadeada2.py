nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa?").upper()

# PRIMEIRO PROBLEMA A SER RESOLVIDO
if doenca_infectocontagiosa == "SIM":
    print("Encaminhe o paciente para SALA AMARELA.")
elif doenca_infectocontagiosa == "NÃO":
    print("Encaminhe o paciente para SALA BRANCA.")
else: 
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO.")

# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade.")
else:
    gravidez = input("O paciente está gestante?").upper()
    if gravidez == "SIM":
        print("Paciente COM prioridade.")
    else: 
        print("Paciente SEM prioridade.")
