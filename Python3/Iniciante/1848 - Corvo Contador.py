cont = soma = 0
num = ''
while True:
    entrada = str(input())
    if entrada == "caw caw " or entrada == "caw caw":
        cont += 1
        print(soma)
        soma = 0
    else:
        for i in entrada:
            if i == "-":
                num += "0"
            elif i == "*":
                num += "1"
            else:
                num += ''
        soma += int(num, 2)
        num = ''
    if cont == 3:
        break
