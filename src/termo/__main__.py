"""Ponto de entrada do jogo: `uv run termo` ou `uv run python -m termo`."""

from termo.gui import Tela


def main() -> None:
    """Abre a janela do jogo e roda até a pessoa fechar."""
    Tela().rodar()


if __name__ == "__main__":
    main()
