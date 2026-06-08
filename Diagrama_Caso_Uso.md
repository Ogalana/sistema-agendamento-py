```mermaid
graph LR
    %% Ator posicionado do lado esquerdo (fora da caixa)
    Admin["👤 Barbeiro / Admin"]

    %% Limite do Sistema (System Boundary igual ao 'Online Book Store' do seu modelo)
    subgraph BarbaNav ["💈 Sistema Barbearia"]
        UC1(["Visualizar Dashboard <br> (Agendamentos do Dia)"])
        UC2(["Gerenciar Agendamentos <br> (CRUD)"])
        UC3(["Cancelar Agendamento <br> (Soft Delete)"])
        UC4(["Realizar Checkout <br> (Simulação de Pagamento)"])
        UC5(["Visualizar Histórico <br> e Faturamento Bruto"])
    end

    %% Associações com linhas simples sem setas (padrão estrito da UML)
    Admin --- UC1
    Admin --- UC2
    Admin --- UC3
    Admin --- UC4
    Admin --- UC5

    %% Estilização padrão acadêmica (fundo claro nas elipses e bordas finas)
    style Admin fill:#f9f9f9,stroke:#333,stroke-width:1px
    style UC1 fill:#ffffff,stroke:#333,stroke-width:1px
    style UC2 fill:#ffffff,stroke:#333,stroke-width:1px
    style UC3 fill:#ffffff,stroke:#333,stroke-width:1px
    style UC4 fill:#ffffff,stroke:#333,stroke-width:1px
    style UC5 fill:#ffffff,stroke:#333,stroke-width:1px