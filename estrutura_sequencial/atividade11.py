#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#A:o produto do dobro do primeiro com metade do segundo .
#B:a soma do triplo do primeiro com o terceiro.
#C:o terceiro elevado ao cubo.

#entrada de dados

numeroInteiro1 = int(input("Informe um valor Inteiro:"))
numeroInteiro2 = int(input("Informe  novamente um valor Inteiro:"))
numeroFloat    = float(input("Informe um valor real:"))


#processamento de dados 

resultadoA = int((numeroInteiro1*2)*(numeroInteiro2/2))
resultadoB = (numeroInteiro1*3)+numeroFloat
resultadoC = numeroFloat **3

#saida de dados 

print("o produto do dobro do primeiro com metade do segundo é:",resultadoA)
print("a soma do triplo do primeiro com o terceiro:",resultadoB)
print("o terceiro elevado ao cubo:",resultadoC)