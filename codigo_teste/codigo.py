from dataclasses import dataclass


@dataclass
class Tarefa:
    id: int
    nome: str
    status: str = 'a fazer'

class ListaDeTarefas:
    def __init__(self) -> None:
        self.tarefas: list[Tarefa] = []
        self.contador_id = 1

    def criar_tarefa(self, nome: str, status: str ='a fazer') -> None:
        tarefa = Tarefa(self.contador_id, nome, status)
        self.tarefas.append(tarefa)
        self.contador_id += 1

        return tarefa
    
    def atualizar_tarefa(
        self, 
        nome: str | None = None, 
        status: str | None = None, 
        identificador: int | None = None) -> None:

        for tarefa in self.tarefas:
            if tarefa.id == identificador:
                if nome:
                    tarefa.nome = nome
                break

    def deletar_tarefa(self, identificador: int) -> None:
        for tarefa in self.tarefas:
            if tarefa.id == identificador:
                self.tarefas.remove(tarefa)
            break

    def mostrar_tarefa(self, identificador: int) -> Tarefa | None:
        for tarefa in self.tarefas:
            if tarefa.id == identificador:
                return tarefa
            
        return None
