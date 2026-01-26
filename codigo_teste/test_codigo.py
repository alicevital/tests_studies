from codigo_teste.codigo import Tarefa
from codigo_teste.codigo import ListaDeTarefas

def test_tarefa_contem_os_campos():
    identificador = 1
    nome = 'Estudar pytest'
    status = 'fazendo'

    tarefa = Tarefa(identificador, nome, status)

    assert tarefa.id == identificador
    assert tarefa.nome == nome
    assert tarefa.status == status


def test_criar_tarefa():
    #arrange
    lista_de_tarefas = ListaDeTarefas()

    #act
    tarefa = lista_de_tarefas.criar_tarefa('teste')

    #assert
    lista_de_tarefas.mostrar_tarefa(tarefa.id)


def test_atualizar_tarefa():
    lista_de_tarefas = ListaDeTarefas()

    tarefa = lista_de_tarefas.atualizar_tarefa('quase terminado')

    lista_de_tarefas.atualizar_tarefa(tarefa.status)


def test_deletar_tarefa():
    lista_de_tarefas = ListaDeTarefas()

    tarefa = lista_de_tarefas.deletar_tarefa('teste')

    lista_de_tarefas.deletar_tarefa(tarefa.id)