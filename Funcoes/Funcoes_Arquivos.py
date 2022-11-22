# CHAMAR MENU

def chamarMenu():
    escolha = int ( input("Digite: "
                    "\n <1> PARA REGISTRAR ATIVO"
                    "\n <2> PARA PERSISTIR EM ARQUIVO"
                    "\n <3> PARA EXIBIR ATIVOS ARMAZENADOS"))
    return escolha

# REGISTRAR

def registrar(dicionario):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial: ")] = [
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]
        resp = input("Digite <S> para continuar: ").upper()

# PERSISTIR

def persistir(dicionario):
    with open("inventario.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + ".")
            print("Persistido com sucesso!")

# EXIBIR

def exibir():
    with open("inventario.csv", "r") as inv:
        linhas = inv.readlines()
    return linhas