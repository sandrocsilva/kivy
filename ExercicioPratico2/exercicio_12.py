val = input("Entre com um valor: ")

try:
    type(int(val))
except ValueError:
    print("É um número decimal")
else:
    print("É um número inteiro")
