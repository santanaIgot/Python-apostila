inventario = {}


def chamarMenu():
    escolha = int(input("Digite: "
                        ""
                        "< 1 > para registrar ativo"
                        ""
                        "< 2 > para persistir em arquivo"
                        ""
                       " < 3 > para exibir ativos armazenados: "))
    return escolha


def registrar(dicionario):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial: ")] = [
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]
        resp = input("Digite <S> para continuar.").upper()


def persistir(dicionario):
    with open("inventario.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" +
                      valor[1] + ";" + valor[2] + "")
    return "Persistido com sucesso"


def exibir():
    with open("inventario.csv", "r") as inv:
        linhas = inv.readlines()
    return linhas


# Criamos um dicionario de dados , chamado inventario , e montamos um menu de escolha , com as opções 1,2 e 3.
# Enquanto o usuario digitar qualquer uma das três opções , o programa continuára sendo executado,
# entretanto, para qualquer outro valor o programa sera encerrado


# SE o valor digitado for 1 , iremos colocar o usuario em outro laço while , e enquanto ele digitar "S" ,
# Será permitido ele adicionar itens a nosso dicionario inventario

# Se o valor digitado for 2 , abriremos o arquivo "inventario.csv" em modo de concatenação e, então , para cada objeto encontrado no
# nosso dicionario , iremos adicionar uma linha no arquivo .Na linha, escreveremos a chave e os valores desta chave separados por ";"
# (para o Excel isso indicara que cada valor ficraa em uma coluna).Ao término da linha , adicionamos a quebra de linha " \n", isso também
# indicara ao excel uma quebra de linha 