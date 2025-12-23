class Vertice:
  def __init__(self, rotulo, distancia_objetivo):
    self.rotulo = rotulo
    self.distancia_objetivo = distancia_objetivo
    self.visitado = False
    self.adjacentes = []

  def adiciona_adjacente(self, adj):
    self.adjacentes.append(adj)

  def imprimir_adjacentes(self):
    print(f'{self.rotulo}')
    if len(self.adjacentes) > 0:
      for adj in self.adjacentes:
        print(f'-> {adj.vertice_destino.rotulo} (custo: {adj.custo}), dist_obj:{adj.vertice_destino.distancia_objetivo}, dist_astar:{adj.distancia_aestrela}')