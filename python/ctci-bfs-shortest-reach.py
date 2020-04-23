# 1
#   6  4
#     1  2
#     1  5
#     2  3
#     3  4
# 1

# q = graph
# q[n m] = q[qtd de nós arestas]
# [n m] = [u v]
# [u v] = [nó origem  nó destino]
# s = vértice de início

# queries = 1 # q[1]
# qtd_vertices = 6 # q[2][1] n
# qtd_arestas = 4 # q[2][2] m
# arestas = []
# arestas.append([1, 2]) # q[3][1]
# arestas.append([1, 5]) # q[3][2]
# arestas.append([2, 3]) # q[3][3]
# arestas.append([3, 4]) # q[3][4]

queries = 1 # q[1]
qtd_vertices = 4 # q[2][1] n
qtd_arestas = 2 # q[2][2] m
arestas = []
arestas.append([1, 2]) # q[3][1]
arestas.append([1, 3]) # q[3][2]
inicio = 1

VERTICE_ORIGEM = 0
VERTICE_DESTINO = 1
PESO_ARESTA = 6
PESO_SEM_ARESTA = -1

def vertices_vizinhos(arestas, qtd_vertices):
    vizinhos = {}
    for vizinho in range(1, qtd_vertices):
        vizinhos[vizinho] = []

    for aresta in arestas:
        vizinhos[aresta[VERTICE_ORIGEM]].append(aresta[VERTICE_DESTINO])

    return vizinhos

def caminho_custo(arestas, qtd_vertices):
    distancias = {}

    for vertice in range(1, qtd_vertices + 1):
        if vertice != inicio:
            custo = PESO_SEM_ARESTA
            for aresta in arestas:
                if vertice == aresta[VERTICE_DESTINO]:
                    custo = PESO_ARESTA
            distancias[vertice] = custo

    return distancias

distancias = caminho_custo(arestas, qtd_vertices)

for distancia in distancias.values():
    print(distancia, end = " ")