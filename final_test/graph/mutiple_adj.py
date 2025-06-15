# edge 중심으로 연결리스트 만들고 bfs 구현하기 mutiple_adj

from collections import deque


class Edge:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.link1 = None
        self.link2 = None

    def __repr__(self):
        return str((self.n1, self.n2))


class GraphUndirectedListAdjMutiple:

    def __init__(self, vertices):
        self.vertice_size = len(vertices)
        self.arr = [None] * self.vertice_size

    def insert(self, u, v):

        edge = Edge(u, v)

        edge.link1 = self.arr[u]
        self.arr[u] = edge

        edge.link2 = self.arr[v]
        self.arr[v] = edge

    def explore(self, st):

        temp = f"vertex[{st}]: path = "
        temp_arr = []

        edge = self.arr[st]
        while edge:
            temp_arr.append(edge)
            if edge.n1 == st:
                edge = edge.link1
            elif edge.n2 == st:
                edge = edge.link2

        temp += ", ".join(str(i) for i in reversed(temp_arr))

        print(temp)

    def traverse(self, st):
        q = deque()
        visited = [False] * self.vertice_size
        actions = []

        q.append(st)
        visited[st] = True
        actions.append(st)

        while q:
            now = q.popleft()
            next = self.arr[now]

            temp = []

            while next:
                if next.n1 == now:
                    temp.append(next.n2)
                    next = next.link1
                elif next.n2 == now:
                    temp.append(next.n1)
                    next = next.link2

            for edge_idx in reversed(temp):
                if not visited[edge_idx]:
                    q.append(edge_idx)
                    visited[edge_idx] = True
                    actions.append(edge_idx)

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

    graph = GraphUndirectedListAdjMutiple(vertices)

    for u, v in sorted(edges):
        graph.insert(u, v)

    print("graph:")

    for i in range(len(vertices)):
        graph.explore(i)

    print(graph.traverse(0))
