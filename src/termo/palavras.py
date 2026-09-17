"""A lista de palavras do jogo: carregar do arquivo, tirar acento e sortear.

Este módulo é só texto — não importa pygame e não sabe nada de janela.
Para acrescentar palavras ao jogo, edite `palavras.txt`: uma palavra por linha, em
MAIÚSCULAS, com acento, sempre com 5 letras. O teste `test_palavras.py` confere isso.
"""

import random
import unicodedata
from pathlib import Path

# O arquivo mora ao lado deste módulo, e não na pasta de onde você roda o jogo.
# Assim `uv run termo` funciona esteja você onde estiver.
ARQUIVO_PALAVRAS = Path(__file__).parent / "palavras.txt"


def sem_acento(palavra: str) -> str:
    """Devolve a palavra em maiúsculas e sem acento: `Ação` vira `ACAO`.

    É assim que o jogo compara as letras. Quem joga digita sem acento, e ninguém deve
    perder uma tentativa por não lembrar onde vai o til.
    """
    # NFD separa a letra do acento ("Á" vira "A" + acento); depois jogamos fora os acentos.
    decomposta = unicodedata.normalize("NFD", palavra)
    return "".join(letra for letra in decomposta if not unicodedata.combining(letra)).upper()


def canonica(palavra: str) -> str:
    """Devolve a palavra em maiúsculas e com cada acento colado na sua letra (forma NFC).

    Por quê: o mesmo LIÇÃO pode vir escrito de dois jeitos que parecem iguais na tela — com o
    Ç inteiro, ou com um C seguido de uma cedilha solta. No segundo, a palavra tem 7
    caracteres em vez de 5, e a grade mostraria a cedilha sozinha num quadradinho.
    """
    return unicodedata.normalize("NFC", palavra.upper())


def carregar_palavras() -> list[str]:
    """Lê `palavras.txt` e devolve as palavras em maiúsculas, na ordem do arquivo.

    Linha vazia e linha começando com `#` são ignoradas, para o arquivo poder ter comentário.
    """
    palavras = []
    for linha in ARQUIVO_PALAVRAS.read_text(encoding="utf-8").splitlines():
        limpa = canonica(linha.strip())
        if limpa and not limpa.startswith("#"):
            palavras.append(limpa)
    return palavras


def sortear_palavra() -> str:
    """Sorteia uma palavra da lista para ser a secreta da próxima partida."""
    return random.choice(carregar_palavras())
