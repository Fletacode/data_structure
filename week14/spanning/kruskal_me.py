class Vertex:

    def __init__(self, data: int) -> None:
        self.data = data
        self.link: Vertex | None = None

    def __repr__(self) -> str:
        return f"{self.data}"


class Edge:

    def __init__(self, u: Vertex, v: Vertex, w: int) -> None:
        self.u = u
        self.v = v
        self.w = w

    def __repr__(self) -> str:
        return f"{self.u, self.v, self.w}"


class GraphUndirectedListAdj:

    def __init__(self, vertice: set[int]):
        self.arr = [Vertex(i) for i in sorted(vertice)]
        self.edge_arr: list[tuple[int, int, int]] = []
        self.parent = [i for i in range(len(vertice))]

    def find(self, a):

        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
            return self.parent[a]
        else:
            return a

    def union(self, a, b):

        find_a = self.find(a)
        find_b = self.find(b)

        if find_a != find_b:
            self.parent[find_b] = find_a

    def is_same_parent(self, u, v):

        find_a = self.find(u)
        find_b = self.find(v)

        if find_a != find_b:
            return False
        else:
            return True

    def insert_edge(self, u: int, v: int, w: int):

        new_v = Vertex(v)
        new_v.link = self.arr[u].link
        self.arr[u].link = new_v

        new_u = Vertex(u)
        new_u.link = self.arr[v].link
        self.arr[v].link = new_u

        self.edge_arr.append((w, u, v))

    def __repr__(self):

        ret = ""

        for idx, item in enumerate(self.arr):
            ret += f"v[{idx}] = "
            item = item.link
            temp_arr = []
            while item:
                temp_arr.append(item.data)
                item = item.link

            ret += ", ".join(str(i) for i in sorted(temp_arr))
            ret += "\n"

        return ret

    def kruskal(self):

        visited = [False for _ in self.arr]
        actions: list[Edge] = []
        cnt = 0

        for w, u, v in sorted(self.edge_arr):
            if not self.is_same_parent(u, v):
                self.union(u, v)
                visited[u] = True
                visited[v] = True
                actions.append(Edge(u, v, w))
                cnt += w

        return actions, cnt


if __name__ == "__main__":
    vertices: set[int] = {0, 1, 2, 3, 4, 5, 6}
    edges: set[tuple[int, int]] = {
        (0, 1, 28),
        (0, 5, 10),
        (1, 2, 16),
        (1, 6, 14),
        (2, 3, 12),
        (3, 6, 18),
        (3, 4, 22),
        (4, 5, 25),
        (4, 6, 24),
    }

    graph = GraphUndirectedListAdj(vertices)
    for u, v, w in sorted(edges):
        print(f"graph.insert_edge({u}, {v}, {w})")
        graph.insert_edge(u, v, w)
    print()

    print(f"graph:\n{graph}")
    actions, cnt = graph.kruskal()

    for idx, edge in enumerate(actions):
        print(f"{idx}: {edge}")
    print(f"total cost = {cnt}")
