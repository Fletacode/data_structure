class Vertex:
    def __init__(self, data: int) -> None:
        self.data = data
        self.link: Vertex | None = None

    def __repr__(self):
        return f"{self.data:2d}"


class GraphUndirectedListAdj:

    def __init__(self, vertices: set[int]) -> None:
        self.len_verts = len(vertices)
        self.arr: list[Vertex] = [Vertex(v) for v in sorted(vertices)]

    def insert_edge(self, u: int, v: int) -> None:

        vertex = self.arr[u]
        while vertex and vertex.link:
            vertex = vertex.link
        vertex.link = Vertex(v)

        vertex = self.arr[v]
        while vertex and vertex.link:
            vertex = vertex.link
        vertex.link = Vertex(u)

    def delete_edge(self, u, v):

        prev = vertex = self.arr[u]

        while vertex and vertex.data != v:
            prev, vertex = vertex, vertex.link

        if not vertex:
            return
        prev.link = vertex.link

        prev = vertex = self.arr[v]

        while vertex and vertex.data != u:
            prev, vertex = vertex, vertex.link

        if not vertex:
            return

        prev.link = vertex.link

    def traverse(self, start_node: int) -> list[int]:
        visited = [False] * self.len_verts
        actions = []
        stack = [start_node]

        while stack:
            curr_node_data = stack.pop()

            if not visited[curr_node_data]:
                visited[curr_node_data] = True
                actions.append(curr_node_data)

                adj_nodes = []
                vertex = self.arr[curr_node_data].link
                while vertex:
                    adj_nodes.append(vertex.data)
                    vertex = vertex.link

                for adj_node in reversed(adj_nodes):
                    if not visited[adj_node]:
                        stack.append(adj_node)
        return actions

    def __repr__(self):
        temp_str = ""
        for vertice in self.arr:
            root = vertice.data
            temp_str += f"[ {root}]  "

            temp = []
            while vertice and vertice.link:
                if vertice.data != root:
                    temp.append(vertice.data)
                vertice = vertice.link
            temp.append(vertice.data)

            temp_str += str(temp)
            temp_str += "\n"

        return temp_str

    def total_edges(self):
        cnt = 0
        for vertice in self.arr:
            root = vertice.data

            while vertice and vertice.link:
                if vertice.data != root:
                    cnt += 1
                vertice = vertice.link
            cnt += 1

        return cnt // 2


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
    for u, v in sorted(edges):
        graph.insert_edge(u, v)
    print(f"graph:\n{graph}")

    print(f"graph.total_edges = {graph.total_edges()}")

    actions = graph.traverse(0)
    print(f"graph.traversal:\n{actions}")
