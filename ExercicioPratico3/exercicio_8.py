n,x,y,z = map(int, input("Informe o intervalo e 3 números que deverão ser ignorados: ").split())
for i in range(n):
    if (i == x) or (i == y) or (i == z):
        continue
    print(i,"Esse pode!")