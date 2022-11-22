equipamento = []
valor = []
serial = []
departamento = []
resposta = "SIM"

# CADASTRO DO PRODUTO

while resposta == "SIM":
    equipamento.append(input("Equipamento:"))
    valor.append(float(input("Valor:")))
    serial.append(int(input("Número Serial:")))
    departamento.append(input("Departamento:"))
    resposta = input("Digite SIM para continuar: ").upper()

# EXIBIÇÃO DO PRODUTO

for indice in range(0, len(equipamento)):
    print("\nEquipamento: ",(indice+1))
    print("Nome...............: ",equipamento[indice])
    print("Valor..............: ",valor[indice])
    print("Serial.............: ",serial[indice])
    print("Departamento.......: ",departamento[indice])

# BUSCA DO PRODUTO

busca = input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamento)):
    if busca == equipamento[indice]:
       print("Valor..............: ",valor[indice])
       print("Serial.............: ",serial[indice])

# SITUAÇÃO 1: DEPRECIAÇÃO DE 10% 

busca = input("\nDigite o nome do equipamento que deseja depreciar: ")
for indice in range(0, len(equipamento)):
    if busca == equipamento[indice]:
        print("Valor Antigo............: ",valor[indice])
        valor[indice] = valor[indice] * 0.9
        print("Valor Novo..............: ",valor[indice])

# SITUAÇÃO 2: ELIMINAR PRODUTO

busca = input("\nDigite o nome do equipamento que deseja eliminar: ")
for indice in range(0, len(equipamento)):
    if busca == equipamento[indice]:
        del equipamento[indice]
        del departamento[indice]
        del valor[indice]
        del serial[indice]
        break
    
# EXIBIÇÃO DO PRODUTO

for indice in range(0, len(equipamento)):
    print("\nEquipamento: ",(indice+1))
    print("Nome...............: ",equipamento[indice])
    print("Valor..............: ",valor[indice])
    print("Serial.............: ",serial[indice])
    print("Departamento.......: ",departamento[indice])