# AgendaFlow 💈

Sistema inteligente de gestão de agendamentos e faturamento para barbearias e prestadores de serviços, desenvolvido em Python com arquitetura modular, Orientação a Objetos (POO) e persistência em banco de dados SQLite.

---

## 🚀 Funcionalidades

- **Agendamento Guiado Inteligente:**
  - Seleção por catálogo de serviços com preços dinâmicos.
  - Exibição automática dos próximos dias úteis disponíveis (com omissão de domingos e dias sem vagas).
  - Listagem em tempo real apenas dos horários livres, impedindo conflito de agenda.
- **Gestão Completa de Horários:**
  - Consulta de todos os agendamentos cadastrados.
  - Filtro de agendamentos por data específica com ordenação cronológica.
  - Busca de agendamento por ID único.
  - Cancelamento de horários sem perda de histórico.
- **Relatório de Negócio e Métricas Financeiras:**
  - Cálculo de faturamento previsto (agendamentos confirmados).
  - Métrica de faturamento perdido (cancelamentos).
  - Ranking dos serviços mais procurados da barbearia.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+** (Módulos nativos: `sqlite3`, `datetime`, `json`)
- **SQLite3:** Banco de dados relacional para persistência de dados.
- **Programação Orientada a Objetos (POO):** Modelagem com a classe `Agendamento`, métodos de domínio e encapsulamento.
- **Git & GitHub:** Versionamento com histórico semântico de commits.

---

## 📂 Estrutura do Projeto

```text
├── models.py       # Classes de domínio (Agendamento) e tabelas de apoio (Serviços, Horários, Dias)
├── database.py     # Camada de persistência (conexão, criação de tabelas, SELECT e INSERT/REPLACE)
├── main.py         # Interface de linha de comando (CLI) e lógica dos fluxos do usuário
├── .gitignore      # Arquivos e diretórios ignorados no versionamento
└── README.md       # Documentação do projeto
```

---

## 💻 Como Rodar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   cd "projeto1 - SEMNOME"
   ```

2. **Execute o programa:**
   ```bash
   python3 main.py
   ```
   *(O banco de dados SQLite `agendaflow.db` será criado automaticamente na primeira execução).*
