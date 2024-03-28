import heapq

def greedy_search(graph, start, goal):
    visited = set()
    priority_queue = [(0, start)]  # Inicializa a fila de prioridade com o nó inicial e custo zero
    while priority_queue:
        cost, current_node = heapq.heappop(priority_queue)  # Remove o nó com o menor custo da fila
        if current_node == goal:
            return cost  # Retorna o custo acumulado se o objetivo for alcançado
        if current_node not in visited:
            visited.add(current_node)
            for neighbor, neighbor_cost in graph[current_node].items():
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + neighbor_cost, neighbor))  # Adiciona vizinhos à fila de prioridade
    return float('inf')  # Retorna infinito se o objetivo não for alcançado


graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'D': 2},
    'C': {'A': 3, 'D': 8},
    'D': {'B': 2, 'C': 8}
}

start_node = 'A'
goal_node = 'D'

shortest_path_cost = greedy_search(graph, start_node, goal_node)
print("O custo do caminho mais curto de", start_node, "para", goal_node, "é:", shortest_path_cost)