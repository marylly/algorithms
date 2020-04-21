def vertice_menor_custo(custos):
    menor_custo = float('inf')
    vertice_menor_custo = None
    custo = 0
    for vertice in custos:
        custo = custos[vertice]
        if custo < menor_custo and vertice not in processados:
            menor_custo = custo
            vertice_menor_custo = vertice
    return vertice_menor_custo

def menor_custo(custos):
    vertice = vertice_menor_custo(custos)
    custo = 0
    while vertice is not None:
        custo = custos[vertice]
        vizinhos = grafo[vertice]
        for vizinho in vizinhos.keys():
            novo_custo = custo + vizinhos[vizinho]
            if vizinho not in custos:
                custos[vizinho] = float('inf')

            if custos[vizinho] > novo_custo:
                custos[vizinho] = novo_custo
                if vertice in vertices_menor_custo: 
                    vertices_menor_custo.remove(vertice)

        processados.append(vertice)
        if vertice not in vertices_menor_custo and 'fim' not in vertices_menor_custo: 
            vertices_menor_custo.append(vertice)
        vertice = vertice_menor_custo(custos)
    return vertices_menor_custo, custos_iniciais['fim']

infinito = float('inf')
grafo = {}
grafo['inicio'] = {}
grafo['inicio']['a'] = 6
grafo['inicio']['b'] = 2

grafo['a'] = {}
grafo['a']['fim'] = 1

grafo['b'] = {}
grafo['b']['a'] = 3
grafo['b']['fim'] = 5

grafo['fim'] = {}

custos_iniciais = {}
custos_iniciais['a'] = 6
custos_iniciais['b'] = 2
custos_iniciais['fim'] = infinito

custos = []
processados = []
vertices_menor_custo = []

print("Grafo", grafo)
final = menor_custo(custos_iniciais)
print("Custos Finais", final)

print("----------------------------------------------------")

grafo = {}
grafo["inicio"] = {}
grafo["inicio"]["vertice1"] = 5
grafo["inicio"]["vertice2"] = 2

grafo["vertice1"] = {}
grafo["vertice1"]["vertice3"] = 4
grafo["vertice1"]["vertice4"] = 2

grafo["vertice2"] = {}
grafo["vertice2"]["vertice1"] = 8
grafo["vertice2"]["vertice4"] = 7

grafo["vertice3"] = {}
grafo["vertice3"]["vertice4"] = 6
grafo["vertice3"]["fim"] = 3

grafo["vertice4"] = {}
grafo["vertice4"]["fim"] = 1

grafo['fim'] = {}

custos_iniciais = {}
custos_iniciais['vertice1'] = 5
custos_iniciais['vertice2'] = 2
custos_iniciais['fim'] = infinito

custos = []
processados = []
vertices_menor_custo = []

print("Grafo", grafo)
final = menor_custo(custos_iniciais)
print("Custos Finais", final)
print("Caminho menor cursto", vertices_menor_custo)

print("----------------------------------------------------")

grafo = {}
grafo["inicio"] = {}
grafo["inicio"]["vertice1"] = 10

grafo["vertice1"] = {}
grafo["vertice1"]["vertice2"] = 20

grafo["vertice2"] = {}
grafo["vertice2"]["vertice3"] = 1
grafo["vertice2"]["fim"] = 30

grafo["vertice3"] = {}
grafo["vertice3"]["vertice1"] = 1

grafo['fim'] = {}

custos_iniciais = {}
custos_iniciais['vertice1'] = 10
custos_iniciais['fim'] = infinito

custos = []
processados = []
vertices_menor_custo = []

print("Grafo", grafo)
final = menor_custo(custos_iniciais)
print("Custos Finais", final)
print("Caminho menor cursto", vertices_menor_custo)