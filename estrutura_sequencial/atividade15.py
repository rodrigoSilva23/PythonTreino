'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
'''


#entrada de dados
valorHora = float(input("informe o valor por horas trabalhada:"))
horaTrabalhada = float(input("informe quantas horas trabalhadas no mês:")) #colocado Float ja que a pessoa pode trabalhar alguns minutos a mais.

#processamento de dados

salarioMesBruto    = valorHora * horaTrabalhada
descontoINSS       = (salarioMesBruto*8)/100
descontoSindicato  = (salarioMesBruto*5)/100
descontoImposto    = (salarioMesBruto*11)/100
salarioLiquido     = salarioMesBruto - descontoINSS - descontoSindicato - descontoImposto


#saida de dados

print("seu salario bruto é de :{:.2f}".format(salarioMesBruto)+"R$")
print("desconto de 8% do INSS :-"+"{:.2f}".format(descontoINSS)+"R$")
print("desconto de 5% do Sindicato :-"+"{:.2f}".format(descontoSindicato)+"R$")
print("desconto de 11% do Imposto de renda :-"+"{:.2f}".format(descontoImposto)+"R$")
print("Seu salario liquido é de:{:.2f}".format(salarioLiquido)+"R$")