<h1 align="center">
  <strong>Nova Bank – Gestão de Contas e Transações</strong> <br> 🏦🌐💸💳
</p>

<img src="static/img/novabank.jpeg" alt="tela inicial (dashboard)">

<br>

<p align="center">
  🪓💻 <strong>Tecnologias Utilizadas: </strong>
</p>


<p align="center">
  <img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=black"/> 
  <img src="https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=black"/> 
  <img src="https://img.shields.io/badge/-Tailwind_CSS-06B6D4?style=flat-square&logo=tailwind-css&logoColor=black"/>
  <img src="https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black">
  <img src="https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white"/> 
  <img src="https://img.shields.io/badge/-Jinja2-B41717?style=flat-square&logo=jinja&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Render-000000?style=flat-square&logo=render&logoColor=red"/>
  <img src="https://img.shields.io/badge/Project%20Management-0f172a?style=flat-square&logo=trello&logoColor=white"/>
  <img src="https://img.shields.io/badge/Prototyping-111827?style=flat-square&logo=adobecreativecloud&logoColor=white"/>
</p>



<h1 align="center"> 📌 Sobre o Projeto: </h1>
<p align="center">
Sistema bancário web em Python + Flask que permite:
</p>

- 🏦 Gerenciar contas de usuários;  
- 💸 Realizar depósitos e saques;  
- 📊 Consultar saldo disponível; e  
- 🌐 Interface web interativa e limpa.  

<p align="center">
Um sistema bancário é um software que gerencia contas, transações financeiras e histórico de operações, simulando funcionalidades básicas de um banco real.
</p>

<br>

<h1 align="center"> 🗂️ Estrutura do Projeto – NovaBank 🏦🌐💸💳
</p> </h1>
<p align="center">
<pre>
NovaBank/

├── .flaskenv                  # ⚙️ Configuração FLASK_APP=main.py
├── app.py                     # 🚀 Inicialização da aplicação
├── main.py                    # 📝 Arquivo principal
├── wsgi.py                    # 🌐 Deploy WSGI (Vercel)
├── Procfile                   # 📦 Configuração do Vercel
├── LICENSE                    # 📄 Licença do projeto
├── README.md                  # 📄 Este arquivo (**README.md**)
└── requirements.txt           # 📦 Dependências Python e tecnologias
backending/
├── __init__.py                # 📦 Inicializa o pacote
├── banco.py                   # 💰 Funções de contas e transações
├── cores.py                   # 🎨 Constantes de cores para terminal
static/
    img/                       # 🖼️ Logo/imagem da aplicação
      └── novabank.jpeg  
      └── Banco_do_Brasil.jpeg 
      └── Itau.jpeg         
├── warning.js                 # ⚠️ Scripts de alerta
templates/
├── base.html                  # 📄 Template base
├── index.html                 # 🏠 Página inicial
├── patrocinadores.html        # 🏦 Bancos parceiros   
├── tela_inicio.html           # 🔑 Tela de login/início
├── tela_depositarsaldo.html   # 💵 Tela de depósito
├── tela_saquesaldo.html       # 💸 Tela de saque
└── tela_versaldo.html         # 📊 Tela de visualização de saldo
                              <br> <hr>
                              <p align="center">Jinja2 ⛩️
                              </p>
{% block conteudo x(header, script, principal, footer...)%}{% endblock %}<br>
</pre>
</p>




<h1 align="center"> ⚙️ Versões: </h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square"/> 
  <img src="https://img.shields.io/badge/Flask-2.4.1-000000?style=flat-square"/> 
  <img src="https://img.shields.io/badge/Jinja2-3.1-B41717?style=flat-square"/> 
  <img src="https://img.shields.io/badge/HTML5-5.3-E34F26?style=flat-square"/> 
  <img src="https://img.shields.io/badge/TailwindCSS-3.4.8-38B2AC?style=flat-square"/> 
  <img src="https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=flat-square"/> 
  <img src="https://img.shields.io/badge/Render-Latest-6B5BFF?style=flat-square"/>
  <img src="https://img.shields.io/badge/Prototyping-111827?style=flat-square&logo=adobecreativecloud&logoColor=white"/>
</p>



<h1 align="center">🚀 Deploy: </h1>
<p align="center">
O sistema está pronto para deploy em plataformas que suportam **WSGI**, como o **Render**.
Basta apontar o `wsgi.py` e instalar as dependências listadas em `requirements.txt`.
</p>


<h1 align="center">📄 Licença: </h1>
<p align="center">
Este projeto está licenciado sob a [MIT License](LICENSE).
</p>


<h2 align="center">👨🏻‍💻 Autor deste Repositório: </h2>

<div align="center">

Lucas Paguetti Pereira 🧙‍♂️  
🏫 Instuição: Cesar School 🎓🧡  
📍 Recife, Pernambuco — <strong>Brazil</strong> 🇧🇷  

<a href="https://www.instagram.com/lucpaguetti/">
  <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white">
</a>
<a href="https://github.com/wqiluc">
  <img src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white">
</a>
<a href="https://www.linkedin.com/in/lucas-paguetti-pereira-70267339b/">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white">
</a>
<a href="https://discord.com/users/lucaspaguettipereira">
  <img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white">
</a>
<a href="mailto:lpp2@cesar.school">
  <img src="https://img.shields.io/badge/Email-lpp2@cesar.school-D14836?style=for-the-badge&logo=gmail&logoColor=white">
</a>