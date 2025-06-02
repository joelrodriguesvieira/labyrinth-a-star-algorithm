import heapq

CUSTOS = {
    'S': 1, 
    'E': 1,   
    '.': 1,   
    '?': 2,   
    '_': 3,   
    '#': 4 
}

class No:
    def __init__(self, posicao, custo_g=0, custo_h=0):
        self.posicao = posicao
        self.custo_g = custo_g  # Custo do início até este nó
        self.custo_h = custo_h  # Heurística
        self.custo_f = custo_g + custo_h  # Custo total
        self.pai = None

    def __lt__(self, outro):
        return self.custo_f < outro.custo_f

class Labirinto:
    def __init__(self, matriz):
        self.matriz = matriz
        self.linhas = len(matriz)
        self.colunas = len(matriz[0])
        self.inicio = None
        self.fim = None
        self.encontrar_pontos()

    def encontrar_pontos(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.matriz[i][j] == 'S':
                    self.inicio = (i, j)
                elif self.matriz[i][j] == 'E':
                    self.fim = (i, j)

    def heuristica(self, a, b):
        # Distância de Manhattan
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def obter_vizinhos(self, posicao):
        x, y = posicao
        vizinhos = []
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.linhas and 0 <= ny < self.colunas:
                if CUSTOS[self.matriz[nx][ny]] < CUSTOS["#"]:
                    vizinhos.append((nx, ny))
        return vizinhos

    def busca_a_estrela(self):
        inicio_no = No(self.inicio, custo_h=self.heuristica(self.inicio, self.fim))
        fim_no = No(self.fim)
        lista_aberta = []
        heapq.heappush(lista_aberta, inicio_no)
        nos_visitados = {}

        while lista_aberta:
            no_atual = heapq.heappop(lista_aberta)

            # print(f"Visitando: {no_atual.posicao} | Custo atual: {no_atual.custo_g}, Heurística h: {no_atual.custo_h}")
            
            if no_atual.posicao == fim_no.posicao:
                caminho = []
                while no_atual:
                    caminho.append(no_atual.posicao)
                    no_atual = no_atual.pai
                return caminho[::-1]

            nos_visitados[no_atual.posicao] = no_atual.custo_g

            for vizinho_pos in self.obter_vizinhos(no_atual.posicao):
                custo_g = no_atual.custo_g + CUSTOS[self.matriz[vizinho_pos[0]][vizinho_pos[1]]]
                custo_h = self.heuristica(vizinho_pos, self.fim)
                vizinho_no = No(vizinho_pos, custo_g, custo_h)
                vizinho_no.pai = no_atual

                if vizinho_pos in nos_visitados and nos_visitados[vizinho_pos] <= custo_g:
                    continue

                heapq.heappush(lista_aberta, vizinho_no)

        return None

matriz = [
  ["S", ".", ".", "_", "_"],
  ["_", "_", ".", "_", "_"],
  [".", ".", ".", "_", "_"],
  [".", "_", "_", "_", "_"],
  [".", ".", ".", ".", "E"]
]

labirinto = Labirinto(matriz)
caminho = labirinto.busca_a_estrela()

if caminho:
    print("Caminho encontrado:")
    for passo in caminho:
        print(passo, end=" -> ")
    print("FIM")
else:
    print("Caminho não encontrado")