# 🌊 Fluxo – Financial Wellness Hub
🚀 **Solução Desenvolvida para o Hackathon Financeiro 2025**

<div align="center">
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React">
  <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite">
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS">
  <img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black" alt="Firebase">
</div>

O Fluxo é mais que um banco digital — é um **Assistente de Bem-Estar Financeiro**.
A missão é simples e poderosa: traduzir a complexidade bancária em uma experiência humana, reduzindo a ansiedade financeira e guiando o usuário em direção aos seus objetivos por meio de um extrato inteligente, claro e integrado.

---

### 🎯 O Desafio

Milhões de usuários enfrentam um problema recorrente:
- Extratos cheios de siglas e códigos confusos.
- Apps fragmentados que não conversam entre si.
- Falta de personalização e orientação.

O Fluxo resolve isso ao centralizar informações e transformar dados bancários em linguagem compreensível, visual e útil.

---

### 💡 A Solução

Criamos um **Hub Financeiro Integrado** que reúne:
- ✔️ **Tradução automática de dados** (“bancuês” → português claro).
- ✔️ **Controle visual de gastos** com gráficos e categorias.
- ✔️ **Serviços financeiros essenciais** unificados em um só lugar.
- ✔️ **Insights e recomendações** que melhoram a saúde financeira do usuário.

---

### ✨ Funcionalidades Principais (MVP)

#### 🧠 Extrato Inteligente & Humano
- **Tradução automática** de códigos bancários. (Ex: `PGTO *UBER` → `Uber – Viagens`).
- **Categorização visual** com ícones e cores para fácil identificação.
- **Agrupamento amigável** por data (ex: *Hoje, Ontem, Esta Semana*).

#### 🔗 Hub de Serviços Integrados
- **Pix Inteligente:** Sugere pagamentos recorrentes e lembra transações importantes.
- **Cashback com Propósito:** Cashback direcionado automaticamente para uma meta ou sonho (ex: viagem).
- **Seguro On-Demand:** Ative ou desative proteções com apenas um clique, quando precisar.

#### 🎨 Personalização & Insights
- **Saudações dinâmicas** baseadas no saldo, data e "humor financeiro".
- **Alertas de saúde financeira** e recomendações inteligentes para otimizar gastos.

---

### 🛠️ Tecnologias Utilizadas

| Área                      | Tecnologias                                   |
| ------------------------- | --------------------------------------------- |
| **Front-end**             | `React` + `Vite`                              |
| **Estilização**           | `Tailwind CSS`                                |
| **Ícones**                | `Lucide React`                                |
| **Gráficos**              | `Recharts`                                    |
| **Back-end & Banco de Dados** | `Firebase (Firestore + Authentication)`     |

---

### 🚀 Como Rodar o Projeto Localmente

**Pré-requisitos:**
- **Node.js:** Versão 20.19+ ou 22.12+. Use um gerenciador de versões como o [nvm](https://github.com/nvm-sh/nvm) para facilitar.
- **Conta no Firebase:** Gratuita para começar.

#### 1. Clonar o Repositório
```bash
git clone https://github.com/SEU-USUARIO/fluxo-hackathon.git
cd fluxo-hackathon
```
> *Substitua `SEU-USUARIO` pelo nome de usuário correto do GitHub.*

#### 2. Instalar as Dependências
Execute o comando na raiz do projeto para instalar todos os pacotes necessários.
```bash
npm install
```

#### 3. Configurar o Firebase
- Crie um novo projeto no [Firebase Console](https://console.firebase.google.com/).
- No seu projeto, ative os seguintes serviços:
  - **Firestore Database:** Crie um banco de dados no modo de produção (ou teste, para desenvolvimento).
  - **Authentication:** Habilite o provedor de login "Anônimo".
- Vá para as configurações do projeto (`Project Settings`) e adicione um novo aplicativo Web.
- Copie o objeto de configuração `firebaseConfig` fornecido.
- No código do projeto, cole suas chaves no arquivo de configuração do Firebase (geralmente em um caminho como `src/firebase.js` ou `src/services/firebase.js`).

*Exemplo do que substituir no seu arquivo de configuração:*
```javascript
const firebaseConfig = {
  apiKey: "SUA_API_KEY",
  authDomain: "SEU_AUTH_DOMAIN",
  projectId: "SEU_PROJECT_ID",
  storageBucket: "SEU_STORAGE_BUCKET",
  messagingSenderId: "SEU_MESSAGING_SENDER_ID",
  appId: "SEU_APP_ID"
};
```

#### 4. Executar o Projeto
Inicie o servidor de desenvolvimento local.
```bash
npm run dev
```
O aplicativo estará disponível em `http://localhost:5173` (ou outra porta indicada no terminal).

---

### 📂 Modelagem de Dados (Firestore NoSQL)

A modelagem foi pensada para garantir escalabilidade e clareza usando o padrão de coleções e documentos do Firestore.

#### Coleção `users`
Armazena informações sobre cada usuário.
- **Documento:** ID do Usuário (gerado pelo Firebase Auth)
  - `name`: (string) Nome do usuário.
  - `risk_profile`: (string) Perfil de risco ('Conservador', 'Moderado', 'Arrojado').
  - `createdAt`: (timestamp) Data de criação do perfil.

#### Coleção `transactions`
Armazena todas as transações de todos os usuários.
- **Documento:** ID da Transação (gerado automaticamente)
  - `userId`: (string) Referência ao ID do usuário na coleção `users`.
  - `amount`: (number) Valor da transação.
  - `type`: (string) Tipo de transação ('in' para entrada, 'out' para saída).
  - `raw_description`: (string) A descrição original e não tratada do banco.
  - `clean_description`: (string) A descrição traduzida e limpa (ex: "Uber Viagens").
  - `category`: (string) Categoria da transação (ex: "Transporte", "Alimentação").
  - `createdAt`: (timestamp) Data em que a transação ocorreu.

---

### 🤝 Contribuições

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir *issues* para reportar bugs ou sugerir melhorias, e *pull requests* para implementar funcionalidades.

---

### 📜 Licença

Este projeto está sob a licença MIT. Sinta-se livre para explorar, modificar e compartilhar.
