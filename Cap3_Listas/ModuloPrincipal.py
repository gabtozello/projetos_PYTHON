from Funcoes.Funcoes_Dicionarios import *

minhaLista = []

# CADASTRO DOS PRODUTOS

print("Preenchendo: ")
preencherInventario(minhaLista)

# EXIBIÇÃO DOS PRODUTOS

print("Exibindo: ")
exibirInventario(minhaLista)

# BUSCA DO PRODUTO

print("Pesquisando: ")
localizarPorNome(minhaLista)

# DEPRECIAÇÃO DO PRODUTO

print("Alterando: ")
depreciarPorNome(minhaLista, 20)

# DELETAR PRODUTO

print("Excluindo: ")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

# EXIBIÇÃO DE VALOR (MAIOR, MENOR)

print("Resumindo: ")
resumirValores(minhaLista)