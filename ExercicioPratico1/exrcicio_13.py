tempo = input("Me informe uma quantidade de tempo para que eu converta em segundos: Ex.: 3:20:10:06 ")
dia = 24
hora = 60
minuto = 60
dias = tempo.split(':')[0]
horas = tempo.split(':')[1]
minutos = tempo.split(':')[2]
segundos = tempo.split(':')[3]
tdia = (((int(dias) * dia) * 60) * 60)
thoras = ((int(horas) * hora) * 60)
tminutos = (int(minutos) * minuto)
total = tdia + thoras + tminutos + int(segundos)
print(total)
