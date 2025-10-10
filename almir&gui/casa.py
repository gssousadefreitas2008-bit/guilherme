
class Casa:
    def __init__(self, cor=None, quartos=None, banheiros=None, tamanho=None):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros
        self.tamanho = tamanho

    def descrever(self):
        self.cor = input("Qual a cor da casa? ")
        self.quartos = input("Quantos quartos tem a casa? ")
        self.banheiros = input("Quantos banheiros tem a casa? ")
        self.tamanho = input("Qual o tamanho da casa em m²? ")


        return f"Esta casa é {self.cor}, tem {self.quartos} quartos, {self.banheiros} banheiros e {self.tamanho}m²."

cs = Casa()
print(cs.descrever())



class Pessoa:
    def __init__(self, nome=None):
        self.nome = nome
        self.nome = input("quil o seu nome? ")

    def falar(self, mensagem=None):
        self.mensagem = input("O que você quer dizer? ")
        # return f'{self.nome} disse: {self.mensagem}'
    
    def cantar(self, musica=None):
        self.musica = input("Qual música você quer cantar? ")
        # return f'{self.nome} está cantando: {self.musica}'
    
    def estudar(self, materia=None):
        self.materia = input("o que voce está estudando? ")
        # return f'{self.nome} está estudando: {self.materia}'
    
    def eu(self):
        return f'Meu nome é {self.nome}, e eu gostaria de falar {self.mensagem}, eu gosto de cantar a musica {self.musica} e estou estudando {self.materia}.'

p = Pessoa()
p.falar()
p.cantar()
p.estudar()
print(p.eu())




#Classe Casa

#Cria objetos com informações sobre uma casa.

#__init__: define os atributos (cor, quartos, banheiros, tamanho).

#descrever(): pede os dados da casa e mostra uma descrição.

#self indica que esses dados pertencem àquela casa específica.




#Cria objetos com informações sobre uma pessoa.

#__init__: pede o nome.

#falar(), cantar() e estudar(): pedem informações e guardam em atributos do objeto.

#eu(): mostra tudo o que a pessoa fez/diz.

#self indica que os atributos (nome, mensagem, música, matéria) pertencem àquela pessoa.



 #Sobre o self:

#self significa “eu mesmo” dentro do objeto.
#Serve para dizer que a variável faz parte daquele objeto específico da classe.
 
