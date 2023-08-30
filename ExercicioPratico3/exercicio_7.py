n = int(input("Informe o intervalo: "))
mult = 0
count = 0
total = 0
while count <= n:
    for i in range(2, count):
        if (count % i == 0):
            mult += 1
    if (mult == 0):
        total+=count
        print(count, "É primo")
    count += 1
    mult = 0
print(total)