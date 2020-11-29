#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#  usando a seguinte fórmula: (72.7*altura) - 58


#entrada de dados

altura = float(input("Informe sua altura:"))


#processamento de dados

resultado = (72.7*altura) - 58

#saida de dados

print("com base na altura de ","{:.2f}".format(altura),f" o seu peso ideal deve ser de {resultado}  Kg")
