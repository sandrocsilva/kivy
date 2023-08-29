import datetime

data = input('Entre com uma data: ')
data_format = '%d-%m-%Y'

try:
    dataRes = datetime.datetime.strptime(data, data_format)
    print(dataRes)
except ValueError:
    print("Formato incorreto, use o seguinte DD-MM-YYYY")
