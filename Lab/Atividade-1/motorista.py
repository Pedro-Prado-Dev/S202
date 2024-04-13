from corrida import Corrida

class Motorista:
    def __init__(self, nome: str, corridas: list[Corrida] = None, nota: int = 0):
        self.nome = nome
        self.corridas = corridas or []
        self.nota = nota