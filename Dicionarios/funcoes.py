usuarios ={}

def perguntar():
    resposta = input("O que deseja realizar?"
                     " +< I > - Para Inserir um usuário"
                     " +< P > - Para Pesquisar um usuário"
                     " +< E > - Para Excluir um usuário"
                     " +"
                     "<L> - Para Listar um usuário: ").upper()
    return resposta


def inserir(dicionario):
  chave = input("Digite o login: ").upper()
  usuarios[chave] = [input("Digite o nome: ").upper(),
    input("Digite a última data de acesso: "),
    input("Qual a última estação acessada: ").upper()]
    # Criamos uma variável chave para armazenar os dados de maneira efeciente, deixando nosso codigo mais legível
    # e rápido

    

def pesquisar(dicionario,chave): # precisamos receber o dicionario(Onde se pretende pesquisar) e a chave(o dado quee vai ser pesquisado)
    pesquisar_user = dicionario.get(chave)
    if pesquisar_user != None: # verificamos se a lista esta vazia, se ela estiver vazia não retornará nada
        # caso contrario, irá exibir os dados dentro do dicionário
        print("Nome...........:"+ pesquisar_user[0])
        print("Ultimo acesso..:" + pesquisar_user[1])
        print("Ultima estação.:" + pesquisar_user[0])


def excluir(dicionario,chave):
    if dicionario.get(chave) != None:
        del dicionario.get(chave) # comanado DEL elimina o objeto
        print("Objeto eliminado")


def listar(dicionario):
    for chave,valor in dicionario:
        print("Objeto:..........")
        print("Login:..."+chave)
        print("Dados:..."+valor)





