🗂️ NoteOrg
Gerenciador de resumos acadêmicos via linha de comando (CLI).

🎯 Problema Real
Estudantes acumulam anotações espalhadas em cadernos, documentos e aplicativos diferentes, sem organização por disciplina. Na hora de revisar para provas, perdem tempo procurando conteúdo e muitas vezes não encontram o que precisam.

💡 Proposta da Solução
O NoteOrg é uma aplicação CLI que permite ao estudante cadastrar, listar, buscar e remover resumos organizados por disciplina, tudo salvo localmente em um arquivo JSON.

👥 Público-Alvo
Estudantes que desejam organizar seus resumos de forma simples e rápida.

✨ Funcionalidades
✅ Adicionar resumo vinculado a uma disciplina

✅ Listar todos os resumos

✅ Filtrar resumos por disciplina

✅ Buscar resumos por palavra-chave (título ou conteúdo)

✅ Remover resumo pelo ID

✅ Dados persistidos localmente em data/notas.json

🛠️ Tecnologias Utilizadas
Python 3.10+

Módulos nativos: json, os, sys, datetime

Testes: pytest

Linting: ruff

CI: GitHub Actions

📦 Instalação
Bash
# Clone o repositório
git clone https://github.com/sophia473/noteorg.git
cd noteorg

# (Opcional) Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Instale as dependências de desenvolvimento
pip install pytest ruff
▶️ Execução
Bash
python noteorg.py
O menu interativo será exibido no terminal.

🧪 Rodando os Testes
Bash
pytest . -v
(Comando ajustado para rodar na raiz do projeto).

🔍 Rodando o Lint
Bash
ruff check .
(Comando ajustado para analisar a raiz do projeto).

📁 Estrutura do Projeto
Plaintext
noteorg/
├── .github/
│   └── workflows/
│       └── ci.yml       # Pipeline de CI com GitHub Actions
├── noteorg.py           # Código principal da aplicação (na raiz)
├── test_noteorg.py      # Testes automatizados (na raiz)
├── .gitignore
├── pyproject.toml       # Versão, dependências e configuração
└── README.md
🔢 Versão
1.0.0 — veja pyproject.toml.

👤 Autor
Sophia Silva Melo

🔗 Repositório
https://github.com/sophia473/noteorg
