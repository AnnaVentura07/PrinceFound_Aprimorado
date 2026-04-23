# Prince Found — Gestão de Cosméticos 🐸✨

Este sistema foi desenvolvido como uma **Situação de Aprendizagem (SA)** para consolidar conceitos de desenvolvimento **Full Stack**. A aplicação é focada no gerenciamento de estoque e vendas para o setor de cosméticos, unindo uma interface web amigável a uma API robusta construída com **Django**.

---

## Novidades desta Versão

* **Sistema de Carrinho**: Lógica de sessão para reserva dinâmica de produtos.
* **Validação de Estoque**: Bloqueio de vendas para produtos esgotados no backend e frontend.
* **UX Inteligente**: Mensagens de feedback que desaparecem automaticamente após **3 segundos**.

---

##  Critérios Técnicos Atendidos

* **CRUD Completo**: Controle total de produtos (Cadastrar, Listar, Editar e Excluir).
* **Gestão Dinâmica**: Monitoramento de quantidades e disponibilidade em tempo real.
* **Segurança Avançada**: 
    * Proteção de rotas via `@login_required`.
    * Tratamento de exceções para objetos relacionados inexistentes.
    * Proteção contra **CSRF** em todos os formulários.
* **Arquitetura REST**: Endpoints prontos para integração via **JSON**.
* **Automação**: Categorização automática de produtos na primeira execução.

---

##  Tecnologias Utilizadas

* **Backend**: Python 3.x & Django Framework.
* **API**: Django REST Framework.
* **Frontend**: HTML5, CSS3 (Design Responsivo) e JavaScript.
* **Banco de Dados**: SQLite (Leve e eficiente para desenvolvimento).

---

##  Como Executar o Projeto

### 1. Clonar o Repositório
```bash
git clone https://github.com/AnnaVentura07/PrinceFound_Aprimorado
cd PrinceFound_Aprimorado
2. Configurar o Ambiente VirtualNo Windows:Bashpython -m venv venv
venv\Scripts\activate
No Linux / macOS:Bashpython3 -m venv venv
source venv/bin/activate
3. Configuração InicialBash# Instalar bibliotecas necessárias
pip install django djangorestframework

# Preparar o banco de dados
python manage.py migrate

# Criar usuário administrador
python manage.py createsuperuser
4. Iniciar a AplicaçãoBashpython manage.py runserver
Acesse o sistema em: http://127.0.0.1:8000/ Mapa de RotasRotaDescriçãoAcesso/accounts/login/Autenticação de usuários.Público/dashboard/Gestão central de produtos.Restrito/carrinho/Itens selecionados para compra.Restrito/dicas/Conteúdo e orientações.Público/api/Dados serializados (JSON).Restrito/admin/Painel administrativo nativo.Admin

Desenvolvido por: Anna Luisa dos Santos Ventura
Projeto Acadêmico: Situação de Aprendizagem (SA).

