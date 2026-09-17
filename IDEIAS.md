# Ideias pra vibe codar

Escolha uma, copie o prompt sugerido pro Claude Code (ou escreva do seu jeito) e vá ajustando até
ficar do seu gosto. **Uma de cada vez.**

Legenda: 🟢 fácil (minutos) · 🟡 médio (uma boa meia hora) · 🔴 difícil (o resto do workshop — e tá
ótimo)

> **Terminou uma?** Marque com ✅ no começo do nome dela, na tabela. Assim ninguém pede duas vezes e
> dá pra ver de longe o quanto o jogo já andou.

## 🟢 Fáceis

| Ideia                        | Prompt de exemplo                                                                                                    | Onde o Claude vai mexer                            |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| Tema de cores novo           | "Troque as cores do jogo pra um tema claro, com fundo branco e letras escuras."                                      | constantes de cor no topo de `gui.py`              |
| Acrescentar palavras         | "Adicione 30 palavras novas de 5 letras na lista, de coisas de cozinha."                                             | `src/termo/palavras.txt`                           |
| Mostrar as chances que faltam | "Mostre 'Faltam 3 tentativas' embaixo do título."                                                                   | `desenhar_titulo` em `gui.py` + `tentativas_restantes` |
| Comemoração melhor           | "Quando eu acertar, faça a linha certa piscar em verde e mostre uma mensagem grande no meio da tela."               | `desenhar` em `gui.py`                             |
| Contador de vitórias         | "Mostre no título da janela quantas partidas eu já ganhei nesta sessão."                                             | `Tela` em `gui.py`                                 |
| Destacar a linha atual       | "Deixe a linha que estou digitando com a borda mais grossa, pra eu saber onde estou."                               | `desenhar_casa` em `gui.py`                        |
| Letras maiores               | "Aumente as letras e os quadradinhos — a janela pode crescer, desde que continue cabendo na tela."                  | `LADO_CASA` e as fontes em `gui.py`                |
| Som ao enviar o chute        | "Toque um som curto quando eu envio um chute e outro diferente quando eu acerto."                                   | `tratar_evento` em `gui.py` + pasta `assets/`      |

## 🟡 Médios

| Ideia                        | Prompt de exemplo                                                                                                       | Onde o Claude vai mexer                                          |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Teclado clicável             | "Deixe eu jogar clicando nas letras do teclado da tela, pra jogar só com o mouse."                                       | `gui.py`: guardar o retângulo de cada tecla + `MOUSEBUTTONDOWN`  |
| Animação de virar a letra    | "Quando eu envio o chute, faça os quadradinhos virarem um de cada vez, da esquerda pra direita."                        | `gui.py` com `pygame.time.get_ticks()` — nunca `time.sleep`      |
| Estatísticas salvas          | "Guarde num arquivo quantas partidas eu joguei, quantas ganhei e minha sequência atual, e mostre na tela final."       | módulo puro novo `estatisticas.py` (JSON) + testes + `gui.py`    |
| Resultado pra colar no zap   | "Quando eu terminar, copie pro Ctrl+V um resuminho em quadradinhos coloridos, como o Termo faz."                       | módulo puro `compartilhar.py` + testes + `pygame.scrap`          |
| Recusar palavra inventada    | "Não aceite chute que não é palavra de verdade; me avise 'essa palavra não existe' sem gastar tentativa."              | lista de palavras aceitas em `palavras.py` + `Jogo.enviar` + testes |
| Modo difícil                 | "No modo difícil, sou obrigado a usar no chute seguinte todas as letras que já descobri."                              | regra em `jogo.py` + testes + interruptor na `Tela`              |
| Recusar letra já descartada  | "Quando eu digitar uma letra que já ficou cinza num chute anterior, não aceite a letra e mostre um aviso."             | `Jogo.digitar` em `jogo.py` + `letras_usadas()` + testes         |
| Dica que revela uma letra    | "Adicione a tecla D, que revela uma letra da palavra em troca de uma tentativa."                                       | `Jogo` em `jogo.py` + `tratar_evento` + testes                   |
| Tela inicial                 | "Crie uma tela de abertura com o nome do jogo, as regras em três linhas e um botão Jogar."                             | estado novo na `Tela` (`abertura` / `jogando`)                   |
| Palavras por tema            | "Deixe eu escolher o tema das palavras: animais, comida ou geral."                                                     | vários arquivos `.txt` + `palavras.py` + testes                  |

## 🔴 Difíceis

| Ideia                        | Prompt de exemplo                                                                                                          | Onde o Claude vai mexer                                           |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Dica escrita por IA          | "Adicione a tecla D, que pede a uma IA da Anthropic uma dica sobre a palavra secreta e mostra na tela. A chave vem da variável de ambiente ANTHROPIC_API_KEY e nunca pode aparecer no código; sem chave, o jogo segue funcionando e só avisa." | módulo próprio `dica.py` + `uv add anthropic` + `gui.py`. A chave **nunca** no código |
| Palavra do dia               | "Todo mundo que jogar hoje tem de pegar a mesma palavra, e amanhã tem de mudar."                                            | sorteio pela data em `palavras.py` + testes com data fixa         |
| Modo dueto                   | "Modo com duas palavras ao mesmo tempo, duas grades lado a lado e 7 tentativas — como o dueto do Termo."                    | módulo próprio + duas grades na `Tela`; não infle `jogo.py`       |
| Solucionador                 | "Crie a tecla S, que sugere o melhor chute possível considerando tudo o que já foi descoberto."                             | módulo puro `solucionador.py` + testes                            |
| Gráfico de desempenho        | "Numa tela de estatísticas, desenhe um gráfico de barras de em quantas tentativas eu costumo acertar."                      | `estatisticas.py` + tela nova em `gui.py`                         |
| Palavras de outros tamanhos  | "Deixe eu escolher palavras de 4 a 7 letras; a grade e a janela se ajustam."                                                | `TAMANHO_PALAVRA` vira parâmetro do `Jogo` + geometria em `gui.py` |
| Contra o relógio             | "Modo cronometrado: 3 minutos pra acertar quantas palavras der."                                                            | módulo próprio com o tempo + `Tela`                               |
| Dois jogadores               | "Modo em que uma pessoa digita a palavra secreta e a outra tenta adivinhar."                                                | estado novo na `Tela` + entrada escondida + testes                |

## Dicas pra pedir bem

- Descreva **o que você quer ver**, não como programar: "quero que as letras virem uma de cada vez"
  funciona melhor que "crie uma função de animação".
- Se não ficou como imaginou, diga o que viu e o que esperava. O Claude ajusta.
- Digite `/verificar` de vez em quando. Se algo quebrou, ele conta.
- Terminou algo? `/revisar` antes de commitar.
- Travou? Peça: "Explique em português simples o que esse erro quer dizer e o que fazer."
- Quem roda `uv run termo` é **você** — o Claude não abre janela. Ele te diz o que tem de aparecer.
