class Vertice:

    def __init__(self, data):
        self.data = data
        self.right = None


class GraphUndriectedListAdj:

    def __init__(self, vertices):
        self.vertices = vertices
        self.arr = [Vertice(data) for data in vertices]
        self.size = 0

    def insert(self, u, v):
        self.size += 1

        new_vertice = Vertice(v)

        vertice = self.arr[u]

        while vertice.right:
            vertice = vertice.right

        vertice.right = new_vertice

        new_vertice = Vertice(u)

        vertice = self.arr[v]

        while vertice.right:
            vertice = vertice.right

        vertice.right = new_vertice

    def __repr__(self):

        temp = ""

        for idx, vertice in enumerate(self.arr):
            temp += f"[{idx}]  "
            vertice = vertice.right
            while vertice:
                temp += str(vertice.data) + ", "
                vertice = vertice.right
            temp = temp[:-2]
            temp += "\n"

        return temp

    def total_edges(self):
        return self.size

    def traverse(self, st: int):

        stack = []
        visited = [False for _ in range(len(self.arr))]
        actions = []

        stack.append(st)

        while stack:
            now = self.arr[stack.pop()]
            if visited[now.data]:
                continue
            actions.append(now.data)
            visited[now.data] = True

            temp = []
            now = now.right
            while now:
                temp.append(now.data)
                now = now.right

            for i in reversed(temp):
                stack.append(i)

        return actions


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

    graph = GraphUndriectedListAdj(vertices)
    for u, v in sorted(edges):
        graph.insert(u, v)
    print(f"graph:\n{graph}")

    print(f"graph.total_edges = {graph.total_edges()}")
    print()

    print("graph.traversal:\n")
    print(graph.traverse(0))
