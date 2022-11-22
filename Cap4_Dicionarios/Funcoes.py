#PREENCHER A VARIAVEL OPÇÃO

def perguntar():
    resposta = input(" O que deseja realizar? " +
                     "\n<I> - Para Inserir um usuário." +
                     "\n<P> - Para Pesquisar um usuário." +
                     "\n<E> - Para Excluir um usuário." +
                     "\n<L> - Para Listar um usuário:").upper()
    return resposta

#PREENCHER O DICIONARIO DE DADOS

def inserir(dicionario):
    dicionario[input("Digite ").upper()] = [input("Digite o login: ").upper(),
                                                     input("Digite o nome: ").upper(),
                                                     input("Digite a última data de acesso: "),
                                                     input("Qual a última estação acessada: ").upper()]

#PESQUISAR NO DICIONARIO DE DADOS

def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print("Nome..........:" + lista[0])
        print("Último acesso.:" + lista[1])
        print("Última estação:" + lista[2])

#EXCLUIR NO DICIONARIO DE DADOS

def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Login Excluído.")

#LISTAR OBJETOS

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto.........")
        print("Login..........:", chave)
        print("Dados..........:", valor)