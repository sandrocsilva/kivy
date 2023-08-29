ip = input("Me informe o endereço ip para informar a sua classe: ")

classe = int(ip.split(".")[0])

if (classe >= 0) and (classe <= 127):
    print('Este ip ' + ip + ' é classe A')
elif (classe >= 128) and (classe <= 191):
    print('Este ip ' + ip + ' é classe B')
elif (classe >= 192) and (classe <= 223):
    print('Este ip ' + ip + ' é classe C')
elif (classe >= 224) and (classe <= 239):
    print('Este ip ' + ip + ' é classe D')
elif(classe >= 240):
    print('Este ip ' + ip + ' é classe E')

