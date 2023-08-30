n,x,y,z = map(int, input("Informe o intervalo e 3 números que deverão ser ignorados: ").split())
count = 0
while count <= n:
    if (count == x) or (count == y) or (count == z):
        count += 1
        continue
    print(count)
    count += 1
