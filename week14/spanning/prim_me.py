from collections import deque


class Vertex:

    def __init__(self, data: int, w: int) -> None:
        self.data = data
        self.link: Vertex | None = None
        self.w = w

    def __repr__(self) -> str:
        return f"{self.data}"


class Edge:

    def __init__(self, u: Vertex, v: Vertex, w: int) -> None:
        self.u = u
        self.v = v
        self.w = w

    def __repr__(self) -> str:
        return f"{self.u, self.v, self.w}"


class TreeBinaryHeapMin:
    def __init__(self) -> None:
        self.arr: deque[Edge] = deque()

    def parent(self, pos) -> int:
        return (pos - 1) // 2

    def left(self, pos) -> int:
        return pos * 2 + 1

    def right(self, pos) -> int:
        return pos * 2 + 2

    def bubble_up(self):
        now = len(self.arr) - 1
        root = self.parent(now)

        while root > -1 and self.arr[now].w < self.arr[root].w:
            self.arr[now], self.arr[root] = self.arr[root], self.arr[now]
            now = root
            root = self.parent(now)

    def bubble_down(self):
        now = 0
        size = len(self.arr)

        while True:
            _left = self.left(now)
            _right = self.right(now)
            smallest = now

            if _left < size and self.arr[smallest].w > self.arr[_left].w:
                smallest = _left

            if _right < size and self.arr[smallest].w > self.arr[_right].w:
                smallest = _right

            if smallest == now:
                break

            self.arr[now], self.arr[smallest] = self.arr[smallest], self.arr[now]
            now = smallest

    def insert(self, edge: Edge) -> int:

        self.arr.append(edge)
        self.bubble_up()

    def delete(self) -> Edge:

        if len(self.arr) == 0:
            return 0

        if len(self.arr) == 1:
            return self.arr.pop()

        delete_node = self.arr.popleft()
        self.arr.appendleft(self.arr.pop())
        self.bubble_down()
        return delete_node

    def __repr__(self):
        return str(self.arr)

    def empty(self) -> bool:
        if len(self.arr) == 0:
            return True
        return False


class GraphUndirectedListAdj:

    def __init__(self, vertice: set[int]):
        self.arr = [Vertex(i, 0) for i in sorted(vertice)]
        self.edge_arr: list[tuple[int, int, int]] = []
        self.pq = TreeBinaryHeapMin()

    def insert_edge(self, u: int, v: int, w: int):

        new_v = Vertex(v, w)
        new_v.link = self.arr[u].link
        self.arr[u].link = new_v

        new_u = Vertex(u, w)
        new_u.link = self.arr[v].link
        self.arr[v].link = new_u

        self.edge_arr.append(Edge(u, v, w))

    def __repr__(self):

        ret = ""

        for idx, item in enumerate(self.arr):
            ret += f"v[{idx}] = "
            item = item.link
            temp_arr = []
            while item:
                temp_arr.append((item.data, item.w))
                item = item.link

            ret += ", ".join(str(i) for i in sorted(temp_arr))
            ret += "\n"

        return ret

    def prim(self, st):
        total = 0
        path = []
        visited = [False for _ in range(len(self.arr))]

        st_node = self.arr[st]
        self.pq.insert(Edge(st_node, st_node, st_node.w))

        while not self.pq.empty():
            edge_now = self.pq.delete()
            now = self.arr[edge_now.v.data]

            if visited[now.data]:
                continue

            path.append(edge_now)
            total += edge_now.w
            visited[now.data] = True

            node = now.link
            while node:
                if not visited[node.data]:
                    self.pq.insert(Edge(now, node, node.w))
                node = node.link

        path.pop(0)
        return path, total


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

    path, total = graph.prim(0)

    print("MST Prim's algorithm")
    for idx, edge in enumerate(path):
        print(f"{idx}: {edge}")

    print(f"total cost = {total}")
