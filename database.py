import json
from models import Agendamento

ARQUIVO_DADOS = "agendamentos.json"

def carregar_agendamentos():
    """Lê o JSON e transforma cada item em um Objeto da classe Agendamento"""
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            dados = json.load(f)
            # Transforma a lista de dicionários em lista de objetos Afendamento
            return [Agendamento.from_dict(d) for d in dados]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_agendamentos(agendamentos):
    """Converte os Objetos em dicionários e grava no arquivo JSON"""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        # Chama .to_dict() em cada agendamento (compatível com objetos e dicts)
        dados = [a.to_dict() if hasattr(a, "to_dict") else a for a in agendamentos]
        json.dump(dados, f, ensure_ascii=False, indent=4)

