with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
print("Tipo de dado da variável:",type(conteudo))
print("Contéudo do arquivo: ", conteudo)