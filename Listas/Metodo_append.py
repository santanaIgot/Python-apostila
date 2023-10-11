# inventario=[]
# resposta="S"
# while resposta=="S":
#   inventario.append(input("Equipamento: "))
#   inventario.append(float(input("Valor: ")))
#   inventario.append(int(input("Número Serial: ")))
#   inventario.append(input("Departamento: "))
#   resposta=input("Digite "+resposta+" para continuar: ").upper()
  # ele irá percorrer todas as posições e exibira todos os valores
#   for elemento in inventario:
#     print(elemento)

# append() adiciona itens a lista 


equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
  equipamentos.append(input("Equipamento: "))
  valores.append(float(input("Valor: ")))
  seriais.append(int(input("Número Serial: ")))
  departamentos.append(input("Departamento: "))
  resposta = input("Digite "+resposta+" para continuar: ").upper()

for indice in range(0, len(equipamentos)):
  print("\
        Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])


busca = input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos)):
  if busca == equipamentos[indice]:
    print("Valor..: ", valores[indice])
    print("Serial.:", seriais[indice])

# observamos que dentro do for, montamos uma tomada de decisão simples
# cuja função será comparar o conteudo da variavel de busca,
# com todos os elementos que estiverem armazenados dentro da lista "equipamentos"
# quando ele encontrar um valor igual irá exibir o valor e o serial do equipamento


depreciacao = input(" Digite o nome do equipamento que será depreciado: ")
for indice in range(0, len(equipamentos)):
  if depreciacao == equipamentos[indice]:
    print("Valor antigo: ", valores[indice])
    valores[indice] = valores[indice] * 0.9
    print("Novo valor: ", valores[indice])

# como podemos observar na lista acima, quando igualamos uma lista acompanhada de um índice , sobreescrevemos o conteúdo
# do dado na posição específicada do indice ,
# ou seja departamentos[0]="teste" => essa linha seria resposável por substituir pela string "teste" o dado que esta na posição 0


serial = int(input(" Digite o serial do equipamento que será excluido: "))
for indice in range(0, len(departamentos)):
  if seriais[indice] == serial:
    del departamentos[indice]
    del equipamentos[indice]
    del seriais[indice]
    del valores[indice]
    break

for indice in range(0, len(equipamentos)):
  print("Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])

# Repare que neste código acima utilizamos o break dentro do if 
#  o que significa que quando ele encontrar o valor desejado irá excluir o elemento 
# da posição onde foi encontrado e depois irá sair do laço for 
