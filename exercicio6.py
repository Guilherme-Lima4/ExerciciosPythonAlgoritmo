larguraParede = float(input("Informe a largura da parede:  "))
alturaParede = float(input("Informe a altura da parede:  "))

larguraAzu = float(input("Informe a largura do azulejo:  "))
alturaAzu = float(input("Informe a altura do azulejo:  "))

   # para transformar os valores informados em centimetro
larguraAzuCent = larguraAzu / 100 
alturaAzuCent =  alturaAzu / 100

areaParede = larguraParede * alturaParede
areaAzu = larguraAzuCent * alturaAzuCent

print 'Azulejos necessarios para preencher a parede = ', (areaParede / areaAzu)
