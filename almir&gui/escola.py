def elogin():
    def log():
        log=int(input("Escolha o seu tipo de login:\n1)Login de aluno \n2)Login executivo \n"))
        if log ==1:
            nome=input("digite seu nome:")
            cpf=input("digite seu cpf:")
            idade=input("digite sua idade:")
            repetir=1
            while repetir==1:
                turma=int(input("escolha sua turma\n1)DS\n2)ADM\n3)FIN\n4)ENF\n"))
                if turma==1:
                    classe="DS"
                    repetir = repetir-1
                elif turma ==2:
                    classe="ADM"
                    repetir = repetir-1
                elif turma==3:
                    classe="FIN"
                    repetir = repetir-1
                elif turma==4:
                    classe="ENF"
                    repetir = repetir-1
                else:
                    print("Por favor, escolha uma opção válida.") 
            print("-=-=-=-=-=-FICHA DO ALUNO-=-=-=-=-=-")
            print("nome:",nome)
            print("cpf:",cpf)
            print("idade:",idade)
            print("turma:",classe,"\n")
            metarepetir=1
            while metarepetir==1:
                menualuno=int(input("em qual sistema deseja de entrar? \n1)avaliador de médias\n2)leitor de horários\n3)retornar\n"))
                if menualuno==1:
                    repetir=1
                    while repetir==1:
                        int(input("Escolha a sua matéria\n1)Matemática\n2)Física\n3)Biologia\n4)Química\n5)Português\n6)Inglês"))
                        if turma==1:
                            classe="Matemática"
                            repetir = repetir-1
                        elif turma ==2:
                            classe="Física"
                            repetir = repetir-1
                        elif turma==3:
                            classe="Biologia"
                            repetir = repetir-1
                        elif turma==4:
                            classe="Química"
                            repetir = repetir-1
                        elif turma==5:
                            classe="Português"
                            repetir = repetir-1
                        elif turma ==6:
                            classe="Inglês"
                            repetir = repetir-1
                        else:
                            print("Por favor, escolha uma opção válida.")
                        print("digite a suas notas")
                        n1=float(input("Nota 1: "))
                        n2=float(input("Nota 2: "))
                        n3=float(input("Nota 3: "))
                        n4=float(input("Nota 4: "))
                        nt=float(input("Nota de trabalho: "))
                        media=((n1+n2+n3+n4+nt)/5)
                        print("sua média é ",media)
                        if media < 6:
                            print("está reporvado(a)!")
                        else:
                            print("está aprovado(a)!")
                elif menualuno == 2:
                    if turma == 1 :
                        print(" Aula 1 português\n Aula 2 matematica\n Aula 3 ingles\n Aula 4 POO\n Aula 5 historia\n Aula 6 geografia\n" )
                    elif turma == 2 :
                        print(" Aula 1 ADM\n Aula 2 economia\n Aula 3 matematica\n Aula 4 ingles\n Aula 5 historia\n Aula 6 geografia\n" )
                    elif turma == 3 :
                        print(" Aula 1 matematica\n Aula 2 economia\n Aula 3 ingles\n Aula 4 finanças\n Aula 5 historia\n Aula 6 geografia\n" )
                    elif turma == 4 :
                        print(" Aula 1 biologia\n Aula 2 quimica\n Aula 3 fisica\n Aula 4 portugues\n Aula 5 historia\n Aula 6 geografia\n" )
        else:
            repetir=1
            while repetir==1:
                senha="admasdfg"
                nome=input("digite seu nome:")
                cpf=input("digite seu cpf:")
                idade=input("digite sua idade:")
                login=input("digite a senha:")
                if login == senha:
                    repetir = 1
                    while repetir==1:
                        turma=int(input("escolha sua função\n1)Cozinheiro(a)\n2)Professor(a)\n3)Coordenador(a)\n4)Responsável(a)\n"))
                        if turma==1:
                            classe="Cozinheiro(a)"
                            repetir = repetir-1
                        elif turma ==2:
                            classe="Professor(a)"
                            repetir = repetir-1
                        elif turma==3:
                            classe="Coordenador(a)"
                            repetir = repetir-1
                        elif turma==4:
                            classe="Responsável(a)"
                            repetir = repetir-1
                        else:
                            print("Por favor, escolha uma opção válida.") 
                    print("-=-=-=-=-=-FICHA DO EXECUTIVO-=-=-=-=-=-")
                    print("nome:",nome)
                    print("cpf:",cpf)
                    print("idade:",idade)
                    print("função:",classe,"\n")
                    repetir = repetir-1
                else:
                    print("senha incorreta")
    log()
elogin()

