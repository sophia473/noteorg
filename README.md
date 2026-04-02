🗂️ NoteOrg
Gerenciador de resumos acadêmicos via linha de comando (CLI).

🎯 Problema Real
Estudantes acumulam anotações espalhadas em cadernos, documentos e aplicativos diferentes, sem organização por disciplina. Na hora de revisar para provas, perdem tempo procurando conteúdo e muitas vezes não encontram o que precisam.

💡 Proposta da Solução
O NoteOrg é uma aplicação CLI que permite ao estudante cadastrar, listar, buscar e remover resumos organizados por disciplina, tudo salvo localmente em um arquivo JSON — sem necessidade de internet ou cadastro.

👥 Público-Alvo
Estudantes do ensino médio, técnico ou superior que desejam organizar seus resumos de forma simples e rápida.

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
# Clone o repositório
git clone [https://github.com/seu-usuario/noteorg.git](https://github.com/sophia473/noteorg.git)
cd noteorg

# (Opcional) Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Instale as dependências de desenvolvimento
pip install pytest ruff
▶️ Execução
python src/noteorg.py
O menu interativo será exibido no terminal.

🧪 Rodando os Testes
pytest tests/ -v
🔍 Rodando o Lint
ruff check src/ tests/
📁 Estrutura do Projeto
noteorg/
├── src/
│   └── noteorg.py          # Código principal da aplicação
├── tests/
│   └── test_noteorg.py     # Testes automatizados
├── data/                   # Criado automaticamente (dados locais)
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline de CI com GitHub Actions
├── .gitignore
├── pyproject.toml          # Versão, dependências e configuração
└── README.md
🔢 Versão
1.0.0 — veja pyproject.toml

👤 Autor
Sophia Silva Melo — GitHub

🔗 Repositório
[https://github.com/seu-usuario/noteorg](https://github.com/sophia473/noteorg.git)
