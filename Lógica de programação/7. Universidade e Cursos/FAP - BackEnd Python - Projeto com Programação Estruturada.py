import os
import time


universidades = {}

def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_universidade(nome_universidade):
    if nome_universidade not in universidades:
        universidades[nome_universidade] = []
        print(f"\nUniversidade '{nome_universidade}' adicionada com êxito!")
    else:
        print(f"\nUniversidade com mesmo nome já cadastrada...")
    time.sleep(2)
    clear_screen()

def adicionar_curso(nome_universidade, nome_curso):
    if nome_universidade in universidades:
        universidades[nome_universidade].append(nome_curso)
        print(f"\nCurso '{nome_curso}' adicionado à universidade '{nome_universidade}' com êxito!")
    else:
        print(f"\nNenhum Universidade com o nome: '{nome_universidade}' foi registrada.")
    time.sleep(2)
    clear_screen()

def excluir_universidade(nome_universidade):
    if nome_universidade in universidades:
        del universidades[nome_universidade]
        print(f"\nUniversidade '{nome_universidade}' excluída com sucesso.")
    else:
        print(f"\nNenhum Universidade com o nome: '{nome_universidade}' foi registrada.")
    time.sleep(2)
    clear_screen()

def excluir_curso(nome_universidade, nome_curso):
    if nome_universidade in universidades:
        if nome_curso in universidades[nome_universidade]:
            universidades[nome_universidade].remove(nome_curso)
            print(f"Curso '{nome_curso}' excluído da Universidade '{nome_universidade}' com sucesso.")
        else:
            print(f"Curso '{nome_curso}' não encontrado na universidade '{nome_universidade}'.")
    else:
        print(f"\nNenhum Universidade com o nome: '{nome_universidade}' foi registrada")
    time.sleep(2)
    clear_screen()

def listar_cursos_universidades():
    clear_screen()
    if universidades:
        for nome_universidade, cursos in universidades.items():
            print(f"Universidade: {nome_universidade}")
            if cursos:
                for curso in cursos:
                    print(f"  - Curso: {curso}")
            else:
                print("  - Nenhum curso cadastrado")
    else:
        print("Nenhuma Universidade cadastrada.")
    input("\nPressione Enter para continuar...")
    clear_screen()

def menu():
    while True:
        clear_screen()
        print("###### MENU ######")
        print("\n[1] Adicionar Universidade")
        print("[2] Adicionar Curso")
        print("[3] Excluir Curso ou Universidade")
        print("[4] Listar Cursos e Universidades")
        print("[5] Sair do programa")
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            nome_universidade = input("\nDigite o nome da Universidade: ")
            adicionar_universidade(nome_universidade)
        elif opcao == '2':
            nome_universidade = input("\nDigite o nome da Universidade: ")
            nome_curso = input("Digite o nome do Curso: ")
            adicionar_curso(nome_universidade, nome_curso)
        elif opcao == '3':
            clear_screen()
            print("[1] Excluir Universidade")
            print("[2] Excluir Curso")
            sub_opcao = input("\nEscolha uma opção: ")
            if sub_opcao == '1':
                nome_universidade = input("\nDigite o nome da Universidade: ")
                excluir_universidade(nome_universidade)
            elif sub_opcao == '2':
                nome_universidade = input("\nDigite o nome da Universidade: ")
                nome_curso = input("Digite o nome do Curso: ")
                excluir_curso(nome_universidade, nome_curso)
            else:
                print("\nOpção inválida.")
                time.sleep(2)
                clear_screen()
        elif opcao == '4':
            listar_cursos_universidades()
        elif opcao == '5':
            print("\nSaindo do programa", end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            print("\n")
            time.sleep(1)
            clear_screen()
            break
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            clear_screen()


if __name__ == "__main__":
    menu()
