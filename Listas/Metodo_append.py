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
