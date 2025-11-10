# 🛍️ MiniShop Django

**MiniShop** é um mini e-commerce desenvolvido com **Django 5.2**, permitindo que usuários naveguem por produtos, adicionem itens ao carrinho, finalizem pedidos e visualizem seus históricos.  
O projeto inclui autenticação completa (login, logout e registro), painel administrativo e um tema moderno em tons de **roxo**.

---

## 🚀 Tecnologias utilizadas

- Python 3.13  
- Django 5.2  
- SQLite3  
- Bootstrap 5  
- HTML + CSS (tema roxo personalizado)  
- Pillow  

---

## 📦 Funcionalidades

- Catálogo de produtos  
- Login, logout e registro de usuários  
- Carrinho de compras vinculado ao usuário  
- Finalização e histórico de pedidos  
- Painel administrativo completo  
- Tema escuro moderno e responsivo  

---

## ⚙️ Como executar o projeto localmente

### 1️⃣ Clone o repositório
git clone https://github.com/Bryan-Serafim/minishop_django.git
cd minishop_django

2️⃣ Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate      # Linux / macOS
# ou
.venv\Scripts\activate         # Windows

3️⃣ Instale as dependências
pip install -r requirements.txt


Se não der certo:

pip install django pillow

4️⃣ Execute as migrações e crie o superusuário
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

5️⃣ Inicie o servidor
python manage.py runserver


Acesse:
Home: http://127.0.0.1:8000
Admin: http://127.0.0.1:8000/admin

🧠 Estrutura do banco de dados

O banco de dados contém relacionamentos com chaves estrangeiras, incluindo o modelo User do Django:

User – modelo de autenticação padrão

Category – categorias de produtos

Product – pertence a uma categoria

Order – vinculado a um usuário

OrderItem – vinculado a um pedido e a um produto

🎨 Tema visual

Paleta: roxo, lilás e preto suave

Navbar com gradiente

Cards de produtos com sombras sutis

Tabelas e botões com degradê roxo

👨‍💻 Desenvolvedores

Leonardo Eliel

Alexsandro Ocanha

Bryan Fernando

📜 Licença

Projeto desenvolvido como atividade da disciplina Programação III – IFRO.
