with open("/Users/igorsantana/Desktop/python-ap/Python-apostila/teste.rtf", "r") as arquivo:
  conteudo = arquivo.read()


with open("/Users/igorsantana/Desktop/python-ap/Python-apostila/teste.rtf", "w") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo.")
