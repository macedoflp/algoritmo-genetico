import numpy as np
import random

# Definição dos Access Points (APs)
Aps = {
    "APA": {"localizacao": [0, 0], "cap": 64},
    "APB": {"localizacao": [80, 0], "cap": 64},
    "APC": {"localizacao": [0, 80], "cap": 128},
    "APD": {"localizacao": [80, 80], "cap": 128},
}

# Função para calcular a distância euclidiana para um cliente e um AP
def calcular_distancia(cliente, ap):
    return np.sqrt((cliente[0] - ap[0])**2 + (cliente[1] - ap[1])**2)

# Avaliação da aptidão da solução (distância total + penalização para soluções inválidas)
def avaliar_solucao(solucao, clientes):
    total_distancia = 0
    capacidade_usada = {ap: 0 for ap in Aps.keys()}

    for cliente, ap in zip(clientes, solucao):
        capacidade_usada[ap] += 1
        if capacidade_usada[ap] > Aps[ap]["cap"]:
            return float("inf")  # Penaliza soluções inválidas

        total_distancia += calcular_distancia(cliente, Aps[ap]["localizacao"])

    return total_distancia

# Gerar uma população inicial válida
def gerar_populacao_inicial(tamanho_populacao, num_clientes):
    populacao = []

    for _ in range(tamanho_populacao):
        solucao = []
        capacidadeRestante = {ap: Aps[ap]["cap"] for ap in Aps}

        for _ in range(num_clientes):
            apsValidos = [ap for ap, cap in capacidadeRestante.items() if cap > 0]
            escolhido = random.choice(apsValidos)
            solucao.append(escolhido)
            capacidadeRestante[escolhido] -= 1
        
        populacao.append(solucao)

    return populacao

# Seleção por torneio
def selecao_torneio(populacao, fitness, tamanho_torneio=3):
    participantes = random.sample(range(len(populacao)), tamanho_torneio)
    melhor = min(participantes, key=lambda x: fitness[x])
    return populacao[melhor]

# Cruzamento (crossover)
def crossover(pai1, pai2):
    ponto_corte = random.randint(1, len(pai1) - 1)
    filho = pai1[:ponto_corte] + pai2[ponto_corte:]
    return filho

# Função para corrigir soluções que ultrapassam a capacidade dos APs
def corrigir_solucao(solucao):
    capacidadeRestante = {ap: Aps[ap]["cap"] for ap in Aps}
    nova_solucao = []

    for ap in solucao:
        if capacidadeRestante[ap] > 0:
            nova_solucao.append(ap)
            capacidadeRestante[ap] -= 1
        else:
            # Escolhe um AP que ainda tem capacidade disponível
            ap_valido = random.choice([ap for ap, cap in capacidadeRestante.items() if cap > 0])
            nova_solucao.append(ap_valido)
            capacidadeRestante[ap_valido] -= 1

    return nova_solucao

# Mutação com verificação de capacidade
def mutacao(solucao, taxa_mutacao=0.1):
    capacidadeRestante = {ap: Aps[ap]["cap"] for ap in Aps}
    nova_solucao = solucao[:]

    for i in range(len(solucao)):
        if random.random() < taxa_mutacao:
            apsValidos = [ap for ap, cap in capacidadeRestante.items() if cap > 0]
            if apsValidos:
                nova_solucao[i] = random.choice(apsValidos)

    return corrigir_solucao(nova_solucao)

# Algoritmo Genético garantindo soluções válidas
def algoritmo_genetico(clientes, tamanho_populacao=50, geracoes=100, taxa_mutacao=0.1):
    populacao = gerar_populacao_inicial(tamanho_populacao, len(clientes))

    for geracao in range(geracoes):
        fitness = [avaliar_solucao(solucao, clientes) for solucao in populacao]
        nova_populacao = []

        for _ in range(tamanho_populacao):
            pai1 = selecao_torneio(populacao, fitness)
            pai2 = selecao_torneio(populacao, fitness)
            filho = crossover(pai1, pai2)
            filho = mutacao(filho, taxa_mutacao)
            filho = corrigir_solucao(filho)  # Garante que a solução final é válida
            nova_populacao.append(filho)

        populacao = nova_populacao

    # Retorna a melhor solução encontrada
    melhor_solucao = populacao[np.argmin(fitness)]
    return melhor_solucao   

# Função para carregar clientes a partir do arquivo CSV
def carregar_clientes(caminho_arquivo):
    clientes = []
    with open(caminho_arquivo, "r") as arquivo:
        next(arquivo)  # Ignorar o cabeçalho
        for linha in arquivo:
            _, x, y = linha.strip().split(";")  # Ignora a coluna Cliente
            clientes.append([float(x), float(y)])
    return clientes

# Formatar a solução para exibição
def formatar_solucao(solucao, clientes):
    resultado = {ap: [] for ap in Aps.keys()}
    
    for i, ap in enumerate(solucao):
        resultado[ap].append(i + 1)  # Adiciona o cliente na lista do AP
    
    return resultado

# Carregar clientes do arquivo CSV
clientes = carregar_clientes("ag_data.csv")

# Rodar o algoritmo genético
melhor_solucao = algoritmo_genetico(clientes)

# Formatar a solução
resultado_formatado = formatar_solucao(melhor_solucao, clientes)

# Exibir os resultados
for ap, clientes_conectados in resultado_formatado.items():
    print(f"-------------{ap}--------------")
    print(f"{ap}: {clientes_conectados}")
    print(f"(Quantidade de clientes: {len(clientes_conectados)})")

