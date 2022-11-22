# CRIANDO DICIONARIO DE DADOS

usuarios = {}

# PREENCHENDO DICIONARIO

usuarios = {
    "Chaves" : ["Chaves Silva" , "17/06/2017" , "Recep_01"],
    "Quico" : ["Enrico Flores" , "03/06/2017" , "Recep_02"]
}

# ADICIONAR USUARIO  (manualmente)

usuarios ["Florinda"] = ["Florinda Flores" , "26/11/2017" , "Recep_01"]

# RETORNAR OS DADOS

print(usuarios)
print("#########################========#########################")

# retornar apenas os dados do objeto que tiver a chave "Chaves"
# o método get() recebe um dado e vai pesquisá-lo entre as chaves que existem dentro do dicionário

print("Dados: ", usuarios.get("Chaves"))
