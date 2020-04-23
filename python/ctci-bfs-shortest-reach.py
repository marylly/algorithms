QTD_VERTICES = 0
QTD_ARESTAS = 1
VERTICE_ORIGEM = 0
VERTICE_DESTINO = 1
PESO_ARESTA = 6
PESO_SEM_ARESTA = -1

def maximo_qtd_arestas(qtd_vertices):
    return (qtd_vertices * (qtd_vertices - 1)) / 2

def valida_numero_inteiro(valor):
    return isinstance(valor, (int, complex, float))

def converte_inteiro(valor):
    try:
        valor = int(valor)
    except ValueError:
        print("Informe um valor numérico inteiro")
    return valor

def valida_pesquisa(queries):
    queries = converte_inteiro(queries)
    if not valida_numero_inteiro(queries):
        raise ValueError("Informe um valor numérico inteiro para a quantidade de pesquisas")

    if queries < 1 or queries > 10:
        raise ValueError("Informe um valor numérico inteiro entre 1 e 10 para a quantidade de pesquisas")

    return queries

def define_pesquisa():
    queries = input("Informe a quantidade de grafos a pesquisar: ")
    queries = valida_pesquisa(queries)
    return queries

def define_grafo_setup(queries):
    setup = []
    for query in range(1, queries + 1):
        estrutura = input("Informe a estrutura do grafo " + str(query) + " (Quantidade de Vértice <espaço> Quantidade de Arestas): ")
        grafo = estrutura.split(" ")
        setup.append({"vertices": int(grafo[QTD_VERTICES])})
        setup[query - 1]["arestas"] = []
        for aresta in range(1, int(grafo[QTD_ARESTAS]) + 1):
            setup[query - 1]["arestas"].append(define_aresta(aresta, query))
        print("")
        setup[query - 1]['inicio'] = define_inicio(setup[query - 1]['vertices'])
    return setup

def formata_vertices(vertices):
    vertices = vertices.split(" ")
    return [vertices[VERTICE_ORIGEM], vertices[VERTICE_DESTINO]]

def valida_aresta(vertices):
    vertices[VERTICE_ORIGEM] = converte_inteiro(vertices[VERTICE_ORIGEM])
    vertices[VERTICE_DESTINO] = converte_inteiro(vertices[VERTICE_DESTINO])

    if not valida_numero_inteiro(vertices[VERTICE_DESTINO]):
        raise ValueError("Informe um valor numérico inteiro para o vértice de origem da aresta")

    if not valida_numero_inteiro(vertices[VERTICE_DESTINO]):
        raise ValueError("Informe um valor numérico inteiro para o vértice de destino da aresta")

    return vertices

def define_aresta(aresta, query):
    vertices = input("Informe a aresta " + str(aresta) + " do grafo " + str(query) + " (Vértice Origem <espaço> Vértice Destino): ")
    aresta = valida_aresta(formata_vertices(vertices))
    return aresta

def valida_inicio(inicio, qtd_vertices):
    inicio = converte_inteiro(inicio)
    if not valida_numero_inteiro(inicio):
        raise ValueError("Informe um valor numérico inteiro para o vértice de início da pesquisa")

    if inicio < 1 or inicio > qtd_vertices:
        raise ValueError("Vértice informado inválido.")

    return inicio

def define_inicio(qtd_vertices):
    inicio = input("Informe o vértice de início da pesquisa: ")
    inicio = valida_inicio(inicio, qtd_vertices)
    return inicio

def recebe_entradas():
    entrada = {}
    entrada['queries'] = define_pesquisa()
    entrada['setup'] = define_grafo_setup(entrada['queries'])
    return entrada

def caminho_custo(entrada):
    for query in range(0, entrada['queries']):
        arestas = entrada['setup'][query]['arestas']
        qtd_vertices = entrada['setup'][query]['vertices']
        inicio = entrada['setup'][query]['inicio']
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