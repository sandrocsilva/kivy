idade = int(input("Digite um número: "))
if (idade < 1):
    print("Idade " + str(idade) + ", demonstra que você é um recém-nascido")
elif (idade >= 18):
    print("Idade " + str(idade) + ", já demonstra que você é de maior")
elif (idade < 18):
    print("Idade " + str(idade) + ", ainda demonstra que você é de menor")