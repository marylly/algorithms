VERTICE_ORIGEM = 0
VERTICE_DESTINO = 1
PESO_ARESTA = 6
PESO_SEM_ARESTA = -1

def converte_inteiro(valor):
    return int(valor)

def valida_pesquisa(queries):
    if isinstance(queries, (int, complex, float)):
        queries = converte_inteiro(queries)
    else:
        raise ValueError("Informe um valor numérico inteiro para a quantidade de pesquisas")

    if queries < 1 or queries > 10:
        raise ValueError("Informe um valor numérico inteiro entre 1 e 10 para a quantidade de pesquisas")

    return queries

def define_pesquisa():
    print("Informe a quantidade de grafos a pesquisar:")
    queries = input()
    valida_pesquisa(queries)
    return queries

def recebe_entradas():
    entrada = {}
    entrada["queries"] = int(define_pesquisa())
    entrada['setup'] = []
    for query in range(1, entrada['queries'] + 1):
        estrutura = input("Informe a estrutura do grafo " + str(query) + " (Quantidade de Vértice <espaço> Quantidade de Arestas): ")
        grafo = estrutura.split(" ")
        entrada['setup'].append({"vertices": int(grafo[0])})
        entrada['setup'][query - 1]["arestas"] = []
        for aresta in range(1, int(grafo[1]) + 1):
            vertices = input("Informe a aresta " + str(aresta) + " do grafo " + str(query) + " (Vértice Origem <espaço> Vértice Destino): ")
            vertice_origem = int(vertices.split(" ")[0])
            vertice_destino = int(vertices.split(" ")[1])
            entrada['setup'][query - 1]["arestas"].append([vertice_origem, vertice_destino])
        print("")
    entrada['inicio'] = int(input("Informe o vértice de início da pesquisa: "))
    return entrada

def caminho_custo(entrada):
    for query in range(0, entrada['queries']):
        arestas = entrada['setup'][query]['arestas']
        qtd_vertices = entrada['setup'][query]['vertices']
        inicio = entrada['inicio']
        distancias = {}
        for vertice in range(1, qtd_vertices + 1):
            if vertice != inicio:
                custo = PESO_SEM_ARESTA
                for aresta in arestas:
                    if vertice == aresta[VERTICE_DESTINO]:
                        custo = PESO_ARESTA
                distancias[vertice] = custo
    return distancias

def imprime_caminhos(distancias):
    for distancia in distancias.values():
        print(distancia, end = " ")

entrada = recebe_entradas()
distancias = caminho_custo(entrada)
imprime_caminhos(distancias)