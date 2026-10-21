from datetime import datetime
from models import Agendamento, SERVICOS, HORARIOS_PADRAO
from database import carregar_agendamentos, salvar_agendamentos


def obter_horario_disponiveis(data, agendamentos):
    """Retorna uma lista de horários livres para uma data específica."""
    horarios_ocupados = [
        item["hora"] for item in agendamentos
        if item["data"] == data and item["status"] != "Cancelado"
    ]
    return [h for h in HORARIOS_PADRAO if h not in horarios_ocupados]


def exibir_agendamento(agendamento):
    """Exibe os detalhes formatados de um agendamento."""
    print("-------------------------")
    print(f"ID: {agendamento['id']}")
    print(f"Nome: {agendamento['nome']}")
    print(f"Serviço: {agendamento['servico']} (R$ {agendamento.get('preco', 0.0):.2f})")
    print(f"Data: {agendamento['data']}")
    print(f"Hora: {agendamento['hora']}")
    print(f"Status: {agendamento['status']}")


def mostrar_menu():
    """Exibe as opções do sistema."""
    print("\n===== AGENDAFLOW =====")
    print("1 - Cadastrar agendamento")
    print("2 - Listar todos os agendamentos")
    print("3 - Listar agendamentos por data")
    print("4 - Buscar agendamento por ID")
    print("5 - Cancelar agendamento")
    print("6 - Relatório financeiro / métricas")
    print("7 - Sair")


def cadastrar_agendamento(agendamentos):
    """Cadastra um novo agendamento com serviço e horário guiados."""
    print("\n--- NOVO AGENDAMENTO ---")
    nome = input("Nome do cliente: ").strip()
    if not nome:
        print("Erro: O nome é obrigatório.")
        return

    # 1. Escolha do Serviço
    print("\nServiços disponíveis:")
    for codigo, info in SERVICOS.items():
        print(f"{codigo} - {info['nome']} (R$ {info['preco']:.2f})")

    opcao_servico = input("Escolha o número do serviço: ").strip()
    if opcao_servico not in SERVICOS:
        print("Erro: Serviço inválido!")
        return
    servico_escolhido = SERVICOS[opcao_servico]

    # 2. Escolha e Validação da Data (não aceita passado)
    data = input("\nData desejada (DD/MM/AAAA): ").strip()
    try:
        data_obj = datetime.strptime(data, "%d/%m/%Y").date()
        if data_obj < datetime.now().date():
            print("Erro: Não é possível agendar em datas passadas!")
            return
    except ValueError:
        print("Erro: Data inválida! Use o formato DD/MM/AAAA (ex: 25/10/2026).")
        return

    # 3. Listagem dos Horários Livres para essa Data
    horarios_livres = obter_horario_disponiveis(data, agendamentos)
    if not horarios_livres:
        print(f"Desculpe, todos os horários para o dia {data} já estão ocupados!")
        return

    print(f"\nHorários disponíveis para {data}:")
    for i, h in enumerate(horarios_livres, 1):
        print(f"{i} - {h}")

    try:
        opcao_hora = int(input("Escolha o número do horário: "))
        if opcao_hora < 1 or opcao_hora > len(horarios_livres):
            print("Erro: Opção de horário inválida!")
            return
        hora_escolhida = horarios_livres[opcao_hora - 1]
    except ValueError:
        print("Erro: Digite um número válido para o horário.")
        return

    # 4. Criando e Salvando o Agendamento
    proximo_id = max([a["id"] for a in agendamentos], default=0) + 1

    agendamento = Agendamento(
        id=proximo_id,
        nome=nome,
        servico=servico_escolhido["nome"],
        preco=servico_escolhido["preco"],
        data=data,
        hora=hora_escolhida,
        status="Agendado"
    )

    agendamentos.append(agendamento)
    salvar_agendamentos(agendamentos)

    print(f"\n✅ Agendamento #{proximo_id} confirmado para {nome}!")
    print(f"Serviço: {servico_escolhido['nome']} (R$ {servico_escolhido['preco']:.2f})")
    print(f"Data e Hora: {data} às {hora_escolhida}")


def listar_agendamentos(agendamentos):
    """Exibe todos os agendamentos cadastrados."""
    if not agendamentos:
        print("Nenhum agendamento cadastrado.")
        return

    print("\n--- TODOS OS AGENDAMENTOS CADASTRADOS ---")
    for agendamento in agendamentos:
        exibir_agendamento(agendamento)


def listar_por_data(agendamentos):
    """Filtra e exibe agendamentos de uma data específica."""
    if not agendamentos:
        print("Nenhum agendamento cadastrado no sistema.")
        return

    data_busca = input("Digite a data para consultar (DD/MM/AAAA): ").strip()

    # Validação do formato
    try:
        datetime.strptime(data_busca, "%d/%m/%Y")
    except ValueError:
        print("Erro: Formato de data inválido! Use DD/MM/AAAA.")
        return

    # Filtra os agendamentos daquela data
    agendamentos_do_dia = [a for a in agendamentos if a["data"] == data_busca]

    if not agendamentos_do_dia:
        print(f"Nenhum agendamento encontrado para o dia {data_busca}.")
        return

    # Ordena pelo horário (ex: 08:00 antes de 09:00)
    agendamentos_do_dia.sort(key=lambda x: x["hora"])

    print(f"\n--- AGENDAMENTOS DO DIA {data_busca} ({len(agendamentos_do_dia)} encontrado(s)) ---")
    for a in agendamentos_do_dia:
        exibir_agendamento(a)


def buscar_agendamento(agendamentos):
    """Busca um agendamento específico pelo ID."""
    if not agendamentos:
        print("Nenhum agendamento cadastrado.")
        return

    try:
        id_busca = int(input("Digite o ID do agendamento: "))
    except ValueError:
        print("Digite um ID numérico válido.")
        return

    for agendamento in agendamentos:
        if agendamento["id"] == id_busca:
            print("\nAgendamento encontrado!")
            exibir_agendamento(agendamento)
            return

    print("Agendamento não encontrado!")


def cancelar_agendamento(agendamentos):
    """Altera o status de um agendamento para Cancelado."""
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
            if agendamento["status"] == "Cancelado":
                print("Este agendamento já estava cancelado.")
                return

            agendamento.cancelar()
            salvar_agendamentos(agendamentos)
            print(f"Agendamento #{id_cancelar} cancelado com sucesso!")
            return

    print("Agendamento não encontrado.")


def exibir_relatorio_financeiro(agendamentos):
    """Calcula e exibe métricas de negócio e previsão de faturamento."""
    if not agendamentos:
        print("Nenhum dado cadastrado para gerar relatório.")
        return

    total_agendados = [a for a in agendamentos if a["status"] == "Agendado"]
    total_cancelados = [a for a in agendamentos if a["status"] == "Cancelado"]

    # Faturamento previsto (apenas de quem está com status Agendado)
    faturamento_previsto = sum(a.get("preco", 0.0) for a in total_agendados)
    faturamento_perdido = sum(a.get("preco", 0.0) for a in total_cancelados)

    # Contagem de serviços mais procurados
    contagem_servicos = {}
    for a in total_agendados:
        serv = a["servico"]
        contagem_servicos[serv] = contagem_servicos.get(serv, 0) + 1

    print("\n================ RELATÓRIO DO NEGÓCIO ================")
    print(f"Total de registros no sistema: {len(agendamentos)}")
    print(f"✅ Agendamentos confirmados:   {len(total_agendados)}")
    print(f"❌ Agendamentos cancelados:     {len(total_cancelados)}")
    print("------------------------------------------------------")
    print(f"💰 Faturamento previsto:        R$ {faturamento_previsto:.2f}")
    print(f"📉 Valor cancelado (perdido):   R$ {faturamento_perdido:.2f}")
    print("------------------------------------------------------")
    print("Serviços mais agendados:")
    if contagem_servicos:
        # Ordena do mais vendido para o menos vendido
        for serv, qtd in sorted(contagem_servicos.items(), key=lambda item: item[1], reverse=True):
            print(f"  • {serv}: {qtd} agendamento(s)")
    else:
        print("  (Nenhum agendamento ativo no momento)")
    print("======================================================")


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
            listar_por_data(agendamentos)
        elif opcao == "4":
            buscar_agendamento(agendamentos)
        elif opcao == "5":
            cancelar_agendamento(agendamentos)
        elif opcao == "6":
            exibir_relatorio_financeiro(agendamentos)
        elif opcao == "7":
            print("Encerrando o AgendaFlow. Até logo!")
            break
        else:
            print("Opção inválida! Digite um número de 1 a 7.")


if __name__ == "__main__":
    main()
