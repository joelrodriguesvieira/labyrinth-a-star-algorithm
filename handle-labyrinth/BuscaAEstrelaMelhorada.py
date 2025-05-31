import heapq

class BuscarAStarMelhorada:
  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False


  def busca_astar(self, vertice_inicio):

    #prioridade (custo+heuristica), custo, vertice_atual, caminho
    fila_prioridade = [(0+vertice_inicio.distancia_objetivo, 0, vertice_inicio, [])]

    while fila_prioridade:
      prioridade, custo_atual, vertice_atual, caminho_atual = heapq.heappop(fila_prioridade)

      if vertice_atual == self.objetivo:
        self.encontrado = True
        return caminho_atual + [vertice_atual]

      if vertice_atual.visitado:
        continue

      vertice_atual.visitado = True
      print(f'Vértice atual = {vertice_atual.rotulo}')

      for adj in vertice_atual.adjacentes:
        vizinho = adj.vertice_destino
        custo = adj.custo
        novo_custo = custo_atual + custo
        prioridade_vizinho = novo_custo + vizinho.distancia_objetivo

        print(f'*** {vizinho.rotulo}: {prioridade_vizinho}')
        #self.imprimir_caminho(caminho_atual+[vertice_atual])

        heapq.heappush(fila_prioridade, (prioridade_vizinho, novo_custo, vizinho, caminho_atual+[vertice_atual] ))

    return None

  def zerar_busca(self):
    self.encontrado = False

  def imprimir_caminho(self,caminho):
    str = ''
    for c in caminho:
      str += f'{c.rotulo} -> '
    print(str[:-4])



