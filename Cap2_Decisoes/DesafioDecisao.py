nivel_acesso = input("Nível de acesso: (ADM, USR ou GUEST)").upper()


if nivel_acesso == "ADM" or nivel_acesso == "USR":
    pronome = input("Qual o seu pronome? (ELE/ELA)").upper()
    if nivel_acesso == "ADM":
        if pronome == "ELE":
            print("Olá administrador!")
        else:
            print("Olá administradora!")
    else:
        if pronome == "ELA":
            print("Olá usuária!")
        else:
            print("Olá usuário!")
elif nivel_acesso == "GUEST":
    print("Olá visitante!")
else:
    print("Olá desconhecido(a)")