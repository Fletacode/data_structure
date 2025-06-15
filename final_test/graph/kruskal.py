class Vertex:
    def __init__(self, data: int):
        self.data = data
        self.link = None

    def __repr__(self):
        return str(self.data)


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __repr__(self):
        return str((self.u, self.v, self.w))

    def __lt__(self, edge):
        return self.w < edge.w

    def __iter__(self):
        yield self.u
        yield self.v
        yield self.w


class GraphUndirectedListAdj:

    def __init__(self, vertices):
        self.arr = [Vertex(i) for i in vertices]
        self.edge_arr = []
        self.parent = [i for i in range(len(vertices))]

    def insert(self, u, v, w):

        edge = Edge(u, v, w)
        self.edge_arr.append(edge)

        vertex = self.arr[u]
        while vertex.link:
            vertex = vertex.link

        new_vertex = Vertex(v)

        vertex.link = new_vertex

        vertex = self.arr[v]
        while vertex.link:
            vertex = vertex.link

        new_vertex = Vertex(u)

        vertex.link = new_vertex

    def __repr__(self):
        temp = ""

        for idx, vertex in enumerate(self.arr):
            temp += f"v[{idx}] = "
            vertex = vertex.link
            temp_arr = []
            while vertex:
                temp_arr.append(vertex.data)
                vertex = vertex.link

            temp += ", ".join(str(i) for i in temp_arr)
            temp += "\n"

        return temp

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
            return self.parent[a]
        else:
            return a

    def union(self, a, b):

        find_a = self.find(a)
        find_b = self.find(b)

        self.parent[find_b] = find_a

    def is_same_parent(self, a, b):

        find_a = self.find(a)
        find_b = self.find(b)

        if find_a != find_b:
            return False
        else:
            return True

    def kruskal(self):

        actions = []
        total_cost = 0

        for u, v, w in sorted(self.edge_arr):

            if not self.is_same_parent(u, v):
                actions.append(Edge(u, v, w))
                self.union(u, v)
                total_cost += w

        for idx, edge in enumerate(actions):
            print(f"{idx}: {edge}")

        print(f"total cost = {total_cost}")


if __name__ == "__main__":
    vertices: set[int] = {0, 1, 2, 3, 4, 5, 6}
    edges: set[tuple[int, int, int]] = {
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
        graph.insert(u, v, w)
    print()
    print(f"graph:\n{graph}")
    graph.kruskal()
