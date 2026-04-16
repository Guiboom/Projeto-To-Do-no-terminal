# 1 - Adicionar
# 2 - Listar
# 3 - Concluir
# 4 - Remover
# 5 - Sair
import time

tarefas=list()

while True:
    try:
        escolha = int(input("""
---------------
1 - Adicionar
2 - Listar
3 - Concluir
4 - Remover
5 - Sair
---------------
Escolha uma opção:"""))

    except:
        print("Digite uma opção valida()")

    if escolha == 1:
        while True:

                tarefa = input("Digite a tarefa que deseja adicionar: ")
                if len(tarefa.strip()) > 0:
                    tarefas.append([tarefa,False])
                    print("Tarefa adicionada com sucesso!")
                    time.sleep(1)
                    break
                else:
                    print("Digite algo para adicionar!")

    if escolha == 2:
        if tarefas:
            for i in range(len(tarefas)):
                if tarefas[i][1] == False:
                    print(f'{i} - {tarefas[i][0]} ( )')
                if tarefas[i][1] == True:
                    print(f'{i} - {tarefas[i][0]} (X)')
        else:
            print("Você não tem nenhuma tarefa para listar!")
            time.sleep(1)
        input("Clique enter para voltar ao menu!")
