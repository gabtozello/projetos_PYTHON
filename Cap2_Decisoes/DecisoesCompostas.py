nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: ")) 
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()
if idade >= 65 and doenca_infectocontagiosa == "SIM":
    print("O paciente " + nome + " será direcionado para sala AMARELA - COM prioridade.")
elif idade < 65 and doenca_infectocontagiosa == "SIM" :
    print("O paciente " + nome + " será direcionado para sala AMARELA - SEM prioridade.")
elif idade >= 65 and doenca_infectocontagiosa == "NÃO" :
    print("O paciente " + nome + " será direcionado para sala BRANCA - COM prioridade.")
elif idade < 65 and doenca_infectocontagiosa == "NÃO" :
    print("O paciente " + nome + " será direcionado para sala BRANCA - SEM prioridade.")
else:
    print("Responda a suspeita de doença infecto-contagiosa com SIM ou NÃO.")
