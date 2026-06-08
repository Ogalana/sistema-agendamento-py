# 💈 Sistema de Gestão e Agendamento para Barbearias

Aplicação web completa desenvolvida como projeto acadêmico para a disciplina de Desenvolvimento Software. O sistema resolve o problema real de agendamento de horários, precificação automatizada e controle de faturamento diário para pequenas barbearias.

---

## 🚀 Funcionalidades Principais

* **Painel de Controle Principal (Dashboard):** Visualização limpa e em ordem cronológica de todos os agendamentos confirmados para o dia.
* **Agendamento Inteligente (CRUD):** Cadastro de clientes com vinculação automática de preços baseado em uma tabela de serviços dinâmica.
* **Soft Delete (Cancelamento):** Em vez de apagar o histórico do banco de dados, o sistema altera o estado do agendamento para "Cancelado", mantendo a integridade dos dados.
* **Módulo de Checkout Simulado:** Simulação de um gateway de pagamento real (Pix/Cartão/Dinheiro) com emulação de latência de rede (delay de 2.5s) e validação em tempo real via JavaScript.
* **Histórico Comercial & Faturamento:** Tela exclusiva que consolida todos os atendimentos finalizados e calcula o faturamento total bruto gerado.

---

## 🛠️ Stack Tecnológica

* **Backend:** Python 3.12 com **Flask**
* **Banco de Dados:** **PostgreSQL** (Hospedado na nuvem via **Supabase**)
* **Frontend:** HTML5, CSS3 e JavaScript Assíncrono
* **Controle de Versão:** Git & GitHub

---

## 📐 Arquitetura do Sistema

O projeto segue o padrão de arquitetura em 3 camadas:
1.  **Camada de Visão (Frontend):** Templates Jinja2 renderizados dinamicamente pelo servidor Flask.
2.  **Camada de Lógica (Backend):** Rotas controladoras no `app.py` responsáveis pelas regras de negócio, cálculo de preços e segurança das requisições.
3.  **Camada de Dados (Database):** Tabelas relacionais no PostgreSQL controlando os estados de cada registro (`Agendado`, `Concluído`, `Cancelado`).

---

## 🔧 Como Executar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   cd seu-repositorio
