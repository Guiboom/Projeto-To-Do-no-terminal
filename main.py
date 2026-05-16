# 1 - Adicionar
# 2 - Listar
# 3 - Concluir
# 4 - Remover
# 5 - Sair

import time
import json
import os
import datetime

tarefas = list()

#tenta abrir o arquivo

try:
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

#FUNÇÕES

def listar():#Lista as tarefas
    for i in range(len(tarefas)):
        if not tarefas[i][1]:
            print(f"{i+1} - ( ) |{tarefas[i][0]}| - DATA({tarefas[i][2]}) | PRIORIDADE({tarefas[i][3]})")
        else:
            print(f"{i+1} - (X) |{tarefas[i][0]}| - {tarefas[i][2]} {tarefas[i][3]}")

def limpar_tela():
    # Verifica se o sistema é Windows ('nt') ou Linux/macOS ('posix')
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def data_e_hora_atual():
    data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    return data

def definir_prioridade(chc):
    try:
        if chc == '1':
            chc = "Urgente"
        elif chc == '2':
            chc = "Média"
        elif chc == '3':
            chc = "Baixa"
        else:
            chc = "Prioridade não definida"
    except:
        chc = "Não definida"
    return chc



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
            limpar_tela()
            while True:
                tarefa = input("Digite a tarefa que deseja adicionar: ")
                try:
                    prioridade = definir_prioridade(input("Qual a prioridade da tarefa? [1]'Urgente', [2]'Média', [3]'Baixa'"))
                except:
                    prioridade = "Prioridade não definida"
                if len(tarefa.strip()) > 0 :
                    tarefas.append([tarefa, False, data_e_hora_atual(),prioridade])
                    print("Tarefa adicionada com sucesso!")
                    time.sleep(1)
                    break
                else:
                    print("Digite algo para adicionar!")
            limpar_tela()

        if escolha == 2:  # Listar
            limpar_tela()
            if tarefas:
                listar()
            else:
                print("Você não tem nenhuma tarefa para listar!")
                time.sleep(1)
            input("Clique enter para voltar ao menu!")
            limpar_tela()

        if escolha == 3:  # Concluir
            limpar_tela()
            if tarefas:
                while True:
                    listar()
                    try:    
                        chc = int(input('Qual o número da tarefa você deseja concluir? caso queira cancelar ou parar digite 0:'))-1

                        if chc == -1:
                            print('Operação cancelada!')
                            time.sleep(1)
                            limpar_tela()
                            break

                        if 0 <= chc < len(tarefas):
                            tarefas[chc][1] = True
                            print('Tarefa concluida!')
                            time.sleep(1)
                            limpar_tela()

                        else:
                            print('Número inválido! Essa tarefa não existe.')
                            time.sleep(1)
                            limpar_tela()
                    except:
                        print("Digite um número válido")
                        time.sleep(1)
                        limpar_tela()
            else:
                print("Você não tem nenhuma tarefa para listar!")
                time.sleep(1)
            limpar_tela()

        if escolha == 4: #Remover
            limpar_tela()
            if tarefas:
                while True:
                    listar()
                    try:
                        chc = int(input('Qual o número da tarefa você deseja excluir? caso queira cancelar ou parar digite 0:'))-1
                        if chc == -1:
                            print('Operação cancelada!')
                            time.sleep(1)
                            limpar_tela()
                            break
                        if 0 <= chc < len(tarefas):
                            del tarefas[chc]
                            print('Tarefa excluida!')
                            time.sleep(1)
                            limpar_tela()
                        else:
                            print('Número inválido! Essa tarefa não existe.')
                            time.sleep(1)
                            limpar_tela()
                    except:
                        print("Digite um número válido")
                        time.sleep(1)
                        limpar_tela()
            else:
                print("Você não tem nenhuma tarefa para listar!")
                time.sleep(1)
            limpar_tela()

        if escolha == 5: #Sair
            limpar_tela()
            with open("tarefas.json", "w") as file:
                json.dump(tarefas, file)
            print('Saindo.', end='', flush=True)
            time.sleep(1)
            print('.', end='', flush=True)
            time.sleep(1)
            print('.')
            time.sleep(1)
            limpar_tela()
            break
            
    except ValueError:
        print("Digite uma opção valida()")