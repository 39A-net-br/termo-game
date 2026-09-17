# Guia da aula — do zero ao primeiro PR

Este é o roteiro que você segue **na sua tela** durante a aula. Os slides contam o porquê; aqui
estão os comandos, na ordem, com o que tem de aparecer depois de cada um.

Se você se perder, ache o checkpoint mais próximo e siga dali. Se travar, chame — travar faz parte,
e é melhor resolver na hora do que ficar para trás calado.

| Bloco | O que você faz | Tempo |
| ----- | -------------- | ----- |
| [1](#1-a-sua-máquina-pronta) | Instalar as ferramentas e o plugin | 20 min |
| [2](#2-o-vocabulário-do-git) | Entender o vocabulário do git | 18 min |
| [3](#3-o-jogo-na-sua-máquina) | Forkar, clonar e jogar | 10 min |
| [4](#4-a-sessão-com-o-claude-code) | Pedir uma feature ao Claude Code | 25 min |
| [5](#5-fechar-o-ciclo-pr-revisão-merge) | Abrir o PR, revisar e mergear | 14 min |
| [6](#6-lição-de-casa) | Lição de casa | — |

---

## Antes da aula

Duas coisas precisam estar prontas quando a aula começar. As duas levam tempo de download e login, e
não cabem nos 20 minutos do bloco 1.

1. **Você aceitou o convite para a organização `39A-net-br` no GitHub.** Sem isso o plugin da 39A não
   instala — e ele é o centro da aula. Se não recebeu o convite, peça antes.
2. **Claude Code instalado e logado com a sua conta `@39a.net.br`.** Baixe em
   [claude.com/claude-code](https://claude.com/claude-code) e faça login uma vez, para confirmar que
   abre.

Se você ainda não tem conta no GitHub, crie em [github.com/signup](https://github.com/signup) usando
o seu e-mail da 39A — leva três minutos e evita fila na aula.

---

## 1. A sua máquina pronta

Quatro ferramentas. Cada uma resolve uma parte do dia:

| Ferramenta      | Para que serve                                                              |
| --------------- | --------------------------------------------------------------------------- |
| **Git**         | guarda cada versão do seu trabalho e permite voltar atrás                   |
| **uv**          | baixa o Python e as bibliotecas do projeto, sem você configurar nada        |
| **GitHub CLI**  | conversa com o GitHub pelo terminal — login, fork, pull request             |
| **Claude Code** | o programador que vai trabalhar com você (já instalado, do passo anterior)  |

### Instalar

Abra o **PowerShell** (tecla Windows, digite `powershell`, Enter) e rode um de cada vez:

```powershell
winget install --id Git.Git -e
```

```powershell
winget install --id astral-sh.uv -e
```

```powershell
winget install --id GitHub.cli -e
```

**Feche e abra o PowerShell.** Sem isso ele não enxerga o que você acabou de instalar — é o tropeço
número um do dia.

### Dizer quem você é

O git carimba o seu nome em cada mudança. Use **o mesmo e-mail da sua conta do GitHub**, senão o
GitHub não reconhece que o trabalho é seu:

```powershell
git config --global user.name "Seu Nome"
```

```powershell
git config --global user.email "voce@39a.net.br"
```

Agora conecte o GitHub CLI à sua conta. Ele abre o navegador e pede uma confirmação:

```powershell
gh auth login
```

Responda: **GitHub.com** → **HTTPS** → **sim** para autenticar com as credenciais do git → **Login
with a web browser**. Copie o código que aparecer e cole no navegador.

```powershell
gh auth setup-git
```

### Instalar o plugin da 39A

Abra o Claude Code (digite `claude` no PowerShell) e rode, dentro dele:

```
/plugin marketplace add 39A-net-br/claude-plugins-39a
```

```
/plugin install engenharia@39a
```

**Feche e abra o Claude Code** para ele carregar o plugin.

### Checkpoint

Rode no PowerShell:

```powershell
git --version; uv --version; gh auth status
```

Você tem de ver as duas versões e a frase `Logged in to github.com`.

E dentro do Claude Code, digite `/` — a lista tem de mostrar `nova-feature`, `verificar`, `revisar`
e mais uma dúzia. Se aparecer, o plugin está instalado.

> Deu errado? Vá para [Deu problema?](#deu-problema) no fim deste guia.

---

## 2. O vocabulário do git

Você não precisa decorar. Precisa reconhecer estas sete palavras quando elas aparecerem:

| Palavra          | O que é                                                                                  |
| ---------------- | ---------------------------------------------------------------------------------------- |
| **repositório**  | a pasta do projeto com todo o histórico dela                                             |
| **fork**         | uma cópia do repositório na **sua** conta, onde você mexe à vontade                      |
| **clone**        | essa cópia baixada para a **sua máquina**                                                |
| **branch**       | uma linha de trabalho paralela, para você mexer sem bagunçar o que já funciona           |
| **commit**       | um ponto salvo no histórico, com uma mensagem dizendo o que mudou                        |
| **push**         | mandar os seus commits da máquina para o GitHub                                          |
| **pull request** | o pedido para juntar a sua branch na principal — é onde o trabalho é revisado            |
| **merge**        | aceitar esse pedido; a partir daí a mudança é oficial                                    |

**Por que branch e PR, se o repositório é seu?** Porque é assim na 39A, e o motivo é sério: nos
projetos de verdade, um `push` na branch `hml` ou `main` **é um deploy** — dispara o CI/CD, que
constrói e publica o sistema no ar, sem ninguém apertar botão. Por isso nada entra direto: tudo passa
por PR, que é onde alguém olha antes de virar realidade.

Aqui não há deploy nenhum, e o hábito é o mesmo de propósito.

---

## 3. O jogo na sua máquina

### Fork e clone

```powershell
gh repo fork 39A-net-br/termo-game --clone
```

Ele cria a cópia na sua conta e já baixa para a pasta onde você está. Se perguntar alguma coisa,
responda **sim**.

> Prefere pelo site? Abra <https://github.com/39A-net-br/termo-game>, clique em **Fork** e depois em
> **Code → HTTPS** para copiar o endereço do **seu** fork, e rode
> `git clone https://github.com/<seu-usuario>/termo-game`.

Entre na pasta:

```powershell
cd termo-game
```

### Rodar

```powershell
uv sync
```

```powershell
uv run termo
```

### Checkpoint

A janela do jogo abriu. **Jogue uma partida** — digite uma palavra de 5 letras, Enter, veja as cores.
`Esc` fecha.

Repare no teclado embaixo: ele vai guardando o que você já descobriu.

---

## 4. A sessão com o Claude Code

Na pasta do jogo, abra o Claude Code:

```powershell
claude
```

### Primeiro: deixe ele ler o projeto

Peça:

```
Leia o CLAUDE.md e o DECISOES.md e me explique em três frases como este projeto é organizado.
```

Este repositório foi escrito para ser entendido por ele. O `CLAUDE.md` diz a arquitetura, as regras
e o que não fazer; o `DECISOES.md` guarda o porquê de cada escolha. É isso que separa um palpite de
uma mudança que respeita o que já existe.

### Escolha o que você quer

Abra o [IDEIAS.md](../IDEIAS.md) e escolha **uma** ideia 🟢. Ou invente a sua.

### Peça o objetivo, não o passo

| Em vez de                                              | Diga                                                        |
| ------------------------------------------------------ | ----------------------------------------------------------- |
| "crie uma constante COR_FUNDO e mude o fill do rect"   | "quero o jogo com fundo claro e letras escuras"             |
| "roda o pytest e o ruff"                                | "confere se está tudo certo" (ou `/verificar`)              |
| "escreve um teste pra isso"                             | nada — ele já escreve; o projeto exige                      |

E peça o plano antes:

```
Antes de mexer, me mostre o plano do que você vai fazer.
```

> Também dá para ligar o **modo plano** apertando `Shift+Tab` até aparecer `plan mode` no rodapé.
> Nesse modo ele não altera nada sem você aprovar.

**Leia o plano.** São 30 segundos que evitam meia hora de código errado. Se não for o que você quis,
diga agora — é muito mais barato do que depois de pronto.

### Acompanhe o que ele faz

Enquanto ele trabalha, olhe as linhas que aparecem:

- **Read / Grep** — ele está lendo o projeto antes de escrever. Bom sinal.
- **Edit / Write** — está mexendo num arquivo. O nome do arquivo aparece ali.
- **Bash** — está rodando alguma coisa, normalmente os testes.

Quando ele disser que terminou, cobre a prova:

```
/verificar
```

Roda os testes e a checagem de qualidade, e explica o resultado em português. Depois:

```
/revisar
```

Ele revisa o próprio trabalho como um programador experiente faria, e conta o que encontrou.

### Veja com os seus olhos

```powershell
uv run termo
```

O Claude **não enxerga a sua tela**. Se não ficou como você imaginou, diga o que apareceu e o que
você esperava — essa frase costuma resolver em uma rodada.

### Checkpoint

Você mudou alguma coisa no jogo, os testes estão verdes e você viu a mudança na janela.

---

## 5. Fechar o ciclo: PR, revisão, merge

### Guarde o seu trabalho numa branch

```powershell
git checkout -b feature/20260917-minha-feature
```

```powershell
git add -A
```

```powershell
git commit -m "muda as cores do jogo para o tema claro"
```

A mensagem diz **o que passa a existir**, em português, não o que você fez no código.

### Mande para o GitHub

```powershell
git push -u origin feature/20260917-minha-feature
```

### Abra o pull request

Abra o **seu** fork no navegador: `https://github.com/<seu-usuario>/termo-game`. Vai aparecer uma
faixa amarela com **Compare & pull request**. Clique.

> ⚠️ **Olhe o campo `base repository` no topo.** O GitHub vem com `39A-net-br/termo-game`
> selecionado — e você quer o **seu** fork. Troque para `<seu-usuario>/termo-game`, senão você está
> pedindo para entrar no repositório da aula em vez do seu.

Quem prefere o terminal:

```powershell
gh pr create --base main --repo <seu-usuario>/termo-game --fill
```

### Revise antes de mergear

Clique na aba **Files changed**. Verde é linha que entrou, vermelho é linha que saiu. Você não
precisa entender cada linha — precisa reconhecer se mudou o que você pediu, e só isso.

Essa é a única revisão que existe neste repositório. Nos projetos da 39A, é aqui que outra pessoa
olha antes de a mudança virar oficial.

### Merge

Botão **Merge pull request** → **Confirm merge**.

### Checkpoint

A sua feature está na `main` do seu jogo. O PR fica no histórico, com o que mudou e por quê.

---

## 6. Lição de casa

Três tarefas. **Uma de cada vez**, cada uma na sua branch, cada uma com o seu PR — é o ciclo inteiro
de novo, agora sem ninguém do lado.

### 1. Não deixar digitar letra já descartada

Quando uma letra já apareceu em cinza, ela não está na palavra. O jogo pode se recusar a aceitá-la
de novo, com um aviso.

Peça mais ou menos assim:

```
Quando eu digitar uma letra que já ficou cinza num chute anterior, não aceite a letra e
mostre um aviso dizendo que ela não está na palavra.
```

### 2. Som no jogo

Um som curto ao enviar o chute, outro ao acertar.

```
Toque um som curto quando eu envio um chute e um som diferente quando eu acerto a palavra.
```

### 3. O desafio: uma dica escrita por IA

Você vai receber uma chave de API da Anthropic. Com ela, o jogo pode pedir a uma IA uma **dica** para
a palavra da partida — um botão ou uma tecla que escreve uma frase ajudando, sem entregar a resposta.

**A chave nunca entra no código.** Este repositório é público: uma chave commitada aqui é uma chave
vazada, e ela é sua. Guarde numa variável de ambiente:

```powershell
setx ANTHROPIC_API_KEY "cole-a-sua-chave-aqui"
```

Feche e abra o PowerShell depois. Para conferir se pegou:

```powershell
echo $env:ANTHROPIC_API_KEY
```

O `.gitignore` deste projeto já ignora arquivos `.env`, mas a variável de ambiente é mais segura
ainda: ela não existe dentro da pasta do projeto, então não tem como escapar num commit.

Um bom pedido para começar:

```
Adicione a tecla D, que pede a uma IA da Anthropic uma dica sobre a palavra secreta e mostra
a dica na tela. A chave da API vem da variável de ambiente ANTHROPIC_API_KEY e nunca pode
aparecer no código. Se a chave não estiver configurada, o jogo continua funcionando normalmente
e só avisa que a dica não está disponível.
```

Repare no que esse pedido tem: **o objetivo**, a **regra de segurança** e **o que fazer quando der
errado**. É esse último pedaço que a maioria das pessoas esquece — e é ele que separa uma feature que
funciona na sua máquina de uma que funciona na de todo mundo.

---

## Deu problema?

| O que aconteceu                                | O que fazer                                                                            |
| ---------------------------------------------- | -------------------------------------------------------------------------------------- |
| `git`, `uv` ou `gh` não é reconhecido          | Feche e abra o PowerShell. Se continuar, rode o `winget install` daquela ferramenta de novo. |
| `/plugin marketplace add` reclama de permissão | Você ainda não está na organização `39A-net-br`, ou falta `gh auth setup-git`.          |
| As skills não aparecem ao digitar `/`          | Feche e abra o Claude Code — ele carrega o plugin ao abrir.                             |
| `uv sync` falha ao baixar                      | Proxy ou antivírus da empresa. Tente pela rede do celular.                              |
| A janela do jogo abre e fecha na hora          | Copie a mensagem de erro e cole no Claude Code.                                         |
| Erro falando de `pygame`                       | `uv sync --reinstall`.                                                                  |
| O PR quer ir para o repositório da 39A         | Troque o `base repository` para o **seu** fork, no topo da página do PR.                |
| Os testes ficaram vermelhos e eu não entendo   | Cole o erro no Claude Code e peça: "explique em português simples o que quebrou".       |
| Me perdi                                       | Volte ao checkpoint do bloco em que você está. Nada aqui quebra de verdade.             |
