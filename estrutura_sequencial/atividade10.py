#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

#entrada de dados

grausC= float(input("informe a temperatura em graus Celsius:"))

#processamento de dados

conversao = (grausC*1.8)+32 # caso não tenha intendido segue um link de apoio https://www.teclasap.com.br/fahrenheit-x-celsius/

#saida de dados

print("a conversão de celsius  para fahrenheit é:{:.2f}".format(conversao),"°F")