class Vertex:
    def __init__(self, data: int) -> None:
        self.data = data
        self.link: Vertex | None = None

    def __repr__(self):
        return f"{self.data:2d}"


class GraphUndirectedListAdj:
    def __init__(self, vertices: set[int]):
        self.adj_list: dict[int, list[int]] = {vertex: [] for vertex in vertices}
        self.num_vertices = len(vertices)

    def insert_edge(self, u: int, v: int):
        if u in self.adj_list and v in self.adj_list:
            if v not in self.adj_list[u]:
                self.adj_list[u].append(v)
                self.adj_list[u].sort()
            if u not in self.adj_list[v]:
                self.adj_list[v].append(u)
                self.adj_list[v].sort()

    def delete_edge(self, u: int, v: int):
        if u in self.adj_list and v in self.adj_list:
            if v in self.adj_list[u]:
                self.adj_list[u].remove(v)
            if u in self.adj_list[v]:
                self.adj_list[v].remove(u)

    def total_edges(self) -> int:
        count = 0
        for vertex in self.adj_list:
            count += len(self.adj_list[vertex])
        return count // 2

    def __str__(self) -> str:
        result = []
        sorted_vertices = sorted(self.adj_list.keys())
        for vertex in sorted_vertices:
            adj_nodes = ", ".join(map(str, sorted(self.adj_list[vertex])))
            result.append(f"[ {vertex}] {adj_nodes}")
        return "\n".join(result)

    def traverse(self, start_vertex: int) -> list[int]:
        visited: set[int] = set()
        traversal_order: list[int] = []
        stack: list[int] = [start_vertex]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                traversal_order.append(vertex)
                for neighbor in reversed(self.adj_list[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return traversal_order


if __name__ == "__main__":
    vertices: set[int] = {0, 1, 2, 3, 4, 5, 6, 7}
    edges: set[tuple[int, int]] = {
        (0, 1),
        (2, 0),
        (2, 6),
        (1, 3),
        (1, 4),
        (2, 5),
        (7, 3),
        (4, 7),
        (5, 7),
        (6, 7),
    }
    graph = GraphUndirectedListAdj(vertices)
    for u, v in sorted(edges): # 간선을 정렬하여 삽입
        graph.insert_edge(u, v)
    
    print(f"graph:\n{graph}")
    print(f"graph.total_edges = {graph.total_edges()}")
    print()
    actions = graph.traverse(0)
    print(f"graph.traversal:\n{actions}")
