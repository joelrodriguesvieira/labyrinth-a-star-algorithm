class BuscaAEstrela:

  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False

  def melhor_adj(self, vertice):
    if len(vertice.adjacentes) > 0:
      melhor_adjs = vertice.adjacentes[0]
      for adj in vertice.adjacentes:
        if adj.distancia_aestrela < melhor_adjs.distancia_aestrela:
          melhor_adjs = adj
      return melhor_adjs
    else:
      return None

  def busca_aestrela(self, vertice_origem):
    vertice_origem.visitado = True
    print(vertice_origem.rotulo) 

    if (vertice_origem == self.objetivo):
      print(f'Chegamos aos destino em {vertice_origem.rotulo}')
      self.encontrado = True
    else:
      vertice_origem.imprimir_adjacentes()
      melhor_adjacente = self.melhor_adj(vertice_origem)
      if melhor_adjacente != None and not self.encontrado:
        self.busca_aestrela(melhor_adjacente.vertice_destino)
