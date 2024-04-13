from database import Database
from motorista import Motorista

class MotoristaDAO:
    def __init__(self, database: Database):
        self.db = database

    def criar_motorista(self, motorista: Motorista):
        try:
            self.db.connect()
            self.db.collection.insert_one({
                "nome": motorista.nome,
                "corridas": [],  # Inicialmente, sem corridas
                "nota": motorista.nota
            })
            print(f"Motorista {motorista.nome} criado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar motorista: {e}")
        finally:
            self.db.disconnect()

    def ler_motorista(self, nome: str) -> Motorista:
        try:
            self.db.connect()
            motorista_data = self.db.collection.find_one({"nome": nome})
            if motorista_data:
                return Motorista(nome=motorista_data["nome"], corridas=motorista_data["corridas"], nota=motorista_data["nota"])
            else:
                print("Motorista não encontrado.")
        except Exception as e:
            print(f"Erro ao ler motorista: {e}")
        finally:
            self.db.disconnect()

    def atualizar_motorista(self, motorista: Motorista):
        try:
            self.db.connect()
            self.db.collection.update_one({"nome": motorista.nome}, {"$set": {"nota": motorista.nota}})
            print(f"Motorista {motorista.nome} atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar motorista: {e}")
        finally:
            self.db.disconnect()

    def deletar_motorista(self, nome: str):
        try:
            self.db.connect()
            self.db.collection.delete_one({"nome": nome})
            print(f"Motorista {nome} deletado com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar motorista: {e}")
        finally:
            self.db.disconnect()
