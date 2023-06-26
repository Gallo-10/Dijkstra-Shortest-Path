import networkx as nx
import random


random.seed(1)

# Busca de custo uniforme
def busca(grafo, origem, objetivo):
    # Define a origem
    vet = [origem]

    # Inicializa o vetor de explorado
    explorado = []

    # Custo dos caminhos
    custo = {origem: 0}

    # Caminho
    caminho = {origem: [origem]}

    # Loop principal
    while vet:
        # Retiro a primeira posição do vetor
        no = vet.pop(0)
        # Se o no não estiver no veto explorado
        if no not in explorado:
            # Se o no for o objetivo termina e retorna o caminho e o custo
            if no == objetivo:
                return caminho[no], custo[no]
            # Se ele não for o objetivo adiciono no vetor de explorado e expando a busca
            explorado.append(no)

            for vizinho in grafo[no]:
                # Se o custo não estiver no dicionário ainda, ou se precisar ser atualizado pq o novo caminho é menor
                if vizinho not in custo or custo[vizinho] > custo[no] + grafo[no][vizinho]:
                    custo[vizinho] = custo[no] + grafo[no][vizinho]
                    caminho[vizinho] = caminho[no] + [vizinho]
                    vet.append(vizinho)
                # Ordena o vetor pelo custo
                vet = sorted(vet, key=lambda x: custo[x])
    return False

grafo = {
    'No 0': {'No 28': 4, 'No 22': 10},
    'No 1': {},
    'No 2': {'No 24': {'jorge': 2}},
    'No 3': {'No 8': {'jorge': 6}, 'No 15': {'jorge': 1}},
    'No 4': {'No 18': {'jorge': 1}},
    'No 5': {},
    'No 6': {'No 25': {'jorge': 1}},
    'No 7': {},
    'No 8': {'No 3': {'jorge': 6}, 'No 14': {'jorge': 9}},
    'No 9': {}
}


# Criando um grafo aleatorio com 30 nos
G = nx.Graph()
for i in range(30):
    G.add_node("Equipamento " + str(i))

# Criando 70 arestas aleatorias
for i in range(70):
    G.add_edge("Equipamento " + str(random.randint(0, 29)), "Equipamento " + str(random.randint(0, 29)))

# Adicionando pesos
for i in G.edges():
    G[i[0]][i[1]]['weight'] = random.randint(1, 10)


# Transformando o grafo em um dicionario
dic = nx.to_dict_of_dicts(G)

for i in dic:
    for j in dic[i]:
        dic[i][j] = dic[i][j]['weight']

caminho, custo = busca(dic, 'Equipamento 0', 'Equipamento 4')
print("Caminho percorrido: ", caminho)
print("Custo: ", custo)