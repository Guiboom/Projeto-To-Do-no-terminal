# 1 - Adicionar
# 2 - Listar
# 3 - Concluir
# 4 - Remover
# 5 - Sair

import time

tarefas = list()

while True:
    try:
        escolha = int(
            input("""
---------------
1 - Adicionar
2 - Listar
3 - Concluir
4 - Remover
5 - Sair
---------------
Escolha uma opção:""")
        )

        if escolha == 1:  # Adiconar
            while True:
                tarefa = input("Digite a tarefa que deseja adicionar: ")
                if len(tarefa.strip()) > 0:
                    tarefas.append([tarefa, False])
                    print("Tarefa adicionada com sucesso!")
                    time.sleep(1)
                    break
                else:
                    print("Digite algo para adicionar!")

        if escolha == 2:  # Listar
            if tarefas:
                for i in range(len(tarefas)):
                    if not tarefas[i][1]:
                        print(f"{i+1} - {tarefas[i][0]} ( )")
                    else:
                        print(f"{i+1} - {tarefas[i][0]} (X)")
            else:
                print("Você não tem nenhuma tarefa para listar!")
                time.sleep(1)
            input("Clique enter para voltar ao menu!") 

        if escolha == 3:  # Concluir
            if tarefas:
                for i in range(len(tarefas)):
                    if not tarefas[i][1]:
                        print(f"{i+1} - {tarefas[i][0]} ( )")
                    else:
                        print(f"{i+1} - {tarefas[i][0]} (X)")
                while True:
                        chc = int(input('Qual tarefa você deseja concluir? caso queira cancelar ou parar digite 0:'))-1
                        if chc == -1:
                            print('Operação cancelada!')
                            break
                        if 0 <= chc < len(tarefas):
                            tarefas[chc][1] = True
                            print('Tarefa concluida!')
                        else:
                            print('Número inválido! Essa tarefa não existe.')
            else:
                print("Você não tem nenhuma tarefa para listar!")
                time.sleep(1)


        if escolha == 6:
            try:
                print(tarefas)
            except:
                print("Sem nenhum valor")


    except ValueError:
        print("Digite uma opção valida()")