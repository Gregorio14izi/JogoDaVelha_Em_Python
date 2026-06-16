def validaPosicao(entrada):
    entradaValida = False

    if len(entrada) == 3:
        if entrada[0] in ["0", "1", "2"]:
            if entrada[2] in ["0", "1", "2"]:
                entradaValida = True
    
    return entradaValida


# NOVA FUNÇÃO (Botar o xinho e a bolinhaaaa)
def mostrar(valor):
    if valor == 1:
        return "X"
    elif valor == 2:
        return "O"
    else:
        return " "


havencedor = False
tabuleiro = [0] * 9

# Limpar o tabuleiro
for index in range(9):
    tabuleiro[index] = 0

jogador1 = "Jogador 1"
jogador2 = "Jogador 2"

jogadorDaVez = 1
velha = 1

while True:
    print(f"{mostrar(tabuleiro[0])}{mostrar(tabuleiro[1])}{mostrar(tabuleiro[2])}")
    print(f"{mostrar(tabuleiro[3])}{mostrar(tabuleiro[4])}{mostrar(tabuleiro[5])}")
    print(f"{mostrar(tabuleiro[6])}{mostrar(tabuleiro[7])}{mostrar(tabuleiro[8])}")

    print(f"Digite a posição da sua peça Jogador {jogadorDaVez}")
    jogada = input()

    if validaPosicao(jogada):
        linha = int(jogada[0])
        coluna = int(jogada[2])

        print(f"linha: {linha}; coluna: {coluna}")

        if tabuleiro[3 * linha + coluna] == 0:
            tabuleiro[3 * linha + coluna] = jogadorDaVez

            if (
                (tabuleiro[0] == jogadorDaVez and tabuleiro[1] == jogadorDaVez and tabuleiro[2] == jogadorDaVez) or
                (tabuleiro[3] == jogadorDaVez and tabuleiro[4] == jogadorDaVez and tabuleiro[5] == jogadorDaVez) or
                (tabuleiro[6] == jogadorDaVez and tabuleiro[7] == jogadorDaVez and tabuleiro[8] == jogadorDaVez)
            ):
                havencedor = True
            elif (
                (tabuleiro[0] == jogadorDaVez and tabuleiro[3] == jogadorDaVez and tabuleiro[6] == jogadorDaVez) or
                (tabuleiro[1] == jogadorDaVez and tabuleiro[4] == jogadorDaVez and tabuleiro[7] == jogadorDaVez) or
                (tabuleiro[2] == jogadorDaVez and tabuleiro[5] == jogadorDaVez and tabuleiro[8] == jogadorDaVez)
            ):
                havencedor = True
            elif (
                (tabuleiro[0] == jogadorDaVez and tabuleiro[4] == jogadorDaVez and tabuleiro[8] == jogadorDaVez) or
                (tabuleiro[2] == jogadorDaVez and tabuleiro[4] == jogadorDaVez and tabuleiro[6] == jogadorDaVez)
            ):
                havencedor = True
            else:
                jogadorDaVez = 2 if jogadorDaVez == 1 else 1

            velha += 1
        else:
            print("Jogada inválida!")
    else:
        print("Jogada inválida!")

    if havencedor or velha > 9:
        break

print(f"{mostrar(tabuleiro[0])}{mostrar(tabuleiro[1])}{mostrar(tabuleiro[2])}")
print(f"{mostrar(tabuleiro[3])}{mostrar(tabuleiro[4])}{mostrar(tabuleiro[5])}")
print(f"{mostrar(tabuleiro[6])}{mostrar(tabuleiro[7])}{mostrar(tabuleiro[8])}")
if havencedor:
    print(f"O Morato é muito legal, e parabéns pela vitória jogador {jogadorDaVez}" )
else:
    print("Deu a mãe do Marraaaaaaaaaaaaa")