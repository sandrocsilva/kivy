def isvogal(letra):
    vogal = ['a', 'e', 'i', 'o', 'u']
    if letra in vogal:
        return 'É uma vogal!'
    else:
        return 'É uma consoante!'


var = input("Entre com uma letra: ").lower()

print(isvogal(var))
