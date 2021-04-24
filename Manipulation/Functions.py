def perguntar():
    return input("O que deseja realizar ?\n" +
                 "<I> - Para INSERIR um usuario\n").upper()


def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [
        input("Digite o nome: "),
        input("Digite a ultima data de acesso: "),
        input("Qual a ultima estacao acessada: ")
    ]

def salvar(dicionario):
    with open("bd.txt","a") as arquivo:
        for key, value in dicionario.items():
            arquivo.write(key + ":" + str(value))