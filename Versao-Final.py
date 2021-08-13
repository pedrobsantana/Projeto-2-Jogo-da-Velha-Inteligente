import random
from tabulate import tabulate

def validaEntradaCorreta(letra, numero):
    """
    Confere se as coordenadas recebidas estão dentro das opções válidas
    Parâmetros: letra, numero
    Retorno: True(Opção válida)/False(Opção inválida)
    """
    if letra not in ["A", "B", "C"] or numero not in ["1", "2", "3"]:
        return False
    else:
        return True

def validaEntradaDisponivel(tabuleiro, letra, numero):
    """
    Confere se a coordenada recebida está disponível
    Parâmetros: tabuleiro, letra, numero
    Retorno: True(Disponivel)/False(Indisponivel)
    """
    if tabuleiro[letra][numero-1] != "":
        return False
    else:
        return True

def validaEntrada(tabuleiro, letraNumero):
    """
    Valida entrada do usuário para possíveis erros de digitação, cordenadas inválidas ou já utilizadas
    Parâmetros: tabuleiro, letraNumero (coordenadas da jogada)
    Retorno: letra e numero (coordenadas da jogada validadas)
    """
    # Valida digitações fora do esperado
    try:
        letra, numero = letraNumero.upper().split()
    except:
        return validaEntrada(tabuleiro, input(f"Coordenada inválida, digite uma válida: "))
    # Se entrada correta e disponível retorna, caso contrário chama a função novamente
    if validaEntradaCorreta(letra, numero):
        if validaEntradaDisponivel(tabuleiro, letra, int(numero)):
            return letra, int(numero)
        else:
            return validaEntrada(tabuleiro, input(f"Coordenadas indisponíveis, digite uma livre: ")) 
    else:
        return validaEntrada(tabuleiro, input(f"Coordenada inválida, digite uma válida: "))  

def jogada(tabuleiro):
    """
    Pede a jogada ao usuario e aplica ao tabuleiro
    Parâmetros: tabuleiro
    Retorno: tabuleiro
    """
    letra, numero = validaEntrada(tabuleiro, input(f"Vez do jogador: "))

    tabuleiro[letra][numero-1] = "O"

    return tabuleiro

def parabenizaGanhador(tabuleiro, jogadorGanhou):
    """
    Imprime o tabuleiro e parabeniza o ganhador
    Parâmetros: tabuleiro e jogador que ganhou
    """
    imprimiTabuleiro(tabuleiro)
    # Parabenização invertida pois jogador da vez veio depois da jogada onde a vitória ocorreu
    if jogadorGanhou == "X":
        print("A máquina ganhou!")
    else:
        print("O jogador ganhou! (Não deve acontecer)")

def imprimiTabuleiro(tabuleiro):
    """
    Imprime o tabuleiro utilizando o tabulate para estilização
    Parâmetros: tabuleiro
    """
    print(tabulate(tabuleiro, headers="keys", tablefmt="fancy_grid"))

def confereGanhador(tabuleiro, jogador):
    """
    Confere linhas, colunas e diagonais pelo padrão de vitória
    Parâmetros: tabuleiro
    Retorno: True(Vitória)/False(Sem vitória)
    """
    # Confere Colunas
    if tabuleiro["A"].count(jogador) == 3 or \
       tabuleiro["B"].count(jogador) == 3 or \
       tabuleiro["C"].count(jogador) == 3:
        parabenizaGanhador(tabuleiro, jogador)
        return True
    # Confere Linhas
    elif tabuleiro["A"][0] == tabuleiro["B"][0] == tabuleiro["C"][0] == jogador or \
         tabuleiro["A"][1] == tabuleiro["B"][1] == tabuleiro["C"][1] == jogador or \
         tabuleiro["A"][2] == tabuleiro["B"][2] == tabuleiro["C"][2] == jogador:
        parabenizaGanhador(tabuleiro, jogador)
        return True
    # Confere Diagonais
    elif tabuleiro["A"][0] == tabuleiro["B"][1] == tabuleiro["C"][2] == jogador or tabuleiro["C"][0] == tabuleiro["B"][1] == tabuleiro["A"][2] == jogador:
        parabenizaGanhador(tabuleiro, jogador)
        return True
    return False

def confereEmpate(tabuleiro):
    """
    Confere se há espaços disponíveis no tabuleiro
    Parâmetros: tabuleiro
    Retorno: True(Empate)/False(Sem empate)
    """
    if "" not in tabuleiro["A"] and "" not in tabuleiro["B"] and "" not in tabuleiro["C"]:
        imprimiTabuleiro(tabuleiro)
        print("O jogo empatou!")
        return True
    else:
        return False

def confereFim(tabuleiro, jogador):
    """
    Confere se os possiveis finais (vitória de alguma parte) ou empate ocorreram
    Parâmtros: tabuleiro, jogador (que fez a última jogada)
    Retorno: True(Acabou o jogo)/ False(Não acabou o jogo)
    """
    acabou = False
    acabou = confereGanhador(tabuleiro, jogador)
    if not acabou:
        acabou = confereEmpate(tabuleiro)
    return acabou

def contaJogadaLinha(tabuleiro,jogador,linha):
    counter = 0
    if tabuleiro["A"][linha] == jogador:
        counter += 1
    if tabuleiro["B"][linha] == jogador:
        counter += 1
    if tabuleiro["C"][linha] == jogador:
        counter += 1
    return counter

# especificando as posições do tabuleiro, de 2 a 9 (o 1 é onde a máquina começa jogando)
def posicao2(tabuleiro,jogador):
    if tabuleiro["B"][0] == jogador:
        return True
    else:
        return False

def posicao3(tabuleiro,jogador):
    if tabuleiro["C"][0] == jogador:
        return True
    else:
        return False

def posicao4(tabuleiro,jogador):
    if tabuleiro["A"][1] == jogador:
        return True
    else:
        return False

def posicao5(tabuleiro,jogador):
    if tabuleiro["B"][1] == jogador:
        return True
    else:
        return False

def posicao6(tabuleiro,jogador):
    if tabuleiro["C"][1] == jogador:
        return True
    else:
        return False

def posicao7(tabuleiro,jogador):
    if tabuleiro["A"][2] == jogador:
        return True
    else:
        return False

def posicao8(tabuleiro,jogador):
    if tabuleiro["B"][2] == jogador:
        return True
    else:
        return False

def posicao9(tabuleiro,jogador):
    if tabuleiro["C"][2] == jogador:
        return True
    else:
        return False
# função para marcar a jogada da máquina
def fazJogada(tabuleiro,pos):
    if pos == 2:
        tabuleiro["B"][0] = "X"
    elif pos ==3:
        tabuleiro["C"][0] = "X"
    elif pos == 4:
        tabuleiro["A"][1] = "X"
    elif pos == 5:
        tabuleiro["B"][1] = "X"
    elif pos == 6:
        tabuleiro["C"][1] = "X"
    elif pos == 7:
        tabuleiro["A"][2] = "X"
    elif pos == 8:
        tabuleiro["B"][2] = "X"
    elif pos == 9:
        tabuleiro["C"][2] = "X"
    return tabuleiro
 
def jogadaMaquina(tabuleiro, jogada):
    """
    Processa a jogada que deve ser feita pela máquina
    Parâmetros: tabuleiro, rodada (Contagem de quantas jogadas foram feitas)
    Retorno: tabuleiro
    """
    colunas = ["A","B","C"]
    linhas = [0, 1, 2]
    
    if jogada == 1:
        tabuleiro["A"][0] = "X"
        return tabuleiro
    if jogada == 2:
        if posicao2(tabuleiro,"O") or posicao3(tabuleiro,"O") or posicao5(tabuleiro,"O") or posicao6(tabuleiro,"O"):
            tabuleiro = fazJogada(tabuleiro,7)
            return tabuleiro
        if posicao4(tabuleiro,"O"):
            tabuleiro = fazJogada(tabuleiro,3)
            return tabuleiro
        if posicao7(tabuleiro,"O") or posicao8(tabuleiro,"O") or posicao9(tabuleiro,"O"):
            tabuleiro = fazJogada(tabuleiro,3)
            return tabuleiro
    
    if jogada == 3 and tabuleiro["B"][1] == "":
    ####################################################################################
    # tenta ganhar o jogo nas colunas
    ####################################################################################
        if tabuleiro["A"][0] == "X" and tabuleiro["A"][1] == "X" and tabuleiro["A"][2] == "":
            tabuleiro["A"][2] = "X"
            return tabuleiro
        
        if tabuleiro["A"][0] == "X" and tabuleiro["A"][1] == "" and tabuleiro["A"][2] == "X":
            tabuleiro["A"][1] = "X"
            return tabuleiro
        
        if tabuleiro["A"][0] == "" and tabuleiro["A"][1] == "X" and tabuleiro["A"][2] == "X":
            tabuleiro["A"][0] = "X"
            return tabuleiro
        
        if tabuleiro["B"][0] == "X" and tabuleiro["B"][1] == "X" and tabuleiro["B"][2] == "":
            tabuleiro["B"][2] = "X"
            return tabuleiro
        
        if tabuleiro["B"][0] == "X" and tabuleiro["B"][1] == "" and tabuleiro["B"][2] == "X":
            tabuleiro["B"][1] = "X"
            return tabuleiro
        
        if tabuleiro["B"][0] == "" and tabuleiro["B"][1] == "X" and tabuleiro["B"][2] == "X":
            tabuleiro["B"][0] = "X"
            return tabuleiro

        if tabuleiro["C"][0] == "X" and tabuleiro["C"][1] == "X" and tabuleiro["C"][2] == "":
            tabuleiro["C"][2] = "X"
            return tabuleiro
        
        if tabuleiro["C"][0] == "X" and tabuleiro["C"][1] == "" and tabuleiro["C"][2] == "X":
            tabuleiro["C"][1] = "X"
            return tabuleiro
        
        if tabuleiro["C"][0] == "" and tabuleiro["C"][1] == "X" and tabuleiro["C"][2] == "X":
            tabuleiro["C"][0] = "X"
            return tabuleiro
        
        if tabuleiro["A"][0] == "X" and tabuleiro["B"][0] == "X" and tabuleiro["C"][0] == "":
            tabuleiro["C"][0] = "X"
            return tabuleiro
        
        if tabuleiro["A"][0] == "X" and tabuleiro["B"][0] == "" and tabuleiro["C"][0] == "X":
            tabuleiro["B"][0] = "X"
            return tabuleiro

        if tabuleiro["A"][0] == "" and tabuleiro["B"][0] == "X" and tabuleiro["C"][0] == "X":
            tabuleiro["A"][0] = "X"
            return tabuleiro
        ####################################################################################
        # tenta ganhar o jogo nas linhas
        ####################################################################################
        if tabuleiro["A"][1] == "X" and tabuleiro["B"][1] == "X" and tabuleiro["C"][1] == "":
            tabuleiro["C"][1] = "X"
            return tabuleiro
        
        if tabuleiro["A"][1] == "X" and tabuleiro["B"][1] == "" and tabuleiro["C"][1] == "X":
            tabuleiro["B"][1] = "X"
            return tabuleiro

        if tabuleiro["A"][1] == "" and tabuleiro["B"][1] == "X" and tabuleiro["C"][1] == "X":
            tabuleiro["A"][1] = "X"
            return tabuleiro
        
        if tabuleiro["A"][2] == "X" and tabuleiro["B"][2] == "X" and tabuleiro["C"][2] == "":
            tabuleiro["C"][2] = "X"
            return tabuleiro
        
        if tabuleiro["A"][2] == "X" and tabuleiro["B"][2] == "" and tabuleiro["C"][2] == "X":
            tabuleiro["B"][2] = "X"
            return tabuleiro

        if tabuleiro["A"][2] == "" and tabuleiro["B"][2] == "X" and tabuleiro["C"][2] == "X":
            tabuleiro["A"][2] = "X"
            return tabuleiro
        ####################################################################################
        # tenta ganhar o jogo nas diagonais
        ####################################################################################
        if tabuleiro["A"][0] == "X" and tabuleiro ["B"][1] == "X" and tabuleiro ["C"][2] == "":
            tabuleiro ["C"][2] = "X"
            return tabuleiro

        if tabuleiro["A"][0] == "X" and tabuleiro ["B"][1] == "" and tabuleiro ["C"][2] == "X":
            tabuleiro ["B"][1] = "X"
            return tabuleiro
        
        if tabuleiro["A"][0] == "" and tabuleiro ["B"][1] == "X" and tabuleiro ["C"][2] == "X":
            tabuleiro ["A"][0] = "X"
            return tabuleiro
        
        if tabuleiro["A"][2] == "" and tabuleiro ["B"][1] == "X" and tabuleiro ["C"][0] == "X":
            tabuleiro ["A"][2] = "X"
            return tabuleiro
        
        if tabuleiro["A"][2] == "X" and tabuleiro ["B"][1] == "" and tabuleiro ["C"][0] == "X":
            tabuleiro ["B"][1] = "X"
            return tabuleiro
        
        if tabuleiro["A"][2] == "X" and tabuleiro ["B"][1] == "X" and tabuleiro ["C"][0] == "":
            tabuleiro ["C"][0] = "X"
            return tabuleiro
            
        #######################################################################################
        #  Estratégia de nó tático
        # #####################################################################################    
        
        if posicao2(tabuleiro,"O") and posicao9(tabuleiro,"O"):
            tabuleiro = fazJogada(tabuleiro,7)
            return tabuleiro

        tabuleiro = fazJogada(tabuleiro,5)
        return tabuleiro

    if jogada == 3 or jogada == 4 or jogada == 5:
    ####################################################################################
    # tenta ganhar o jogo nas colunas
    ####################################################################################
        if tabuleiro["A"][0] == "X" and tabuleiro["A"][1] == "X" and tabuleiro["A"][2] == "":
            tabuleiro["A"][2] = "X"
            return tabuleiro
        
        if tabuleiro["A"][0] == "X" and tabuleiro["A"][1] == "" and tabuleiro["A"][2] == "X":
            tabuleiro["A"][1] = "X"
            return tabuleiro
        
        if tabuleiro["A"][0] == "" and tabuleiro["A"][1] == "X" and tabuleiro["A"][2] == "X":
            tabuleiro["A"][0] = "X"
            return tabuleiro
        
        if tabuleiro["B"][0] == "X" and tabuleiro["B"][1] == "X" and tabuleiro["B"][2] == "":
            tabuleiro["B"][2] = "X"
            return tabuleiro
        
        if tabuleiro["B"][0] == "X" and tabuleiro["B"][1] == "" and tabuleiro["B"][2] == "X":
            tabuleiro["B"][1] = "X"
            return tabuleiro
        
        if tabuleiro["B"][0] == "" and tabuleiro["B"][1] == "X" and tabuleiro["B"][2] == "X":
            tabuleiro["B"][0] = "X"
            return tabuleiro

        if tabuleiro["C"][0] == "X" and tabuleiro["C"][1] == "X" and tabuleiro["C"][2] == "":
            tabuleiro["C"][2] = "X"
            return tabuleiro
        
        if tabuleiro["C"][0] == "X" and tabuleiro["C"][1] == "" and tabuleiro["C"][2] == "X":
            tabuleiro["C"][1] = "X"
            return tabuleiro
        
        if tabuleiro["C"][0] == "" and tabuleiro["C"][1] == "X" and tabuleiro["C"][2] == "X":
            tabuleiro["C"][0] = "X"
            return tabuleiro
        
        if tabuleiro["A"][0] == "X" and tabuleiro["B"][0] == "X" and tabuleiro["C"][0] == "":
            tabuleiro["C"][0] = "X"
            return tabuleiro
        
        if tabuleiro["A"][0] == "X" and tabuleiro["B"][0] == "" and tabuleiro["C"][0] == "X":
            tabuleiro["B"][0] = "X"
            return tabuleiro

        if tabuleiro["A"][0] == "" and tabuleiro["B"][0] == "X" and tabuleiro["C"][0] == "X":
            tabuleiro["A"][0] = "X"
            return tabuleiro
        ####################################################################################
        # tenta ganhar o jogo nas linhas
        ####################################################################################
        if tabuleiro["A"][1] == "X" and tabuleiro["B"][1] == "X" and tabuleiro["C"][1] == "":
            tabuleiro["C"][1] = "X"
            return tabuleiro
        
        if tabuleiro["A"][1] == "X" and tabuleiro["B"][1] == "" and tabuleiro["C"][1] == "X":
            tabuleiro["B"][1] = "X"
            return tabuleiro

        if tabuleiro["A"][1] == "" and tabuleiro["B"][1] == "X" and tabuleiro["C"][1] == "X":
            tabuleiro["A"][1] = "X"
            return tabuleiro
        
        if tabuleiro["A"][2] == "X" and tabuleiro["B"][2] == "X" and tabuleiro["C"][2] == "":
            tabuleiro["C"][2] = "X"
            return tabuleiro
        
        if tabuleiro["A"][2] == "X" and tabuleiro["B"][2] == "" and tabuleiro["C"][2] == "X":
            tabuleiro["B"][2] = "X"
            return tabuleiro

        if tabuleiro["A"][2] == "" and tabuleiro["B"][2] == "X" and tabuleiro["C"][2] == "X":
            tabuleiro["A"][2] = "X"
            return tabuleiro
        ####################################################################################
        # tenta ganhar o jogo nas diagonais
        ####################################################################################
        if tabuleiro["A"][0] == "X" and tabuleiro ["B"][1] == "X" and tabuleiro ["C"][2] == "":
            tabuleiro ["C"][2] = "X"
            return tabuleiro

        if tabuleiro["A"][0] == "X" and tabuleiro ["B"][1] == "" and tabuleiro ["C"][2] == "X":
            tabuleiro ["B"][1] = "X"
            return tabuleiro
        
        if tabuleiro["A"][0] == "" and tabuleiro ["B"][1] == "X" and tabuleiro ["C"][2] == "X":
            tabuleiro ["A"][0] = "X"
            return tabuleiro
        
        if tabuleiro["A"][2] == "" and tabuleiro ["B"][1] == "X" and tabuleiro ["C"][0] == "X":
            tabuleiro ["A"][2] = "X"
            return tabuleiro
        
        if tabuleiro["A"][2] == "X" and tabuleiro ["B"][1] == "" and tabuleiro ["C"][0] == "X":
            tabuleiro ["B"][1] = "X"
            return tabuleiro
        
        if tabuleiro["A"][2] == "X" and tabuleiro ["B"][1] == "X" and tabuleiro ["C"][0] == "":
            tabuleiro ["C"][0] = "X"
            return tabuleiro

        ####################################################################################
        # evita perder o jogo nas diagonais
        ####################################################################################
        if tabuleiro["C"][0] == "O" and tabuleiro ["B"][1] == "O" and tabuleiro["A"][2] == "":
            tabuleiro["A"][2] = "X"
            return tabuleiro
        
        if tabuleiro["B"][1] == "O" and tabuleiro ["A"][2] == "O" and tabuleiro ["C"][0] == "":
            tabuleiro ["C"][0] = "X"
            return tabuleiro
        
        if tabuleiro["B"][1] == "" and tabuleiro ["A"][2] == "O" and tabuleiro ["C"][0] == "O":
            tabuleiro ["B"][1] = "X"
            return tabuleiro
    
        ####################################################################################
        # evita perder o jogo nas colunas
        ####################################################################################
        if tabuleiro["B"][0] == "O" and tabuleiro["B"][1] == "O" and tabuleiro["B"][2] == "":
            tabuleiro["B"][2] = "X"
            return tabuleiro
        
        if tabuleiro["B"][0] == "O" and tabuleiro["B"][2] == "O" and tabuleiro["B"][1] == "":
            tabuleiro["B"][1] = "X"
            return tabuleiro
        
        if tabuleiro["B"][1] == "O" and tabuleiro["B"][2] == "O" and tabuleiro["B"][0] == "":
            tabuleiro["B"][0] = "X"
            return tabuleiro

        if tabuleiro["C"][0] == "O" and tabuleiro["C"][1] == "O" and tabuleiro["C"][2] == "":
            tabuleiro["C"][2] = "X"
            return tabuleiro
        
        if tabuleiro["C"][0] == "O" and tabuleiro["C"][2] == "O" and tabuleiro["C"][1] == "":
            tabuleiro["C"][1] = "X"
            return tabuleiro
        
        if tabuleiro["C"][1] == "O" and tabuleiro["C"][2] == "O" and tabuleiro["C"][0] == "":
            tabuleiro["C"][0] = "X"
            return tabuleiro

        ####################################################################################
        # evita perder o jogo nas linhas
        ####################################################################################
        if tabuleiro["A"][1] == "O" and tabuleiro["B"][1] == "O" and tabuleiro["C"][1] == "":
            tabuleiro["C"][1] = "X"
            return tabuleiro
        
        if tabuleiro["A"][1] == "O" and tabuleiro["C"][1] == "O" and tabuleiro["B"][1] == "":
            tabuleiro["B"][1] = "X"
            return tabuleiro
        
        if tabuleiro["B"][1] == "O" and tabuleiro["C"][1] == "O" and tabuleiro["A"][1] == "":
            tabuleiro["A"][1] = "X"
            return tabuleiro

        if tabuleiro["A"][2] == "O" and tabuleiro["B"][2] == "O" and tabuleiro["C"][2] == "":
            tabuleiro["C"][2] = "X"
            return tabuleiro
        
        if tabuleiro["A"][2] == "O" and tabuleiro["C"][2] == "O" and tabuleiro["B"][2] == "":
            tabuleiro["B"][2] = "X"
            return tabuleiro
        
        if tabuleiro["B"][2] == "O" and tabuleiro["C"][2] == "O" and tabuleiro["A"][2] == "":
            tabuleiro["A"][2] = "X"
            return tabuleiro
    
        ####################################################################################
        # faz jogada aleatória
        #################################################################################### 
        entradaValida = False
        while not entradaValida:
            randColuna = random.randint(0,len(colunas)-1)
            randLinha = random.randint(0,len(linhas)-1)
            entradaValida = validaEntradaDisponivel(tabuleiro, colunas[randColuna], linhas[randLinha]+1)
        
        tabuleiro[colunas[randColuna]][linhas[randLinha]] = "X"
        return tabuleiro

# Dicionário para registro do jogo
tabuleiro = {
                " ": ["1", "2", "3"],
                "A": ["", "", ""],
                "B": ["", "", ""],
                "C": ["", "", ""]
            }
# Flag que é acionada para finalizar o jogo
acabou = False
# String para acompanhar qual o jogador da vez
jogador = "X"
# Inteiro para contar em qual rodada estamos
rodada = 0

print("Instruções:\nDigite as coordenadas da sua jogada no formato letra e numero (Exs: 'A 1', 'B 2', 'C 3', etc)\n")
# Loop enquanto jogo não acabar que cicla em jogada da maquina e jogada do usuario com as devidas validações de entrada e fim de jogo

while not acabou:
    rodada += 1
    tabuleiro = jogadaMaquina(tabuleiro, rodada)
    acabou = confereFim(tabuleiro, "X")
    if not acabou:
        imprimiTabuleiro(tabuleiro)
        tabuleiro = jogada(tabuleiro)
        acabou = confereFim(tabuleiro, "O")