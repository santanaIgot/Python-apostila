primo = "S"


for numero in range (1, numero +1):
    resto = numero % divisor 
    if(resto == 0 and (divisor != 1 and divisor != numero)):
        primo = "N"
        if primo == "S":
            print("O num "+ str (numero) + "è primo")

            # eçif primo == "N"
            # print("O Numero"+str(numero )+"nao é primo")