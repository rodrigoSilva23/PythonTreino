#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

#entrada de dados

altura = float(input("Informe sua altura:"))


#processamento de dados

resultadoH = (72.7*altura) - 58

resultadoM = (62.1*altura) - 44.7

#saida de dados1.82


print("com base na altura de "+ "{:.2f}".format(altura)+" o seu peso ideal deve ser de "+"{:.2f}".format(resultadoH)+" Kg para um Homem e "+"{:.2f}".format(resultadoM)+" Kg para uma Mulher")
