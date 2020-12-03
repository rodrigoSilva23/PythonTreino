#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

#entrada de dados 

verificar = input("informe uma letra:").upper()

#condicional de verificação e exibição

if len(verificar) != 1:
    print("Informe um valor, ou digite apenas 1 caracter!")

elif verificar == "A" or verificar == "E" or verificar == "I" or verificar == "O" or verificar == "U":
    print("a letra digitada é uma VOGAL")

else:
    print("a letra digitada é uma CONSOANTE")

