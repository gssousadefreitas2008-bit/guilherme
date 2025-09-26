class Animal:   
 
 def __init__(self, nome):
    self.nome=nome    
 
 def falar(self):
    print("Som do animal")

class Cachorro(Animal):
    def falar(self):
       print("Au Au!")

class Gato(Animal):
    def falar(self):
      print("Miau!") 
      return print("miau miau")
    

class pessoa :
   def andar(self):

dog = Cachorro("pretinha")
cat = Gato("xinim")

dog.falar()
cat.falar()