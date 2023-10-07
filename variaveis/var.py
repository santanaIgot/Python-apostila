# nome="Humberto Delgado"
# empresa='FIAP'
# qtde_funcionarios=500
# mediaMensalidade=856.50


# nome = "Humberto Delgado"
# empresa = 'FIAP'
# qtde_funcionarios = 500
# mediaMensalidade = 856.50
# print(nome + " trabalha na empresa " + empresa)
# print("Possui: ", qtde_funcionarios, " funcionarios.")
# print("A média da mensalidade é de: " + str(mediaMensalidade))

# variavel é so um espaço alocado em memoria 

nome = input("Digite um funcionário: ")
empresa = input("Digite a instituição: ") 
qtde_funcionarios = int(input("Digite a qtde de funcionários: ")) 
mediaMensalidade = float(input("Digite a média da mensalidade: ")) 
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))

print(type(mediaMensalidade))
