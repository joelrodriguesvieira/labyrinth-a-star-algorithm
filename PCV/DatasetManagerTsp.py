import math

def load_tsp_file(filepath):
    with open(filepath, 'r') as f:
      lines = f.readlines()

    coords = []
    reading_nodes = False

    for line in lines:
        if line.startswith('NODE_COORD_SECTION'):
            reading_nodes = True
            continue
        if line.strip() == 'EOF':
            break
        if reading_nodes:
            parts = line.strip().split()
            if len(parts) >= 3:
                _, x, y = parts
                coords.append((float(x), float(y)))

    # calcula a matriz de distâncias
    num_cities = len(coords)
    distances = {}

    for i in range(num_cities):
        distances[i] = {}
        for j in range(num_cities):
            if i == j:
                distances[i][j] = 0
            else:
                xi, yi = coords[i]
                xj, yj = coords[j]
                dist = math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)
                distances[i][j] = dist

    return distances

if __name__ == "__main__":    
  cidades = load_tsp_file("st70.tsp")
  print(cidades)
  