#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
#  calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).



#entrada de dados

inMB =float(input("Informe o tamanho do arquivo MB " ))
inMbps =float(input("Informe a velocidade de sua rede Mbps " ))

#precessamento de dados


velocidade = (inMbps *1024)/8
conversao = inMB * 1024

tempo=conversao / velocidade
temConver = tempo /60


#saida de dados


print("tempo de download é:"+"{:.2f}".format(temConver)+" minutos")


