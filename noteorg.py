"""
NoteOrg - Gerenciador de Resumos Acadêmicos
CLI para adicionar, listar, buscar e remover resumos por disciplina.
"""

import json
import os
import sys
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "notas.json")


def carregar_notas() -> list:
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_notas(notas: list) -> None:
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(notas, f, ensure_ascii=False, indent=2)


def adicionar_nota(disciplina: str, titulo: str, conteudo: str) -> dict:
    if not disciplina or not disciplina.strip():
        raise ValueError("A disciplina não pode ser vazia.")
    if not titulo or not titulo.strip():
        raise ValueError("O título não pode ser vazio.")
    if not conteudo or not conteudo.strip():
        raise ValueError("O conteúdo não pode ser vazio.")

    notas = carregar_notas()
    nova_nota = {
        "id": len(notas) + 1,
        "disciplina": disciplina.strip(),
        "titulo": titulo.strip(),
        "conteudo": conteudo.strip(),
        "criado_em": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    notas.append(nova_nota)
    salvar_notas(notas)
    return nova_nota


def listar_notas(disciplina: str = None) -> list:
    notas = carregar_notas()
    if disciplina:
        return [n for n in notas if n["disciplina"].lower() == disciplina.lower()]
    return notas


def buscar_notas(palavra_chave: str) -> list:
    if not palavra_chave or not palavra_chave.strip():
        raise ValueError("A palavra-chave não pode ser vazia.")
    palavra = palavra_chave.lower()
    notas = carregar_notas()
    return [
        n for n in notas
        if palavra in n["titulo"].lower() or palavra in n["conteudo"].lower()
    ]


def remover_nota(nota_id: int) -> bool:
    notas = carregar_notas()
    nova_lista = [n for n in notas if n["id"] != nota_id]
    if len(nova_lista) == len(notas):
        return False
    salvar_notas(nova_lista)
    return True


def exibir_nota(nota: dict) -> None:
    print(f"\n[ID: {nota['id']}] {nota['titulo']}")
    print(f"  Disciplina : {nota['disciplina']}")
    print(f"  Criado em  : {nota['criado_em']}")
    print(f"  Conteúdo   : {nota['conteudo']}")
    print("-" * 50)


def menu():
    print("\n╔══════════════════════════════╗")
    print("║        NoteOrg v1.0.0        ║")
    print("╠══════════════════════════════╣")
    print("║  1. Adicionar resumo         ║")
    print("║  2. Listar todos os resumos  ║")
    print("║  3. Filtrar por disciplina   ║")
    print("║  4. Buscar por palavra-chave ║")
    print("║  5. Remover resumo           ║")
    print("║  0. Sair                     ║")
    print("╚══════════════════════════════╝")
    return input("Escolha uma opção: ").strip()


def main():
    print("Bem-vindo ao NoteOrg!")
    while True:
        opcao = menu()

        if opcao == "1":
            disciplina = input("Disciplina: ").strip()
            titulo = input("Título do resumo: ").strip()
            conteudo = input("Conteúdo: ").strip()
            try:
                nota = adicionar_nota(disciplina, titulo, conteudo)
                print(f"\n✅ Resumo adicionado com ID {nota['id']}!")
            except ValueError as e:
                print(f"\n❌ Erro: {e}")

        elif opcao == "2":
            notas = listar_notas()
            if not notas:
                print("\nNenhum resumo encontrado.")
            else:
                for n in notas:
                    exibir_nota(n)

        elif opcao == "3":
            disciplina = input("Nome da disciplina: ").strip()
            notas = listar_notas(disciplina)
            if not notas:
                print(f"\nNenhum resumo para '{disciplina}'.")
            else:
                for n in notas:
                    exibir_nota(n)

        elif opcao == "4":
            palavra = input("Palavra-chave: ").strip()
            try:
                notas = buscar_notas(palavra)
                if not notas:
                    print(f"\nNenhum resultado para '{palavra}'.")
                else:
                    for n in notas:
                        exibir_nota(n)
            except ValueError as e:
                print(f"\n❌ Erro: {e}")

        elif opcao == "5":
            try:
                id_txt = input("ID do resumo a remover: ").strip()
                nota_id = int(id_txt)
                if remover_nota(nota_id):
                    print(f"\n✅ Resumo {nota_id} removido!")
                else:
                    print(f"\n❌ Resumo com ID {nota_id} não encontrado.")
            except ValueError:
                print("\n❌ ID inválido. Digite um número inteiro.")

        elif opcao == "0":
            print("\nAté logo!")
            sys.exit(0)

        else:
            print("\n❌ Opção inválida.")


if __name__ == "__main__":
    main()
