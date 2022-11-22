inventario = []
resposta = "SIM"

# CADASTRO DOS PRODUTOS

while resposta == "SIM":
    print("\nCadastrar produto ------ >")
    equipamento = [input("Equipamento: "),
    float(input("Valor: ")),
    int(input("Número Serial: ")),
    input("Departamento: ")]
    inventario.append(equipamento)
    resposta = input("Digite \"SIM\" para continuar: ").upper()

# EXIBIÇÃO DOS PRODUTOS 

for elemento in inventario:
    print("Nome...............: ", elemento[0])
    print("Valor..............: ", elemento[1])
    print("Serial.............: ", elemento[2])
    print("Departamento.......: ", elemento[3])

# BUSCA DO PRODUTO

busca = input("\n Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca == elemento[0]:
        print("Valor..............: ", elemento[1])
        print("Serial.............: ", elemento[2])

# DEPRECIAÇÃO DO PRODUTO

depreciacao = input("\nDigite o nome do equipamento que deseja depreciar: ")
for elemento in inventario:
    if depreciacao == elemento[0]:
        print("Valor Antigo............: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Valor Novo..............: ", elemento[1])

# DELETAR PRODUTO

serial = int(input("\nDigite o serial do equimento que será deletado: "))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

# EXIBIÇÃO DOS PRODUTOS 

for elemento in inventario:
    print("Nome...............: ", elemento[0])
    print("Valor..............: ", elemento[1])
    print("Serial.............: ", elemento[2])
    print("Departamento.......: ", elemento[3])

# EXIBIÇÃO DE VALOR (MAIOR, MENOR)

valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0 :
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))
    