class GraphUndirectedMatAdj:
    def __init__(self, size):
        self.arr = [[0 for _ in range(size)] for _ in range(size)]
        self.size = size

    def insert_edge(self, st, end):
        self.arr[st][end] = 1
        self.arr[end][st] = 1

    def __repr__(self):
        output_lines = ["graph:"]
        for i in range(self.size):
            current_neighbors_reversed = []
            # Iterate j from size-1 down to 0 to get neighbors in reverse numerical order
            for j in range(self.size - 1, -1, -1):
                if self.arr[i][j] == 1:
                    current_neighbors_reversed.append(str(j))
            neighbors_str = ", ".join(current_neighbors_reversed)
            output_lines.append(f"[{i: >2}] {neighbors_str}")
        return "\\n".join(output_lines)

    def total_edges(self):
        cnt = 0
        for i in self.arr:
            for j in i:
                if j == 1:
                    cnt += 1

        return cnt // 2

    def degree(self, vertice):
        cnt = 0
        for i in self.arr[vertice]:
            if i == 1:
                cnt += 1
        return cnt

    def delete_edge(self, st, end):
        self.arr[st][end] = 0
        self.arr[end][st] = 0


if __name__ == "__main__":
    vertices: set[int] = {0, 1, 2, 3}
    edges: set[tuple[int, int]] = {
        (0, 1),
        (2, 0),
        (1, 2),
        (2, 3),
        (1, 3),
        (0, 3),
    }
    graph = GraphUndirectedMatAdj(len(vertices))

    for u, v in edges:
        print(f"graph.insert_edge({u}, {v})")
        graph.insert_edge(u, v)
    print()
    print(graph)
    print(f"total edge = {graph.total_edges()}")
    print(f"degree[0] = {graph.degree(0)}")
    print(f"degree[3] = {graph.degree(3)}")
    # union = SetUnion(graph)
    # print(f"is_connected(0, 3) = {union.is_connected(0, 3)}")
    # print()

    graph.delete_edge(0, 1)
    graph.delete_edge(0, 3)
    print(f"graph:\n{graph}")
    print(f"graph.total_edges = {graph.total_edges()}")
    print()
