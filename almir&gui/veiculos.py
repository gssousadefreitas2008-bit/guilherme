
class Transporte:
    def __init__(self, modelo, capacidade, velocidade_media):
        self.modelo = modelo
        self.capacidade = capacidade
        self.velocidade_media = velocidade_media

    def mover(self):
        # Método genérico (será sobrescrito nas subclasses)
        print(f"O transporte {self.modelo} está se movendo...")

    def __str__(self):
        return f"{self.modelo} (capacidade: {self.capacidade}, velocidade média: {self.velocidade_media} km/h)"



class Carro(Transporte):
    def __init__(self, modelo, capacidade, velocidade_media, combustivel):
        super().__init__(modelo, capacidade, velocidade_media)
        self.combustivel = combustivel

    def mover(self):
        print(f"O carro {self.modelo} está rodando nas ruas com gasolina {self.combustivel}.")



class Onibus(Transporte):
    def __init__(self, modelo, capacidade, velocidade_media, rota):
        super().__init__(modelo, capacidade, velocidade_media)
        self.rota = rota

    def mover(self):
        print(f"O ônibus {self.modelo} está seguindo pela rota {self.rota} com {self.capacidade} passageiros.")



class Bicicleta(Transporte):
    def __init__(self, modelo, capacidade, velocidade_media, usuario=None):
        super().__init__(modelo, capacidade, velocidade_media)
        self.usuario = usuario 

    def mover(self):
        if self.usuario is None:
            print(f"A bicicleta {self.modelo} está estacionada e disponível para uso.")
        else:
            print(f"{self.usuario} está pedalando a bicicleta {self.modelo} a {self.velocidade_media} km/h!")



def iniciar_viagem(transporte):
    transporte.mover()



carro = Carro("Fiat Uno", 5, 80, "etanol")
onibus = Onibus("Mercedes 5000", 50, 60, "Centro → Bairro")
bike = Bicicleta("Caloi Elite", 1, 20)
bike_usada = Bicicleta("Monark", 1, 15, "João")


transportes = [carro, onibus, bike, bike_usada]

for t in transportes:
    iniciar_viagem(t)