class Adjacente:
  def __init__(self, vertice_destino, custo):
    self.vertice_destino = vertice_destino
    self.custo = custo
    self.distancia_aestrela = vertice_destino.distancia_objetivo + custo