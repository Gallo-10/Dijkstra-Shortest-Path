import heapq

def dijkstra(grafo, inicio, objetivo):
    # Inicializar o dicionário de distâncias com um valor infinito para todas as cidades
    distancias = {cidade: float('inf') for cidade in grafo}
    distancias[inicio] = 0

    # Inicializar o dicionário de predecessores vazios para todas as cidades
    predecessores = {cidade: None for cidade in grafo}

    # Criar uma fila de prioridade para armazenar as cidades a serem exploradas
    fila_prioridade = [(0, inicio)]

    while fila_prioridade:
        # Obter a cidade com menor custo atual
        custo_atual, cidade_atual = heapq.heappop(fila_prioridade)

        # Verificar se alcançamos a cidade de destino
        if cidade_atual == objetivo:
            break

        # Verificar os vizinhos da cidade atual
        for vizinho, custo in grafo[cidade_atual].items():
            # Calcular o custo total até o vizinho através da cidade atual
            custo_total = custo_atual + custo

            # Atualizar a distância e o predecessor se o custo total for menor
            if custo_total < distancias[vizinho]:
                distancias[vizinho] = custo_total
                predecessores[vizinho] = cidade_atual

                # Adicionar o vizinho à fila de prioridade com o novo custo total
                heapq.heappush(fila_prioridade, (custo_total, vizinho))

    # Construir o caminho percorrido, começando pela cidade de destino e retrocedendo até a cidade de origem
    caminho = []
    cidade_atual = objetivo
    while cidade_atual:
        caminho.append(cidade_atual)
        cidade_atual = predecessores[cidade_atual]
    caminho.reverse()

    # Retornar o caminho percorrido e o custo total
    return caminho, distancias[objetivo]

grafo = {
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

origem = input("Digite a cidade de origem: ")
destino = input("Digite a cidade de destino: ")
print("O caminho mais curto é: ", dijkstra(grafo, origem, destino))