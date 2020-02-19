larguraParede = float(input("Informe a largura da parede:  "))
larguraAzu = float(input("Informe a largura do azulejo:  "))

larguraAzuCent = larguraAzu / 100 # para transformar o valor informado em centimetro

AreaParede = larguraParede ** 2
AreaAzu = larguraAzuCent ** 2

print 'quantidade de azulejos necessarios para preencher a parede = ', (AreaParede / AreaAzu)