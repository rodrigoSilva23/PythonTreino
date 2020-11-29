#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

#importando biblioteca 

import math

#entrada de dados

metrosQuadrados =float(input("Informe o Tamanho da ária a ser pintada em metros quadrados:"))

#precessamento de dados

resultadoMetros = (metrosQuadrados/3) 

latas = (resultadoMetros / 18)

#saida dados

print(f"você deve compra {math.ceil(latas)} latas  de tinta e ira gastar ", math.ceil(latas)*80,"R$")


