#EXERCÍCIO 2: CONTROLE DE PRODUÇÃO DIÁRIA
#Contexto: Verificar se a linha de produção atingiu a meta do dia
#Comando: Crie um programa que:
#Receba a quantidade produzida
#Compare com a meta de 1000 unidades
#Informe se atingiu ou quantas faltam

quantidade =float(input("Qual foi a quantidade produzida:"))
meta = 1000
faltantes = 1000 - quantidade
if quantidade > meta:
    print("Atingiu uma nova meta!")
else:
    print("Não atingiu a meta!,Ainda faltam {faltantes}")
