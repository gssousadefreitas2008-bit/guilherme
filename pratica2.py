def cadrastro():
    nome=input("digite seu nome: ")
    cpf=input("digite seu cpf: ")
    endereço=input("digite seu endereço: ")
    idade=int(input("digite sua idade: "))


    print("=-=-=--=Ficha de cadastro=-=-=--=")
    print("seu nome é:",nome)
    print("seu cpf é:",cpf)
    print("seu endereço é:",endereço)

    if idade < 18:
        print("voce é menor de idade, nao pode se cadastrar.")
    else:
       print("voce é maior de idade, cadastro realizado com sucesso!")        

cadrastro()