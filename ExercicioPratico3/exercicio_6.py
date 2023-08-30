n = 2
mult = 0
while n <= 100:
    for i in range(2,n):
        if (n % i == 0):
            mult += 1
    if(mult==0):
        print(n,"É primo")
    n+=1
    mult = 0
