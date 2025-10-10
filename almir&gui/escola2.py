# Classe representando uma escola
class Escola:
    def __init__(self, nome=None, endereco=None, alunos=None):
        self.nome = nome
        self.endereco = endereco
        self.alunos = alunos if alunos else []

    def cadastrar_escola(self):
        self.nome = input("Qual é o nome da escola? ")
        self.endereco = input("Qual é o endereço da escola? ")

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def descrever(self):
        return f"A escola {self.nome} está localizada em {self.endereco} e possui {len(self.alunos)} alunos cadastrados."


# Classe representando uma pessoa (aluno)
class Pessoa:
    def __init__(self, nome=None, idade=None, serie=None):
        self.nome = nome
        self.idade = idade
        self.serie = serie
        self.materia = None
        self.mensagem = None

    def cadastrar_aluno(self):
        self.nome = input("Qual é o seu nome? ")
        self.idade = input("Qual é a sua idade? ")
        self.serie = input("Você está em qual série? ")

    def falar(self):
        self.mensagem = input("O que você gostaria de estudar? ")

    def estudar(self):
        self.materia = input("Qual matéria você está estudando agora? ")

    def apresentar(self):
        return f"Meu nome é {self.nome}, tenho {self.idade} anos, estudo na {self.serie} série, estou estudando {self.materia} e quero dizer: '{self.mensagem}'."


# Programa principal
print("=== CADASTRO DA ESCOLA ===")
escola = Escola()
escola.cadastrar_escola()

print("\n=== CADASTRO DO ALUNO ===")
aluno = Pessoa()
aluno.cadastrar_aluno()
aluno.falar()
aluno.estudar()

escola.adicionar_aluno(aluno)

print("\n=== INFORMAÇÕES ===")
print(escola.descrever())
print(aluno.apresentar())