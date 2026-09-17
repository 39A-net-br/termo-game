"""Testes da lista de palavras.

Estes testes olham o arquivo `palavras.txt` em vez de olhar só o código. É de propósito:
a lista é a parte que mais gente vai querer editar, e um erro ali (palavra de 6 letras,
palavra repetida, minúscula) só apareceria como bug estranho no meio de uma partida.
"""

from termo.palavras import (
    ARQUIVO_PALAVRAS,
    carregar_palavras,
    sem_acento,
    sortear_palavra,
)

MINIMO_DE_PALAVRAS = 100


def linhas_de_palavra() -> list[str]:
    """As linhas de palavras.txt como estão no arquivo, sem os comentários e as linhas vazias."""
    linhas = ARQUIVO_PALAVRAS.read_text(encoding="utf-8").splitlines()
    return [linha for linha in linhas if linha.strip() and not linha.strip().startswith("#")]


# ----- O arquivo de palavras -----


def test_a_lista_tem_palavras_suficientes():
    """Poucas palavras fariam a mesma secreta voltar toda hora e o jogo perder a graça."""
    assert len(linhas_de_palavra()) >= MINIMO_DE_PALAVRAS


def test_toda_palavra_tem_cinco_letras():
    """A grade tem cinco colunas: uma palavra maior ou menor quebraria a partida em que caísse."""
    erradas = [linha for linha in linhas_de_palavra() if len(sem_acento(linha)) != 5]
    assert erradas == []


def test_toda_palavra_esta_em_maiusculas_e_sem_espaco():
    """O arquivo é a fonte da verdade e precisa estar limpo.

    Por quê: o código conserta minúscula e espaço ao carregar, então um erro aqui passaria
    despercebido — até alguém comparar duas listas e achar que são diferentes.
    """
    sujas = [linha for linha in linhas_de_palavra() if linha != linha.strip().upper()]
    assert sujas == []


def test_so_existem_letras_do_alfabeto():
    """Número, hífen e espaço no meio da palavra não têm tecla no jogo — seriam impossíveis."""
    estranhas = [
        linha
        for linha in linhas_de_palavra()
        if not sem_acento(linha).isalpha() or not sem_acento(linha).isascii()
    ]
    assert estranhas == []


def test_nao_existe_palavra_repetida():
    """Palavra repetida aumenta a chance dela ser sorteada, sem ninguém perceber.

    A comparação é sem acento: SABIA e SABIÁ seriam o mesmo chute para quem joga.
    """
    palavras = linhas_de_palavra()
    assert len(palavras) == len({sem_acento(palavra) for palavra in palavras})


def test_a_lista_esta_em_ordem_alfabetica():
    """A ordem é o que permite achar o lugar de uma palavra nova sem ler 500 linhas.

    A ordem ignora o acento, para ÁGUIA ficar perto de AGORA em vez de ir para o fim.
    """
    palavras = linhas_de_palavra()
    assert palavras == sorted(palavras, key=sem_acento)


# ----- Carregar e sortear -----


def test_carregar_ignora_comentarios():
    """As linhas de comentário do topo do arquivo não podem virar palavra sorteável."""
    assert all(not palavra.startswith("#") for palavra in carregar_palavras())


def test_sortear_devolve_uma_palavra_da_lista():
    """O sorteio não inventa palavra: sai sempre de palavras.txt."""
    assert sortear_palavra() in carregar_palavras()


# ----- Tirar o acento -----


def test_sem_acento_troca_acento_e_cedilha():
    """É esta função que deixa quem joga digitar sem acento."""
    assert sem_acento("Ação") == "ACAO"
    assert sem_acento("ÁGUIA") == "AGUIA"


def test_sem_acento_nao_muda_o_tamanho_da_palavra():
    """Tirar o acento não pode encurtar nem alongar a palavra.

    Por quê: a grade e a comparação contam letras. Se LIÇÃO virasse quatro ou seis letras
    ao perder os acentos, o jogo compararia posições trocadas e acusaria erro no lugar certo.
    """
    for palavra in carregar_palavras():
        assert len(sem_acento(palavra)) == len(palavra)
