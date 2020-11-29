#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


#entrada de dados 

sexo = input("Informe seu Sexo F-Feminino ou M-Masculino ou N-não definido:").upper()

#condicional de verificação e exibição

if sexo == "F":
    print("Sexo Feminino ")

elif sexo =="M":
    print("Sexo Masculino")

elif sexo =="N":
    print("Sexo Não definido")

else:
    print("Por favor informe um Sexo valido!")
