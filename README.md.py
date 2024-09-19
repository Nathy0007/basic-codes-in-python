#Media do aluno  com loop.
contador = 0
while contador <= 10:
   nome = input('Digite o nome do aluno:')
   n1 = int(input('Nota do aluno:'))
   n2 = int(input('segunda nota '))
   media = (n1 + n2) / 2
   if media >= 7:
    print('parabens sua media foi: {}'.format(media))
   else:
    print('Reprovado')
   continua = input('Deseja continuar? [SIM/NÃO]').lower()
   if continua == 'sim':
      continue
   else:
     print('Programa Finalizado')
     break
contador += 1

#cauculos sobre lucros.
faturamento=2000.85
custo=900
reposição=150
tecerizaçao=200
mensagem= "As vendas formam um sucesso!"

print("faturamento", faturamento)
print("custo", custo)
print("reposição", reposição)
print("lucro", faturamento - custo + reposição - tecerizaçao)
print( mensagem)

#Dia,mês e ano.

mng=
dia=input('Qual foi o dia em que você nasceu?')
mes=input('Qual o mês em que você nasecu?')
ano=input('qual foi o ano em que você nasceu?')
print('voce naseu no dia',dia)
print('do mês',mes)
print('do ano de',ano)

#Somas dos valores(calculadora)

n1=int(input('Digite um numero:'))
n2=int(input('Digite outro numero:'))
s=n1 + n2
print('a soma entre {} e {} equivale a {}'.format(n1,n2,s))
print('soma dos valoror={}'.format(n1+n2))






