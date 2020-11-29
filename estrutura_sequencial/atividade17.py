'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de
 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 1,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

'''


import math

#entrada de dados

metrosQuadrados =float(input("Informe o Tamanho da ária a ser pintada em metros quadrados:"))

#precessamento de dados

resultadoMetros = (metrosQuadrados/6) 

latasG  = math.trunc(resultadoMetros / 18)
latasP  = math.ceil(resultadoMetros/3.6)
mistura = latasP - latasG
calculoM= (((10/100+1)*(latasG*80)+(latasP*16)))

#saida de dados

#comprar apenas latas de 18 litros;

print(f"você deve compra {latasG} latas  de tinta de 18L e ira gastar ", math.ceil(latasG)*80,"R$")

# comprar apenas galões de 3,6 litros;
print(f"você deve compra {latasP} latas  de tinta de 3,6L e ira gastar ",(latasP*16),"R$")

#misturar latas e galões

print(f"você deve compra {latasG} de 18 e {mistura} e latas de 3,6 de tintas e ira gastar ", calculoM,"R$")

