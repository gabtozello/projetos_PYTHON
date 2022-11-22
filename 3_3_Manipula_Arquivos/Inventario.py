from Funcoes.Funcoes_Arquivos import  *
inventario = {}
# CHAMAR MENU
opcao = chamarMenu()
# VERIFICACAO
while opcao > 0 and opcao < 4 :
# REGISTRAR
    if opcao == 1:
        registrar(inventario)
# PERSISTIR
    elif opcao == 2:
        persistir(inventario)
# EXIBIR
    elif opcao == 3:
        resultado = exibir()
        for linha in resultado:
            lista = linha.split(";")
            print("Data........:", linha[1])
            print("Descrição...:", linha[2])
            print("Departamento:", lista[3])
# CHAMAR MENU
    opcao = chamarMenu()