usuarios = {} #criamos um dicionario

usuarios = {
    "Chaves":["Chaves silva", "17/06/2017","Recep_01"],
    "Quico": ["Quico Andrade", "20/09/2019", "Recep_02"]
}
# criamos a chave, e dps dela utilizamos dois pontos";" para armazenar os outros dados que ficam dentro de uma lista

# ---------Como retornar os dados obtidos na lista ---------------- ?

print(usuarios) #Exibe tudo o que tem dentro do dicionário 
print("##############========#########")
print("Dados: ", usuarios.get("Chaves")) #Exibe só a lista da chave Chaves

#  Em dicionarios é muito mais fácil e pratico localizar uma lista ou um dado porque não necessitamos de um foreach para 
# percorrer o dicionario 

