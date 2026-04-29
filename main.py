# 1 - Adicionar
# 2 - Listar
# 3 - Concluir
# 4 - Remover
# 5 - Sair


#Melhorias para fazer
#Limpar a Tela: Usar o módulo os para limpar o terminal a cada vez que o menu aparece, deixando o visual mais limpo.
#Datas: Adicionar a data em que a tarefa foi criada usando o módulo datetime.
#Prioridade: Permitir que o usuário escolha se a tarefa é "Urgente", "Média" ou "Baixa".

import time
import json

tarefas = list()

try:#tenta abrir o arquivo
    with open("tarefas.json", "r") as file:
        tarefas = json.load(file)
    print("Tarefas carregadas!")

except FileNotFoundError:
    tarefas = []
    print("Arquivo não encontrado. Uma nova lista será criada ao sair.")

except json.JSONDecodeError:
    tarefas = []
    print("O arquivo de salvamento estava vazio ou corrompido. Iniciando nova lista.")

except Exception as e:
    tarefas = []
    print(f"Ocorreu um erro inesperado: {e}")

def listar():#Lista as tarefas
    for i in range(len(tarefas)):
        if not tarefas[i][1]:
            print(f"{i+1} - {tarefas[i][0]} ( )")
        else:
            print(f"{i+1} - {tarefas[i][0]} (X)")


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
                listar()
            else:
                print("Você não tem nenhuma tarefa para listar!")
                time.sleep(1)
            input("Clique enter para voltar ao menu!") 

        if escolha == 3:  # Concluir
            if tarefas:
                while True:
                    listar()
                    try:    
                        chc = int(input('Qual o número da tarefa você deseja concluir? caso queira cancelar ou parar digite 0:'))-1

                        if chc == -1:
                            print('Operação cancelada!')
                            break

                        if 0 <= chc < len(tarefas):
                            tarefas[chc][1] = True
                            print('Tarefa concluida!')

                        else:
                            print('Número inválido! Essa tarefa não existe.')
                    except:
                        print("Digite um número válido")
            else:
                print("Você não tem nenhuma tarefa para listar!")
                time.sleep(1)

        if escolha == 4: #Remover
            if tarefas:
                while True:
                    listar()
                    try:
                        chc = int(input('Qual o número da tarefa você deseja excluir? caso queira cancelar ou parar digite 0:'))-1
                        if chc == -1:
                            print('Operação cancelada!')
                            break
                        if 0 <= chc < len(tarefas):
                            del tarefas[chc]
                            print('Tarefa excluida!')
                        else:
                            print('Número inválido! Essa tarefa não existe.')
                    except:
                        print("Digite um número válido")
            else:
                print("Você não tem nenhuma tarefa para listar!")
                time.sleep(1)


        if escolha == 5: #Sair
            with open("tarefas.json", "w") as file:
                json.dump(tarefas, file)
            print('Saindo.', end='', flush=True)
            time.sleep(1)
            print('.', end='', flush=True)
            time.sleep(1)
            print('.')
            time.sleep(1)
            break



    except ValueError:
        print("Digite uma opção valida()")