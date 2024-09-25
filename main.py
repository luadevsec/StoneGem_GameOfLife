import random
from time import sleep
from ascii_art import full, empty  # Importando símbolos de arte ASCII para células

def tela_branca(size):
    tela = []
    for _ in range(size):
        linha = []
        for _ in range(size):
            linha.append(1)
        tela.append(linha)
    return tela

# Função que gera um grid aleatório de tamanho SIZE x SIZE (default é 10x10)
def gerar_grid(tamanho=10):
    grid = []
    for _ in range(tamanho):
        linha = []
        for _ in range(tamanho):
            # Gerar uma célula aleatória: 0 = célula morta, 1 = célula viva
            celula = random.randint(0, 1)
            linha.append(celula)
        grid.append(linha)
    return grid

# Função que exibe o grid na tela com arte ASCII para células vivas e mortas
def exibir_grid(grid):
    for linha in grid:
        for celula in linha:
            # Se a célula for viva (1), exibir "full", se for morta (0), exibir "empty"
            print(full if celula == 1 else empty, end='')
        print()  # Quebrar linha após cada linha do grid
    print()  # Nova linha para separação visual

# Função que calcula o número de vizinhos vivos ao redor de uma célula específica
def contar_vizinhos_vivos(grid, linha, coluna):
    vizinhos = 0
    linhas_totais = len(grid)
    colunas_totais = len(grid[0])
    
    # Verifica as 8 direções ao redor da célula (cima, baixo, esquerda, direita, diagonais)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue  # Pular a célula central (ela mesma)
            linha_vizinha = linha + i
            coluna_vizinha = coluna + j
            if 0 <= linha_vizinha < linhas_totais and 0 <= coluna_vizinha < colunas_totais:
                vizinhos += grid[linha_vizinha][coluna_vizinha]  # Contar célula viva (1)
    return vizinhos

# Função que executa uma iteração do Game of Life e retorna o novo grid atualizado
def executar_vida(grid):
    tamanho = len(grid)
    novo_grid = [[0 for _ in range(tamanho)] for _ in range(tamanho)]  # Criar um grid vazio

    # Itera sobre cada célula do grid
    for linha in range(tamanho):
        for coluna in range(tamanho):
            vizinhos_vivos = contar_vizinhos_vivos(grid, linha, coluna)
            estado_atual = grid[linha][coluna]

            # Regras do Jogo da Vida de Conway:
            # 1. Célula viva com menos de 2 ou mais de 3 vizinhos vivos morre (solidão/superpopulação)
            if estado_atual == 1 and (vizinhos_vivos < 2 or vizinhos_vivos > 3):
                novo_grid[linha][coluna] = 0  # Célula morre
            # 2. Célula viva com 2 ou 3 vizinhos vivos continua viva
            elif estado_atual == 1 and (vizinhos_vivos == 2 or vizinhos_vivos == 3):
                novo_grid[linha][coluna] = 1  # Célula continua viva
            # 3. Célula morta com exatamente 3 vizinhos vivos se torna viva (reprodução)
            elif estado_atual == 0 and vizinhos_vivos == 3:
                novo_grid[linha][coluna] = 1  # Célula nasce
            else:
                novo_grid[linha][coluna] = estado_atual  # Célula mantém o estado atual
    return novo_grid

# Função principal que controla as iterações do jogo e exibe o grid a cada passo
def jogar_vida(iteracoes, tamanho=10):
    grid = gerar_grid(tamanho)  # Gerar o grid inicial aleatório
    for _ in range(iteracoes):
        sleep(0.1)  # Aguardar 0.5 segundos entre cada iteração
        exibir_grid(grid)  # Exibir o estado atual do grid
        grid = executar_vida(grid)  # Atualizar o grid com base nas regras do jogo

# Execução principal do código
if __name__ == '__main__':
    exibir_grid(tela_branca(30))
    sleep(5)
    jogar_vida(iteracoes=10000, tamanho=30)  # Rodar o jogo por 10 iterações com um grid de 20x20
