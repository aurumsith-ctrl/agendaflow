class Agendamento:
    def __init__(self, id, nome, servico, preco, data, hora, status="Agendado"):
        self.id = id
        self.nome = nome
        self.servico = servico
        self.preco = float(preco)
        self.data = data
        self.hora = hora
        self.status = status
    def cancelar(self):
        """Ação de cancelar o agendamento"""
        self.status = "Cancelado"

    def esta_ativo(self):
        """Retorna True se o agendaemento não estiver cancelado"""
        return self.status != "Cancelado"

    def __getitem__(self, item):
        """Permite acesso no estilo dicionário (ex: a['hora'])"""
        return getattr(self, item)

    def __setitem__(self, key, value):
        """Permite atribuição no estilo dicionário (ex: a['status'] = 'Cancelado')"""
        setattr(self, key, value)

    def get(self, item, default=None):
        """Permite usar .get() como em dicionários"""
        return getattr(self, item, default)

    def to_dict(self):
        """Converte o objeto de volta para o dicionário para salvar em JSON"""
        return {
            "id": self.id,
            "nome": self.nome,
            "servico": self.servico,
            "preco": self.preco,
            "data": self.data,
            "hora": self.hora,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, dados):
        """Cria um objeto agendado a partir de um dicionário vindo do JSON"""
        return cls(
            id=dados["id"],
            nome=dados["nome"],
            servico=dados["servico"],
            preco=dados.get("preco", 0.0),
            data=dados["data"],
            hora=dados["hora"],
            status=dados.get("status", "Agendado")
        )


SERVICOS = {
    "1": {"nome": "Corte de Cabelo", "preco": 40.00},
    "2": {"nome": "Barba Completa", "preco": 25.00},
    "3": {"nome": "Limpeza de Pele", "preco": 40.00},
    "4": {"nome": "Cabelo e barba", "preco": 60.00},
}

HORARIOS_PADRAO = [
    "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00",
    "15:00", "16:00", "17:00", "18:00", "19:00", "20:00",
]