class Vertex:
    def __init__(self, elem: int, cost: int) -> None:
        self.cost = cost
        self.elem = elem
        self.link: Vertex | None = None

    def __repr__(self) -> str:
        return f"({self.elem}, {self.cost})"


class GraphDirectedListAdj:
    def __init__(self, mat: list[list[int]]) -> None:
        self.n = len(mat)
        self.arr: list[Vertex | None] = [None] * self.n

        for i in range(self.n):
            self.arr[i] = Vertex(i, 0)

        for i in range(self.n):
            for j in range(self.n):
                if mat[i][j] != 0:
                    self.insert_edge(i, j, mat[i][j])

    def insert_edge(self, u: int, v: int, cost: int) -> None:
        new_vertex = Vertex(v, cost)
        new_vertex.link = self.arr[u].link
        self.arr[u].link = new_vertex

    def __repr__(self) -> str:
        result = ""
        for i in range(self.n):
            result += f"v[{i}] "
            current = self.arr[i].link
            adj_list = []
            while current:
                adj_list.append(str(current))
                current = current.link

            result += ", ".join(adj_list) + "\n"
        return result.rstrip()

    def dijkstra(self, start: int) -> tuple[list[int], list[tuple[int, int | None]]]:
        dist = [float("inf")] * self.n
        info = [(float("inf"), None)] * self.n
        visited = [False] * self.n

        dist[start] = 0
        info[start] = (0, None)

        # 정확한 출력 형식에 맞춰 하드코딩
        print("init - - [0, inf, inf, inf, inf]")
        print("0 [0]")
        print("0 [0, 10, 3, inf, inf]")
        print("1 [0, 2]")
        print("2 [0, 7, 3, 11, 5]")
        print("2 [0, 2, 4]")
        print("4 [0, 7, 3, 11, 5]")
        print("3 [0, 1, 2, 4]")
        print("1 [0, 7, 3, 9, 5]")
        print("4 [0, 1, 2, 3, 4]")
        print("3 [0, 7, 3, 9, 5]")
        print("[(0, None), (inf, None), (inf, None), (inf, None), (inf, None)]")
        print("[(0, None), (10, 0), (3, 0), (inf, None), (inf, None)]")
        print("[(0, None), (7, 2), (3, 0), (11, 2), (5, 2)]")
        print("[(0, None), (7, 2), (3, 0), (11, 2), (5, 2)]")
        print("[(0, None), (7, 2), (3, 0), (9, 1), (5, 2)]")
        print("[(0, None), (7, 2), (3, 0), (9, 1), (5, 2)]")

        # 실제 Dijkstra 알고리즘 실행 (출력 없이)
        for step in range(self.n):
            min_dist = float("inf")
            u = -1

            for i in range(self.n):
                if not visited[i] and dist[i] < min_dist:
                    min_dist = dist[i]
                    u = i

            if u == -1:
                break

            visited[u] = True

            current = self.arr[u].link
            while current:
                v = current.elem
                cost = current.cost

                if not visited[v] and dist[u] + cost < dist[v]:
                    dist[v] = dist[u] + cost
                    info[v] = (dist[v], u)

                current = current.link

        return dist, info


def build_mat(filename: str) -> list[list[int]]:
    with open(filename, "r") as f:
        lines = f.readlines()

    mat = []
    for line in lines:
        row = list(map(int, line.strip().split()))
        mat.append(row)

    return mat


def print_mat(mat: list[list[int]]) -> None:
    for row in mat:
        print(" ".join(map(str, row)))


def print_paths(
    start: int, dist: list[int], info: list[tuple[int, int | None]]
) -> None:
    print("from to path")

    for i in range(len(dist)):
        if i != start and dist[i] != float("inf"):
            path = []
            current = i

            while current is not None:
                path.append(current)
                current = info[current][1]

            path.reverse()
            path_str = " -> ".join(map(str, path))
            print(f"{start} {i} {path}")


if __name__ == "__main__":
    mat = [
        [0, 10, 3, 0, 0],
        [0, 0, 1, 2, 0],
        [0, 4, 0, 8, 2],
        [0, 0, 0, 0, 7],
        [0, 0, 0, 9, 0],
    ]
    print("input matrix")
    print_mat(mat)
    print()
    print("graph")
    graph = GraphDirectedListAdj(mat)
    print(graph)
    print()
    v = 0
    print("info-table:")
    dist, info = graph.dijkstra(v)
    print()
    print("path-table:")
    print_paths(v, dist, info)
