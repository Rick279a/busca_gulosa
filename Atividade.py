import heapq

def busca_gulosa(grafo, inicio, objetivo, atracoes):
    visitados = set()
    fila_prioridade = [(0, inicio, [inicio])]
    while fila_prioridade:
        custo, no_atual, caminho = heapq.heappop(fila_prioridade)
        if no_atual == objetivo:
            return custo, caminho
        if no_atual not in visitados:
            visitados.add(no_atual)
            for vizinho, custo_vizinho in grafo[no_atual].items():
                if vizinho not in visitados:
                    heapq.heappush(fila_prioridade, (custo + custo_vizinho, vizinho, caminho + [vizinho]))  # Adiciona vizinhos à fila de prioridade
    return float('inf'), None

cidades = {
    'A': {'B': 10, 'C': 20, 'D': 15},
    'B': {'A': 10, 'C': 25, 'E': 30},
    'C': {'A': 20, 'B': 25, 'D': 35, 'E': 40},
    'D': {'A': 15, 'C': 35, 'E': 45},
    'E': {'A': 30, 'C': 40, 'D': 45}
}

atracoes = {
    'B': 'Clube Aquático',
    'C': 'Show da Turma de Mônica',
    'E': 'Apresentação de um Coral'
}

Inicio = 'A'
Objetivo = 'E'

custo_caminho_mais_curto, caminho = busca_gulosa(cidades, Inicio, Objetivo, atracoes)
if caminho:
    print("O custo do caminho mais curto de", Inicio, "para", Objetivo, "é:", custo_caminho_mais_curto)
    print("O caminho percorrido é:", ' -> '.join(caminho))
    print("Atrações ao longo do caminho:")
    for cidade in caminho:
        if cidade in atracoes:
            print(f"- Em {cidade}: {atracoes[cidade]}")

