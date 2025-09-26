# 👥 Gestão de Clientes com Flask

Este projeto é um sistema web de gestão de clientes desenvolvido em **Python** utilizando o framework **Flask**.  
Ele permite realizar operações de **CRUD** (Create, Read, Update, Delete) com integração a banco de dados PostgreSQL e interface responsiva com Bootstrap.

---

## 🚀 Funcionalidades

- Cadastro de novos clientes
- Listagem de clientes
- Edição de informações
- Exclusão de clientes
- Exibição de detalhes
- Interface dinâmica com AJAX (sem recarregar a página)

---

## 📂 Estrutura

- `main.py` — Arquivo principal, inicializa o app Flask  
- `configuration.py` — Configuração de rotas e banco  
- `database/database.py` — Conexão com o banco PostgreSQL  
- `database/models/cliente.py` — Model da tabela Cliente (Peewee ORM)  
- `routes/home.py` — Rota inicial `/`  
- `routes/cliente.py` — Rotas do CRUD de clientes  
- `static/js/cru.js` — Script JavaScript para requisições dinâmicas  
- `templates/` — Páginas HTML renderizadas pelo Flask  

---

## ⚙️ Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/PietroHenriqueAndrade/gestao-clientes-flask.git
   cd gestao-clientes-flask

   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure o banco de dados criando um arquivo .env na raiz do projeto:
   ```bash
   echo "DATABASE_URL=postgres://usuario:senha@localhost:5432/minha_base" > .env
   ```
⚠️ Substitua usuario, senha e minha_base pelas suas credenciais do PostgreSQL.

5. Execute a aplicação:
   ```bash
   python main.py
   ```
---

## 🛠️ Tecnologias

- Python
- Flask
- Peewee ORM
- PostgreSQL
- Bootstrap 5
-JavaScript (fetch API / AJAX)

---

## 📌 Observações

O projeto utiliza o Peewee ORM para abstração do banco de dados.
O JavaScript (cru.js) foi customizado para interceptar formulários e botões, tornando o CRUD mais dinâmico.
Projeto desenvolvido para fins de aprendizado em Flask + Banco de Dados + Front-end integrado.


---

## 👨‍💻 Autor

Feito por **Pietro Henrique Gomes de Andrade**  
📧 Email: hpietro540@gmail.com 
💼 [LinkedIn](https://www.linkedin.com/in/pietro-andrade-a6061a386)  
🐙 [GitHub](https://github.com/PietroHenriqueAndrade)