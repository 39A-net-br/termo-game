"""Configuração compartilhada dos testes.

Faz o pygame rodar "às cegas" (sem abrir janela nem som), para que a suíte inteira possa
rodar no terminal, dentro do Claude Code ou em qualquer máquina sem tela.
Isso precisa acontecer ANTES de qualquer `import pygame` — por isso fica aqui, no conftest,
que o pytest carrega antes de todos os arquivos de teste.
"""

import os

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
