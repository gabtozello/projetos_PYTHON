from Funcoes import *

usuarios = {}

opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
        opcao = perguntar()
    if opcao == "P":
        pesquisar(usuarios, input("Qual login deseja pesquisar?"))
        opcao = perguntar()
    if opcao == "E":
        excluir(usuarios, input("Qual login deseja excluir?").upper())
        opcao = perguntar()
    if opcao == "L":
        listar(usuarios)
        opcao = perguntar()
