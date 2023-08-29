try:
    val = float(input("Entre com um valor: "))
except ValueError:
    print("É uma String!")
else:
    print("É número!")