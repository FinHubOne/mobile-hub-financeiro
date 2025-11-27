# Mobile Hub Financeiro

Sistema de gestão financeira inteligente desenvolvido para o Hackathon.

## 📋 Descrição

O Mobile Hub Financeiro é um MVP (Minimum Viable Product) que oferece um "Extrato Inteligente" para ajudar usuários a visualizar e entender suas transações financeiras de forma clara e organizada.

## 🚀 Funcionalidades

- Carregamento de transações financeiras a partir de dados mockados
- Cálculo automático de saldo (entradas vs saídas)
- Exibição formatada do extrato com categorização
- Resumo financeiro com totais de entradas, saídas e saldo final

## 📦 Requisitos

- Python 3.x (testado com Python 3.12+)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/FinHubOne/mobile-hub-financeiro.git
cd mobile-hub-financeiro
```

## 💻 Como Executar

Execute o script principal com o seguinte comando:

```bash
python3 src/main.py
```

Ou, se estiver em um sistema Unix/Linux:

```bash
chmod +x src/main.py
./src/main.py
```

## 📁 Estrutura do Projeto

```
mobile-hub-financeiro/
├── data/
│   └── extrato.json        # Dados mockados de transações financeiras
├── src/
│   └── main.py             # Script principal
└── README.md               # Este arquivo
```

## 📊 Dados Mockados

O arquivo `data/extrato.json` contém transações financeiras fictícias com os seguintes campos:

- `id`: Identificador único da transação
- `descricao`: Descrição da transação
- `valor`: Valor em reais
- `tipo`: "entrada" ou "saida"
- `categoria`: Categoria da transação (Alimentação, Transporte, Lazer, Saúde, Contas, etc.)
- `data`: Data da transação no formato YYYY-MM-DD

## 🎯 Exemplo de Saída

```
================================================================================
                         EXTRATO INTELIGENTE
================================================================================

ID    Data         Descrição                 Categoria       Tipo       Valor
--------------------------------------------------------------------------------
1     2025-11-01   Supermercado Extra        Alimentação     Saida      R$ 150,75
2     2025-11-05   Salário                   Salário         Entrada  R$ 3.500,00
...
--------------------------------------------------------------------------------

                                                  Total de Entradas:  R$ 6.000,00
                                                  Total de Saídas:    R$ 1.502,95
                                                  -------------------------------
                                                  Saldo Final:        R$ 4.497,05

================================================================================
```

## 🛣️ Roadmap

- [x] Estrutura inicial do projeto
- [x] Dados mockados
- [x] Script de leitura e processamento
- [ ] Interface gráfica (Issue #2)
- [ ] Categorização inteligente
- [ ] Análise de padrões de gastos

## 🤝 Contribuindo

Este projeto foi desenvolvido para o Hackathon. Contribuições são bem-vindas!

## 📄 Licença

Este projeto é de código aberto e está disponível para uso educacional.