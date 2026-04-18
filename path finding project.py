import heapq
from collections import deque

# Sample graph (weighted)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1}
}

# ---------------- BFS ----------------
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print("BFS Traversal:")
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node].keys())
    print("\n")


# ---------------- Dijkstra ----------------
def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    print("Dijkstra Shortest Distances:")
    for node, dist in distances.items():
        print(f"{start} -> {node} = {dist}")


# Run
bfs(graph, 'A')
dijkstra(graph, 'A')