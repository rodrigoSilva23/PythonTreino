#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia
# a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos
# além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.




#entrada de dados

pescaKg = float(input("informe quantos quilos foram pegos :"))

#processamento de dados

kgMaximo = 50 #quantidade de quilos maximo regulamentado pelo estado de são paulo

excesso = pescaKg - kgMaximo  # o excesso de quilos durante a pesca

multa = excesso * 4 # a multa baseada no excesso o valor da multa é de 4,00 R$ por quilos

#saida de dados

print("você pescou:"+"{:.2f}".format(pescaKg)+"Kg, o excesso segundo o regulamento foi:"+"{:.2f}".format(excesso)+"Kg Sua multa por exesso é de "+"{:.2f}".format(multa)+"R$")

