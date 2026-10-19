from tarfile import data_filter

import json

AQUIVOS_DADOS = "agendamentos.json"

def carregar_agendamentos():
    try:
        with open(AQUIVOS_DADOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return []


def salvar_agendamentos(agendamentos):
    with open(AQUIVOS_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(agendamentos, arquivo, ensure_ascii=False, indent=4)


def mostrar_menu():
    """Exibe as opções do sistema."""
    print("\n===== AGENDAFLOW =====")
    print("1 - Cadastrar agendamento")
    print("2 - Listar agendamentos")
    print("3 - Buscar agendamento")
    print("4 - Cancelar agendamento")
    print("5 - Sair")

agendamentos = []


def cadastrar_agendamento(agendamentos):
    """Cadastra um novo agendamento."""

    nome = input("Nome do cliente: ").strip()
    servico = input("Serviço desejado: ").strip()
    data = input("Data (DD/MM/AAAA): ").strip()
    hora = input("Horário (HH:MM): ").strip()

    if not nome or not servico or not data or not hora:
        print("Erro: todos os campos são obrigatórios.")
        return

    agendamento = {
        "id": len(agendamentos) + 1,
        "nome": nome,
        "servico": servico,
        "data": data,
        "hora": hora,
        "status": "Agendado"
    }

    agendamentos.append(agendamento)
    salvar_agendamentos(agendamentos)

    print(f"Agendamento de {nome} cadastrado com sucesso!")




def listar_agendamentos(agendamentos):
    """Exibe todos os agendamentos."""

    if not agendamentos:
        print("Nenhum agendamento cadastrado.")
        return

    print("\n--- AGENDAMENTOS CADASTRADOS ---")

    for agendamento in agendamentos:
        print("-------------------------")
        print(f"ID: {agendamento['id']}")
        print(f"Nome: {agendamento['nome']}")
        print(f"Serviço: {agendamento['servico']}")
        print(f"Data: {agendamento['data']}")
        print(f"Hora: {agendamento['hora']}")
        print(f"Status: {agendamento['status']}")



def buscar_agendamento(agendamentos):
    if not agendamentos:
        print('Nenhum agendamentos cadastrado')
        return

    try:
        id_busca = int(input('Digite o ID do agendamento: '))
    except ValueError:
        print('Digite um ID numérico válido.')
        return

    for agendamento in agendamentos:
        if agendamento["id"] == id_busca:
            print('Agendamento encontrado!')
            print(f"ID: {agendamento['id']}")
            print(f"Nome: {agendamento['nome']}")
            print(f"Serviço: {agendamento['servico']}")
            print(f"Data: {agendamento['data']}")
            print(f"Hora: {agendamento['hora']}")
            print(f"Status: {agendamento['status']}")
            return

    print("Agendamento não encontrado!")




def cancelar_agendamento(agendamentos):
    if not agendamentos:
        print("Nenhum agendamento cadastrado.")
        return
    try:
        id_cancelar = int(input("Digite o ID do agendamento que deseja cancelar: "))
    except ValueError:
        print("Digite um ID numérico válido.")
        return
    for agendamento in agendamentos:
        if agendamento["id"] == id_cancelar:
            agendamento["status"] = "Cancelado"
            salvar_agendamentos(agendamentos)
            print('Agendamento cancelado com sucesso!')
            return
    print("Agendamento não encontrado.")

def main():
    """Controla a execução do programa."""
    agendamentos = carregar_agendamentos()

    print("Bem-vindo ao AgendaFlow!")

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_agendamento(agendamentos)

        elif opcao == "2":
            listar_agendamentos(agendamentos)

        elif opcao == "3":
            buscar_agendamento(agendamentos)

        elif opcao == "4":
            cancelar_agendamento(agendamentos)

        elif opcao == "5":
            print("Encerrando o AgendaFlow. Até logo!")
            break

        else:
            print("Opção inválida! Digite um número de 1 a 5.")


if __name__ == "__main__":
    main()
