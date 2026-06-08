```mermaid
classDiagram
    direction LR
    class Agendamento {
        +int id
        +string cliente
        +string servico
        +string horario
        +string status
        +string forma_pagamento
        +float valor
    }

    class Sistema {
        +get_db_connection()
        +TABELA_PRECOS
    }

    Agendamento --> Sistema