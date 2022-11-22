resposta = "SIM"
while resposta == "SIM":
    nivel = input("Digite o nível de acesso: ADM/USR/GUEST ").upper()
    if nivel == "ADM" or nivel == "USR":
        pronome = input("Qual o seu pronome? F ou M ").upper()
        if nivel == "ADM":
            if pronome == "F":
                print("Olá administradora!")
            else:
                print("Olá administrador!")
        else:
            if pronome == "F":
                print("Olá usuária!")
            else:
                print("Olá usuário!")
    elif nivel == "GUEST":
        print("Olá visitante!")
    else: 
        print("Olá terraqueo!")
    resposta = input("Digite SIM para continuar: ").upper()