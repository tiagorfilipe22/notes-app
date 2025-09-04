Development Log - Notes App Project

📝 Conversa inicial sobre desenvolvimento (04 Set 2025)

Projeto Definido

Aplicação de Notas com Markdown Support



Plataforma: Windows (desktop app)

Abordagem: Offline primeiro, depois integração online

Linguagem: Python (preferência do desenvolvedor)



Funcionalidades Principais

Notes App Structure:



Markdown Support ✨

Notes System:



Diaries: Free space to write things + List of Headings

Notes: -  (traço + espaço)

Events: º  (ponto grau + espaço)

Tasks: .  (ponto final + espaço)





Tasks Management:



List of tasks written in Diaries

Can add tasks as well





Events System:



Calendar with marked events

Can add events







Stack Tecnológica Escolhida

UI Framework: CustomTkinter

Porquê escolhido:



UI moderna e limpa

Fácil de usar para Python developers

Boa documentação

Visual contemporâneo



Tecnologias Complementares:

python# UI Framework

CustomTkinter



\# Markdown Processing  

python-markdown + pygments (syntax highlighting)



\# Database

SQLite3 (built-in Python)



\# Text Processing

re (regex) para shortcuts personalizados (-, º, .)



\# Calendar/Date

datetime + calendar (built-in)



\# Future sync

requests + asyncio

Estrutura do Projeto Definida

notes\_app/

├── main.py                 # Entry point

├── requirements.txt

├── config/

│   └── settings.py        # App configurations

├── ui/

│   ├── \_\_init\_\_.py

│   ├── main\_window.py     # Main window

│   ├── components/

│   │   ├── \_\_init\_\_.py

│   │   ├── note\_editor.py # Markdown editor

│   │   ├── sidebar.py     # Sidebar

│   │   └── calendar\_view.py

├── core/

│   ├── \_\_init\_\_.py

│   ├── database.py        # SQLite management

│   ├── markdown\_parser.py # Custom parser

│   └── models.py          # Data models

├── data/

│   └── notes.db          # Database (auto-created)

└── assets/

&nbsp;   └── icons/            # App icons

Setup Processo Completado

1\. Ambiente de Desenvolvimento



OS: Windows

Terminal: PowerShell (para comandos Linux-style: ls, rm, etc.)

Python: Requerido para ambiente virtual

Editor: VS Code recomendado



2\. Dependências Instaladas

bashpip install customtkinter>=5.2.0

pip install markdown>=3.5.0

pip install pygments>=2.16.0

3\. Git + GitHub Configuration



Repository: https://github.com/tiagofilipe22/notes-app.git

Git configurado com Personal Access Token

Merge conflicts resolvidos (.gitignore)

Multi-computer workflow estabelecido



Workflow Multi-Computador Estabelecido

Daily Workflow:

powershell# Antes de trabalhar

git pull origin main



\# Depois de trabalhar  

git add .

git commit -m "Description of changes"

git push origin main

New Computer Setup:

powershell# Clone project

git clone https://github.com/tiagofilipe22/notes-app.git

cd notes-app



\# Setup Python environment

python -m venv notes\_app\_env

notes\_app\_env\\Scripts\\Activate.ps1

pip install -r requirements.txt



\# Run app

python main.py

Código Base Inicial



main.py criado com estrutura básica CustomTkinter

Interface inicial com botões principais

Exemplo de markdown no text area

Status bar implementada

Event handlers básicos definidos



Next Steps Identificados



✅ Setup completo - DONE

🔄 Database SQLite - para guardar notas

📝 Parser Markdown personalizado - para shortcuts (-, º, .)

🎨 Interface completa - editor, sidebar, calendário

📋 Sistema de notas - CRUD operations

✅ Task management - extrair tasks das notas

📅 Calendar integration - eventos marcados

🌐 Online sync - fase futura



Decisões Técnicas

Porquê Python + CustomTkinter:



Developer já familiar com Python

CustomTkinter oferece UI moderna

Boa para aplicações desktop offline

Fácil transição para funcionalidades online



Porquê SQLite:



Built-in Python (sem dependências externas)

Perfeito para aplicações offline

Fácil backup e portabilidade

Suporte a full-text search para notas



Git Workflow:



Multi-computer development requirement

GitHub para backup e sincronização

Personal Access Token configurado

.gitignore personalizado para Python



Questões Resolvidas Durante Setup



Windows Command Line: PowerShell escolhido para comandos Linux-style

Text Editor: VS Code recomendado com extensões Python

Python Installation: Verificação de instalação local

Git Authentication: Personal Access Token configurado

Merge Conflicts: Resolvidos no .gitignore

Virtual Environment: Configurado e funcionando



Estado Atual



✅ Projeto inicializado

✅ Git repository ativo

✅ Ambiente Python configurado

✅ CustomTkinter instalado

✅ Main.py funcional com interface básica

✅ Multi-computer workflow testado



Próxima Sessão de Desenvolvimento

Prioridades:



Database schema design para notes/tasks/events

Markdown parser com shortcuts personalizados

Save/Load functionality

Enhanced UI components





Log criado automaticamente a partir da conversa de desenvolvimento

Última atualização: 04 Setembro 2025

