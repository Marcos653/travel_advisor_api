Projeto Desafio Backend 7
Sobre o projeto
Este projeto é o sétimo desafio de Backend, em que desenvolvemos uma API que será integrada ao Frontend. O principal objetivo do nosso desafio é fornecer informações e recursos do banco de dados relacionados a possíveis destinos de viagem, incluindo fotos e um texto chamativo que estimula o usuário a querer visitar o destino selecionado.

Além de oferecer detalhes sobre potenciais destinos de viagem, nossa API também disponibiliza recursos sobre depoimentos de outras pessoas viajantes. E para incrementar ainda mais nossa aplicação, faremos uma integração com Inteligência Artificial.

Funcionalidades
Informações de destinos de viagem: A API fornece dados completos sobre diferentes destinos de viagem, incluindo fotos e descrições instigantes.
Depoimentos de viajantes: Os usuários podem ler depoimentos de outros viajantes sobre os destinos, obtendo uma visão mais realista e pessoal sobre as experiências de viagem.
Integração com Inteligência Artificial: Utilizamos a IA para melhorar a experiência do usuário e fornecer recomendações personalizadas de viagens.
Tecnologias utilizadas
Banco de dados: SQLite
Linguagem de programação: Python
Framework: Django Rest
Como rodar o projeto
Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

Ferramenta de controle de versão Git
Python 3.x
Django e Django REST Framework
SQLite

🎲 Rodando o projeto
# Clone este repositório
$ git clone [<url-do-repositorio>](https://github.com/Marcos653/travel_advisor_api.git)

# Acesse a pasta do projeto no terminal/cmd
$ cd <nome-da-pasta>

# Instale as dependências
$ pip install -r requirements.txt

# Realize as migrações
$ python manage.py migrate

# Execute a aplicação
$ python manage.py runserver

# O servidor inciará na porta: 8000
