try:
    valor = int(input("Entre com um número entre 1 e 12 referente ao mês: "))

    if (valor == 1):
        print('Janeiro')
    elif (valor == 2):
        print('Fevereiro')
    elif (valor == 3):
        print('Março')
    elif (valor == 4):
        print('Abril')
    elif (valor == 5):
        print('Maio')
    elif (valor == 6):
        print('Junho')
    elif (valor == 7):
        print('Julho')
    elif (valor == 8):
        print('Agosto')
    elif (valor == 9):
        print('Setembro')
    elif (valor == 10):
        print('Outubro')
    elif (valor == 11):
        print('Novembro')
    elif (valor == 12):
        print('Dezembro')
    else:
        print('Informe um valor entre 1 e 12!')
except ValueError:
    print('Informe um valor entre 1 e 12!')