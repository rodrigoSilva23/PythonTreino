#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

#entrada de dados
valorHora = float(input("informe o valor por horas trabalhada:"))
horaTrabalhada = float(input("informe quantas horas trabalhadas no mês:")) #colocado Float ja que a pessoa pode trabalhar alguns minutos a mais.

#processamento de dados

salarioMes =valorHora * horaTrabalhada

#saida de dados

print(f"você ganha {valorHora} R$ por hora e este mês você trabalhou {horaTrabalhada} Horas, por tanto o seu  valor  salarial é de :"" {:.2f}".format(salarioMes)," R$")