class SerVivo:
    def __int__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
        def respirar (self):
            print(f'{self.nome} está respirando...')
             
        def dormir (self):
                print(f'{self.nome} está dormindo')
                    
class Pessoa(SerVivo):
       def falar(self, mensagem):
           print(f'{self.nome} diz: {mensagem}')

       def andar(self, destino):
           print(f'{self.nome} diz: está andando até{destino}.')

       def comer(self, comendo):
        print(f'{self.nome}diz: está comendo{comendo}')
        
p1 = Pessoa("guilerme",16)
p1.andar()

           



        
                      
                      
