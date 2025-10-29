#EXERCÍCIO 1: MONITORAMENTO DE TEMPERATURA
#Contexto: Controlar o sistema de refrigeração de uma máquina industrial
#Comando: Desenvolva um programa que receba a temperatura atual e:
#Alerte se passar de 80°C (crítico)
#Aviso se estiver entre 60-80°C (elevado)
#Normal se abaixo de 60°C

temperatura = float(input("Qual a temperatura atual?"))
if temperatura > 80:
    print("ALERTA! Estado crítico.")
elif temperatura >=60:
    print("AVISO! Temperatura Elevada.")
else:
    print("Temperatura Normal.")
    