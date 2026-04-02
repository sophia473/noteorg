"""
Testes automatizados para NoteOrg.
Cobre: caminho feliz, entrada inválida e casos limite.
"""

import os
import sys
import pytest

# Tenta encontrar o arquivo noteorg.py na raiz do projeto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# Caso o arquivo esteja na mesma pasta dos testes, esta linha garante a leitura:
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

try:
    import noteorg
except ImportError:
    # Se falhar, tenta importar o módulo direto (caso esteja em pacotes)
    from . import noteorg


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def arquivo_temporario(tmp_path, monkeypatch):
    """Redireciona DATA_FILE para um arquivo temporário isolado por teste."""
    data_dir = tmp_path / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    fake_path = str(data_dir / "notas.json")
    # Garante que o noteorg use o caminho falso para não sujar seu arquivo real
    monkeypatch.setattr(noteorg, "DATA_FILE", fake_path)
    yield fake_path


# ── Testes: adicionar_nota ────────────────────────────────────────────────────

def test_adicionar_nota_caminho_feliz():
    """Deve adicionar uma nota com todos os campos válidos."""
    nota = noteorg.adicionar_nota("Matemática", "Derivadas", "Regra da cadeia...")
    assert nota["disciplina"] == "Matemática"
    assert nota["titulo"] == "Derivadas"
    assert nota["id"] == 1


def test_adicionar_nota_disciplina_vazia():
    """Deve lançar ValueError quando a disciplina for vazia."""
    with pytest.raises(ValueError, match="disciplina"):
        noteorg.adicionar_nota("", "Título", "Conteúdo")


def test_adicionar_nota_titulo_vazio():
    """Deve lançar ValueError quando o título for vazio."""
    with pytest.raises(ValueError, match="título"):
        noteorg.adicionar_nota("Física", "", "Conteúdo")


def test_adicionar_nota_conteudo_vazio():
    """Deve lançar ValueError quando o conteúdo for vazio."""
    with pytest.raises(ValueError, match="conteúdo"):
        noteorg.adicionar_nota("Física", "Título", "")


def test_adicionar_multiplas_notas_ids_sequenciais():
    """IDs devem ser sequenciais ao adicionar múltiplas notas."""
    n1 = noteorg.adicionar_nota("Bio", "Célula", "Membrana plasmática")
    n2 = noteorg.adicionar_nota("Bio", "DNA", "Dupla hélice")
    assert n1["id"] == 1
    assert n2["id"] == 2


# ── Testes: listar_notas ──────────────────────────────────────────────────────

def test_listar_notas_retorna_todas():
    """Deve retornar todas as notas quando sem filtro."""
    noteorg.adicionar_nota("Química", "Ligações", "Covalente e iônica")
    noteorg.adicionar_nota("Física", "Cinemática", "MRU e MRUV")
    assert len(noteorg.listar_notas()) == 2


def test_listar_notas_lista_vazia():
    """Deve retornar lista vazia quando não há notas."""
    assert noteorg.listar_notas() == []


def test_listar_notas_filtro_disciplina():
    """Deve retornar apenas as notas da disciplina informada."""
    noteorg.adicionar_nota("História", "Revolução", "Francesa e Industrial")
    noteorg.adicionar_nota("Geografia", "Clima", "Tipos climáticos")
    resultado = noteorg.listar_notas("História")
    assert len(resultado) == 1
    assert resultado[0]["disciplina"] == "História"


def test_listar_notas_filtro_disciplina_case_insensitive():
    """Filtro de disciplina deve ser insensível a maiúsculas/minúsculas."""
    noteorg.adicionar_nota("Português", "Crase", "Uso da crase")
    assert len(noteorg.listar_notas("português")) == 1


# ── Testes: buscar_notas ──────────────────────────────────────────────────────

def test_buscar_nota_por_titulo():
    """Deve encontrar nota quando a palavra-chave está no título."""
    noteorg.adicionar_nota("TI", "Algoritmos", "Complexidade Big-O")
    resultado = noteorg.buscar_notas("Algoritmos")
    assert len(resultado) == 1


def test_buscar_nota_por_conteudo():
    """Deve encontrar nota quando a palavra-chave está no conteúdo."""
    noteorg.adicionar_nota("TI", "Estruturas", "Listas encadeadas e árvores")
    resultado = noteorg.buscar_notas("árvores")
    assert len(resultado) == 1


def test_buscar_nota_sem_resultado():
    """Deve retornar lista vazia quando não há correspondência."""
    noteorg.adicionar_nota("TI", "Redes", "Protocolo TCP/IP")
    assert noteorg.buscar_notas("fotossíntese") == []


def test_buscar_nota_palavra_chave_vazia():
    """Deve lançar ValueError para palavra-chave vazia."""
    with pytest.raises(ValueError, match="palavra-chave"):
        noteorg.buscar_notas("")


# ── Testes: remover_nota ──────────────────────────────────────────────────────

def test_remover_nota_existente():
    """Deve remover nota existente e retornar True."""
    nota = noteorg.adicionar_nota("Inglês", "Present Perfect", "Has/Have + particípio")
    assert noteorg.remover_nota(nota["id"]) is True
    assert noteorg.listar_notas() == []


def test_remover_nota_inexistente():
    """Deve retornar False ao tentar remover ID que não existe."""
    assert noteorg.remover_nota(999) is False


def test_remover_nota_nao_afeta_outras():
    """Remover uma nota não deve afetar as demais."""
    n1 = noteorg.adicionar_nota("Arte", "Barroco", "Características do Barroco")
    n2 = noteorg.adicionar_nota("Arte", "Modernismo", "Semana de 22")
    noteorg.remover_nota(n1["id"])
    restantes = noteorg.listar_notas()
    assert len(restantes) == 1
    assert restantes[0]["id"] == n2["id"]
