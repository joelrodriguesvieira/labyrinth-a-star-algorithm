import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def desenhar_labirinto(matriz, caminho=None):
    cores_rgb = {
        'S': [0.0, 1.0, 0.0],       # verde
        'E': [0.0, 0.0, 1.0],       # azul
        '.': [1.0, 1.0, 1.0],       # branco
        '?': [1.0, 0.65, 0.0],      # laranja
        '_': [0.0, 0.5, 0.0],       # verde escuro
        '#': [0.0, 0.0, 0.0]        # preto
    }

    linhas = len(matriz)
    colunas = len(matriz[0])
    imagem = np.zeros((linhas, colunas, 3))

    for i in range(linhas):
        for j in range(colunas):
            cor = cores_rgb.get(matriz[i][j], [0.5, 0.5, 0.5])
            imagem[i, j] = cor

    plt.imshow(imagem)

    if caminho:
        for (x, y) in caminho:
            plt.plot(y, x, 'ro', markersize=5)

    patches = [
        mpatches.Patch(color=cores_rgb['S'], label='Início (S)'),
        mpatches.Patch(color=cores_rgb['E'], label='Fim (E)'),
        mpatches.Patch(color=cores_rgb['.'], label='Livre (.)'),
        mpatches.Patch(color=cores_rgb['?'], label='Lama (?)'),
        mpatches.Patch(color=cores_rgb['_'], label='Floresta (_)'),
        mpatches.Patch(color=cores_rgb['#'], label='Muro (#)'),
        mpatches.Patch(color='red', label='Caminho')
    ]
    plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.title("Labirinto com Caminho A*")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# ----------- MAIN -----------

from Labirinto import Labirinto

matriz = [
    ["S", ".", ".", ".", "?", ".", ".", ".", "."],
    [".", "#", "#", "#", ".", "_", "_", "#", "."],
    [".", ".", "?", ".", ".", "_", ".", "#", "."],
    ["#", "#", ".", "#", ".", "_", ".", "#", "."],
    [".", ".", ".", "#", ".", "?", ".", ".", "."],
    [".", "#", ".", "#", "#", "?", "#", "#", "."],
    [".", "#", ".", ".", ".", ".", ".", "#", "."],
    [".", "#", "#", "#", "#", "#", ".", "#", "."],
    [".", ".", ".", "?", ".", ".", ".", ".", "E"]
]

lab = Labirinto(matriz)
caminho = lab.busca_a_estrela()

for linha in matriz:
    print(" ".join(linha))

if caminho:
    print("\nCaminho encontrado:")
    print(" -> ".join(str(p) for p in caminho))
else:
    print("\nNenhum caminho encontrado.")

desenhar_labirinto(matriz, caminho)
