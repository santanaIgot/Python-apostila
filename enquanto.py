resp = "S"
qtd = 0
while resp == "S":
    soma = soma + float(input("Digite a nota" + str(qtd + 1)))
    qtd += 1
    
    resp = input("Desejo continuar (S OU N)?").upper()
    while resp != "S " or "N" :
        print("opção inválida")
        resp = input("Desejo continuar (S OU N)?").upper()

    # resp = input("Desejo continuar (S OU N)?").upper()
    # if resp != "S " or "N" :
    #     print("opção inválida")
    #     resp = input("Desejo continuar (S OU N)?").upper()


    media = soma / qtd
    print(media)


    # memso que a condição do laço if esteja errado ele vai executar uma vez só 
    # O while é estrutura de repetição, mesmo se estiver errado ele vai perguntar de novo para digitar nova opção
    