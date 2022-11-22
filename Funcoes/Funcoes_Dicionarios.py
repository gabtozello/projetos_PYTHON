# CADASTRO DOS PRODUTOS

def preencherInventario(lista):
    resposta = "SIM"
    while resposta == "SIM":
        print("\nCadastrar produto ------ >")
        equipamento = [input("Equipamento: "),
        float(input("Valor: ")),
        int(input("Número Serial: ")),
        input("Departamento: ")]
    lista.append(equipamento)
    resposta = input("Digite \"SIM\" para continuar: ").upper()

# EXIBIÇÃO DOS PRODUTOS 

def exibirInventario (lista):
    for elemento in lista:
        print("Nome...............: ", elemento[0])
        print("Valor..............: ", elemento[1])
        print("Serial.............: ", elemento[2])
        print("Departamento.......: ", elemento[3])

# BUSCA DO PRODUTO

def localizarPorNome(lista):
    busca = input("\n Digite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor..............: ", elemento[1])
            print("Serial.............: ", elemento[2]) 

# DEPRECIAÇÃO DO PRODUTO

def depreciarPorNome (lista, porc):
    depreciacao = input("\nDigite o nome do equipamento que deseja depreciar: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor Antigo............: ", elemento[1])
            elemento[1] = elemento[1] * (1-porc/100)
            print("Valor Novo..............: ", elemento[1])

# DELETAR PRODUTO

def excluirPorSerial(lista):
    serial = int(input("\nDigite o serial do equimento que será deletado: "))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
    return "Itens excluídos."

# EXIBIÇÃO DE VALOR (MAIOR, MENOR)

def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0 :
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))

