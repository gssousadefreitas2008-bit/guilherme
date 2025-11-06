class Professor:
    def falar(self):
        print("O professor diz: Bom dia, turma!")

class Aluno:
    def falar(self):
        print("O aluno responde: Bom dia, professor!")

    def estudar(self):
        print("O aluno está estudando.")

def fazer_falar(obj):
    obj.falar()

prof = Professor()
al = Aluno()


fazer_falar(prof)
fazer_falar(al)

class Diretor:
    def falar(self):
        print("O diretor anuncia: Atenção, reunião na sala dos professores!")

class Gravacao:
    def falar(self):
        print("Gravação reproduz: Bom dia, escola!")


pessoas = [Professor(), Aluno(), Diretor(), Gravacao()]

for pessoa in pessoas:
    pessoa.falar()