class Vertex:
    def __init__(self, data: int) -> None:
        self.data = data
        self.link: Vertex | None = None

    def __repr__(self) -> str:
        return f"{self.data}"


class Edge:
    def __init__(self, u: Vertex, v: Vertex):
        self.u = u
        self.v = v

    def __repr__(self) -> str:
        return f"({self.u.data}, {self.v.data})"


class GraphUndirectedListAdj:

    def __init__(self, vertices: set[int]):
        max_vertex = max(vertices) if vertices else 0
        self.arr = [Vertex(i) for i in range(max_vertex + 1)]

    def insert_edge(self, u: int, v: int) -> None:
        # Add v to u's adjacency list
        new_vertex_u = Vertex(v)
        new_vertex_u.link = self.arr[u].link
        self.arr[u].link = new_vertex_u

        # Add u to v's adjacency list
        new_vertex_v = Vertex(u)
        new_vertex_v.link = self.arr[v].link
        self.arr[v].link = new_vertex_v

    def __repr__(self) -> str:
        result = ""
        for i, vertex in enumerate(self.arr):
            adj_list = []
            current = vertex.link
            while current:
                adj_list.append(current.data)
                current = current.link
            result += f"v[{i}] = " + ", ".join(map(str, adj_list)) + "\n"
        return result.rstrip()

    def dfs(self, start: int) -> list[Edge]:
        visited = [False] * len(self.arr)
        spanning_edges = []
        
        def dfs_recursive(vertex_data: int):
            visited[vertex_data] = True
            
            # Traverse adjacency list
            current = self.arr[vertex_data].link
            while current:
                neighbor = current.data
                if not visited[neighbor]:
                    # Add edge to spanning tree
                    spanning_edges.append(Edge(self.arr[vertex_data], self.arr[neighbor]))
                    dfs_recursive(neighbor)
                current = current.link
        
        dfs_recursive(start)
        return spanning_edges


if __name__ == "__main__":
    vertices: set[int] = {0, 1, 2, 3, 4, 5, 6, 7}
    edges: set[tuple[int, int]] = {
        (0, 1),
        (0, 2),
        (1, 3),
        (1, 4),
        (2, 5),
        (2, 6),
        (3, 7),
        (4, 7),
        (5, 7),
        (6, 7),
    }

    graph = GraphUndirectedListAdj(vertices)
    for u, v in sorted(edges):
        print(f"graph.insert_edge({u}, {v})")
        graph.insert_edge(u, v)

    print()
    print(f"graph:\n{graph}")
    
    actions = graph.dfs(0)  # using recursive fashion

    print("actions:")
    for n, edge in enumerate(actions):
        print(f"[{n}]: {edge}")
    
    
