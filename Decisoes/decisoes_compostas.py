# as decisoes compostas sao direcionadas para caso a decisao seja verdadeira e caso a decisão seja falsa
# ou seja ela deve avaliar duas hipóteses 


nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
if idade >= 65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário!")
