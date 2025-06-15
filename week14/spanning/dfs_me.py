class Vertex:

    def __init__(self, data: int) -> None:
        self.data = data
        self.link: Vertex | None = None

    def __repr__(self) -> str:
        return f"{self.data}"


class Edge:

    def __init__(self, u: Vertex, v: Vertex) -> None:
        self.u = u
        self.v = v

    def __repr__(self) -> str:
        return f"{self.u, self.v}"


class GraphUndirectedListAdj:

    def __init__(self, vertice: set[int]):
        self.arr = [Vertex(i) for i in sorted(vertice)]

    def insert_edge(self, u: int, v: int):

        new_v = Vertex(v)
        new_v.link = self.arr[u].link
        self.arr[u].link = new_v

        new_u = Vertex(u)
        new_u.link = self.arr[v].link
        self.arr[v].link = new_u

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

    def dfs(self, st: int) -> list[Edge]:

        visited = [False for _ in range(len(self.arr))]
        actions: list[Edge] = []

        def go(now: int) -> None:
            visited[now] = True
            node = self.arr[now].link

            temp_arr = []

            while node:
                temp_arr.append(node)

                node = node.link

            temp_arr = list(reversed(temp_arr))

            for node in temp_arr:
                if not visited[node.data]:
                    actions.append(Edge(now, node.data))
                    go(node.data)

        go(st)
        return actions


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

    actions = graph.dfs(0)

    print("actions:")
    for idx, edge in enumerate(actions):
        print(f"[{idx}]: ", edge)
