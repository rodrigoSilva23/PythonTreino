#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius


#entrada de dados

grausF= float(input("informe a temperatura em graus Fahrenheit:"))

#processamento de dados

conversao = (grausF-32)/1.8 # caso não tenha intendido segue um link de apoio https://www.teclasap.com.br/fahrenheit-x-celsius/

#saida de dados

print("a conversão de Fahrenheit para celsius é:{:.2f}".format(conversao),"°C")