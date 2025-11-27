class Aluno:
    def __init__(self, nome, nota=0):
        self.__nome = nome
        self.__nota = nota

    @property
    def nome(self):
        return self.__nome

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self.__nota = valor
        else:
            print("Erro: a nota deve ser entre 0 e 10!")


class Disciplina:
    def __init__(self, nome):
        self.__nome = nome
        self.__alunos = []

    @property
    def nome(self):
        return self.__nome

    @property
    def alunos(self):
        return self.__alunos

    def adicionar_aluno(self, aluno):
        self.__alunos.append(aluno)


class Escola:
    def __init__(self, nome):
        self.__nome = nome
        self.__disciplinas = []

    def adicionar_disciplina(self, disciplina):
        self.__disciplinas.append(disciplina)

    def listar(self):
        print(f"\nEscola: {self.__nome}\n")
        for d in self.__disciplinas:
            print(f"Disciplina: {d.nome}")
            for a in d.alunos:
                print(f" - {a.nome} | Nota: {a.nota}")