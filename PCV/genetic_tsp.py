import math
import random

# === 1. Ler o arquivo TSP e carregar as cidades ===
def carregar_cidades(nome_arquivo):
    with open(nome_arquivo, "r") as f:
        linhas = f.readlines()

    inicio = linhas.index("NODE_COORD_SECTION\n") + 1
    cidades = {}
    for linha in linhas[inicio:]:
        if linha.strip().lower().startswith("eof"):
            break
        partes = linha.strip().split()
        idx = int(partes[0]) - 1
        x, y = int(partes[1]), int(partes[2])
        cidades[idx] = (x, y)

    return cidades



# === 2. Funções auxiliares ===
def distancia(c1, c2):
    return math.hypot(c2[0] - c1[0], c2[1] - c1[1])

def matriz_distancia(cidades):
    n = len(cidades)
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                matriz[i][j] = distancia(cidades[i], cidades[j])
    return matriz

def calcular_distancia_total(rotação, matriz):
    total = 0
    for i in range(len(rotação)):
        a = rotação[i]
        b = rotação[(i + 1) % len(rotação)]
        total += matriz[a][b]
    return total

# === 3. Algoritmo Genético ===
def gerar_populacao(tamanho, num_cidades):
    return [random.sample(range(num_cidades), num_cidades) for _ in range(tamanho)]

def avaliar_populacao(populacao, matriz):
    return [(ind, 1 / calcular_distancia_total(ind, matriz)) for ind in populacao]

def selecao_torneio(fitnesses, k=5):
    return max(random.sample(fitnesses, k), key=lambda x: x[1])[0]

def crossover_ox(pai1, pai2):
    inicio, fim = sorted(random.sample(range(len(pai1)), 2))
    meio = pai1[inicio:fim]
    resto = [gene for gene in pai2 if gene not in meio]
    return resto[:inicio] + meio + resto[inicio:]

def mutacao_swap(individuo, taxa=0.01):
    if random.random() < taxa:
        i, j = random.sample(range(len(individuo)), 2)
        individuo[i], individuo[j] = individuo[j], individuo[i]

def proxima_geracao(fitnesses, taxa_mutacao, elite_size, matriz):
    nova = [ind for ind, _ in sorted(fitnesses, key=lambda x: -x[1])[:elite_size]]
    while len(nova) < len(fitnesses):
        pai1 = selecao_torneio(fitnesses)
        pai2 = selecao_torneio(fitnesses)
        filho = crossover_ox(pai1, pai2)
        mutacao_swap(filho, taxa_mutacao)
        nova.append(filho)
    return nova

# === 4. Executar o algoritmo ===
def algoritmo_genetico(cidades, num_geracoes=1000, tamanho_pop=300, taxa_mutacao=0.02, elite_ratio=0.02):
    matriz = matriz_distancia(cidades)
    populacao = gerar_populacao(tamanho_pop, len(cidades))
    elite_size = max(1, int(tamanho_pop * elite_ratio))

    melhor_distancia = float("inf")
    melhor_rota = None

    for geracao in range(num_geracoes):
        fitnesses = avaliar_populacao(populacao, matriz)
        melhor = min(fitnesses, key=lambda x: 1 / x[1])
        dist = calcular_distancia_total(melhor[0], matriz)

        if dist < melhor_distancia:
            melhor_distancia = dist
            melhor_rota = melhor[0]

        if geracao % 100 == 0 or geracao == num_geracoes - 1:
            print(f"Geração {geracao}: Melhor distância = {dist:.2f}")

        populacao = proxima_geracao(fitnesses, taxa_mutacao, elite_size, matriz)

    print("\nMelhor distância encontrada:", melhor_distancia)
    print("Melhor rota (10 primeiros):", melhor_rota)

# === 5. Rodar ===
if __name__ == "__main__":
    # cidades = carregar_cidades("ch130.tsp")
    cidades2 = carregar_cidades("eil101.tsp")
    print(cidades2)
    # algoritmo_genetico(cidades)
