def showMENU():
    print("\n###### MENU ######")
    print("[1] Cadastrar uma tarefa")
    print("[2] Alterar uma tarefa")
    print("[3] Excluir uma tarefa")
    print("[4] Listar tarefas")
    print("[5] Sair do programa")

def newTAREFA(tarefas):
    while True:
        description = input("\nCadastre uma nova tarefa, digite a descrição: ")
        tarefas.append(description)
        print("\n==================\nTarefa cadastrada!\n==================")
        cont = input("\nGostaria de cadastrar outra tarefa? (S/N): ").strip().lower()
        if cont != 's':
            break

def alterTAREFA(tarefas):
    while True:
        showTAREFAS(tarefas)
        try:
            index = int(input("\nDigite o número da tarefa cadastrada que deseja alterar: ")) - 1
            if 0 <= index < len(tarefas):
                newDescript_TAREFA = input("\nDigite uma nova descrição da tarefa: ")
                tarefas[index] = newDescript_TAREFA
                print("\n================\nTarefa alterada!\n================")
            else:
                print("\nNúmero de tarefa inválido.")
        except ValueError:
            print("\nInválido. Por favor, insira um número.")
        cont = input("\nGostaria de alterar outra tarefa? (S/N): ").strip().lower()
        if cont != 's':
            break

def deleteTAREFA(tarefas):
    while True:
        showTAREFAS(tarefas)
        try:
            index = int(input("\nDigite o número da tarefa que deseja excluir: ")) - 1
            if 0 <= index < len(tarefas):
                tarefa = tarefas[index]
                print(f"\nTarefa selecionada: {tarefa}")
                confirmacao = input("\nTem certeza que deseja excluir esta tarefa? (S/N): ").strip().lower()
                if confirmacao == 's':
                    del tarefas[index]
                    print("\n================\nTarefa excluída!\n================")
                else:
                 print(f"\n#############\nCancelando...\n#############\n\n====================================\nA tarefa '{tarefa}' não foi excluída!\n====================================")
            else:
                print("\nNúmero de tarefa inválido.")
        except ValueError:
            print("\nInválido. Por favor, insira um número.")
        
        cont = input("\nVocê quer excluir outra tarefa? (S/N): ").strip().lower()
        if cont != 's':
            break


def showTAREFAS(tarefas):
    if tarefas:
        print("\nLista de Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
    else:
        print("\nNenhuma tarefa cadastrada.")

def main():
    tarefas = []
    while True:
        showMENU()
        opcao = input("\nO que você gostaria de fazer? Digite o número correspondente à ação: ")
        if opcao == '1':
            newTAREFA(tarefas)
        elif opcao == '2':
            alterTAREFA(tarefas)
        elif opcao == '3':
            deleteTAREFA(tarefas)
        elif opcao == '4':
            showTAREFAS(tarefas)
            input("\nPressione Enter para voltar ao menu principal...")
        elif opcao == '5':
            confirm_exit = input("\nNÃO HÁ PERSISTÊNCIA DE DADOS! Você realmente quer sair? (S/N): ").strip().lower()
            if confirm_exit == 's':
                print("\nEncerrando...\n_________________________________\n|Programa finalizado com sucesso|\n|_______________________________|")
                break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()



 