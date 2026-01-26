from codigo_teste.codigo import ListaDeTarefas

def test_full_lista_de_tarefas():
    lista = ListaDeTarefas()

    # criar tarefa
    tarefa = lista.criar_tarefa("Estudar pytest")
    assert tarefa.id == 1
    assert tarefa.nome == "Estudar pytest"
    assert tarefa.status == "a fazer"

    # mostrar tarefa
    tarefa_encontrada = lista.mostrar_tarefa(1)
    assert tarefa_encontrada is not None
    assert tarefa_encontrada.nome == "Estudar pytest"

    # atualizar tarefa
    lista.atualizar_tarefa(
        identificador=1, 
        nome="Estudar pytest com e2e", 
        status="a fazer",
    )

    tarefa_atualizada = lista.mostrar_tarefa(1)
    assert tarefa_atualizada.nome == "Estudar pytest com e2e"
    assert tarefa_atualizada.status == "a fazer"

    lista.deletar_tarefa(1)
    assert lista.mostrar_tarefa(1) is None
    assert lista.tarefas == []





