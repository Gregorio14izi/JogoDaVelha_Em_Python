# 🎮 Jogo da Velha em Python

<img width="800" height="418" alt="demo" src="https://github.com/user-attachments/assets/a670a624-1205-4cfe-9f72-712815d79c69" />

Implementação simples de um jogo da velha para 2 jogadores no terminal.

## ▶️ Como jogar

* Execute o arquivo Python
* Digite a jogada no formato: `linha coluna` (ex: `1-2`)
* Os jogadores se alternam automaticamente

## 🧠 Regras

* Jogador 1 = **X**
* Jogador 2 = **O**
* Não pode jogar em posição ocupada
* O jogo termina quando:

  * Alguém vence 🏆
  * Ou dá empate (velha)

## ⚙️ Lógica

* Tabuleiro representado por uma lista de 9 posições
* Verificação de vitória por:

  * Linhas
  * Colunas
  * Diagonais

## 🔒 Validação

* Entrada deve estar no formato correto (`0 a 2`)
* Jogadas inválidas são rejeitadas

## 💬 Saída

* Mostra o tabuleiro a cada rodada
* Exibe vencedor ou empate ao final
