def carro():
    rodas = int(input("quantas rodas tem seu veículo? "))
    ano = int(input("digite seu o ano lançamento do seu carro "))
    cor =input("qual a cor  do seu carro? ")

    print("=-=-=-=-Ficha de carro=-=-=-=-")
    print("o número de rodas é :",rodas)
    if rodas >7:
        print("seu veículo é um caminhão!")
    elif rodas == 2:
        print(" seu veículo é uma moto!")
    elif rodas ==4:
        print("seu veículo é um carro!")
    print("o ano de lançamento do seu carro é ",ano)
    tempo = ano - 2025
    if tempo ==1:
        print("seu carro está novinho em folha!")
    elif tempo <5:
        print("seu carro está ficando velho!")
    elif tempo <10:
        print("seu carro é velho!")
    print("a cor de seu carro é ",cor)
carro()