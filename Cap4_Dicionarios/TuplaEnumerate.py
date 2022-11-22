usuarios = {}
resp = "S"
emails = []
    #PREENCHENDO EMAILS
while resp == "S":
    emails.append(input("Digite um e-mail: ")).lower()
    resp = input("Digite <S> para continuar: ").upper()
    #ENUMERANDO CADA ITEM ENCONTRADO NA LISTA "E-MAILS" E GERANDO TUPLA COM CADA ELEMENTO (FUNÇÃO: LIST())
tupla = list(enumerate(emails))
    #LAÇO FOR ATRELADO AO TAMANHO DA TUPLA(OU SEJA, QUANTIDADE DE E-MAILS QUE FORAM ARMAZENADOS)
for chave in range(0, len(tupla)):
    #EXIBINDO O E-MAIL QUE IRÁ RECEBER O NOME E O NÍVEL: tupla[chave][1] => da tupla e recuperar o elemento
    #de acordo com o valor da variável-chave, ou seja, da primeira vez, ela estará valendo zero, por isso
    #pegará o primeiro elemento da tupla
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]] = [input("Digite o nome: "), input("Digite o nível: ")]
    #EXIBINDO DADOS
for chave, dado in usuarios.items():
    print("Usuario.: ", chave[0])
    print("E-mail..: ", chave[1])
    print("Nome....: ", dado[0])
    print("Nível...: ", dado[1])
    formaggio