from collections import deque


class Edge:

    def __init__(self, v1: int | None = None, v2: int | None = None) -> None:
        self.v1 = v1
        self.v2 = v2
        self.link_v1: Edge | None = None
        self.link_v2: Edge | None = None

    def __repr__(self):
        return f"({self.v1}, {self.v2})"


class GraphUndirectedListAdjMultiple:

    def __init__(self, vertices):
        self.arr = [None] * len(vertices)
        self.vertices = vertices

    def insert_edge(self, u, v):

        edge = Edge(u, v)

        edge.link_v1 = self.arr[u]
        self.arr[u] = edge

        edge.link_v2 = self.arr[v]
        self.arr[v] = edge

    def exploer(self, st):

        now = self.arr[st]
        trace = []

        while now:
            trace.append(now)
            if now.v1 == st:
                now = now.link_v1
            elif now.v2 == st:
                now = now.link_v2

        return reversed(trace)

    def traverse(self, st: int) -> list[Edge]:

        ans: list[int] = []
        visited = [0 for _ in range(len(self.arr))]
        visited[st] = True
        dq = deque()
        dq.appendleft(st)

        while len(dq) != 0:
            now_val = dq.popleft()
            ans.append(now_val)

            temp: list[int] = []

            node = self.arr[now_val]
            while node:
                if node.v1 == now_val:
                    temp.append(node.v2)
                    node = node.link_v1
                elif node.v2 == now_val:
                    temp.append(node.v1)
                    node = node.link_v2
                else:
                    break

            for i in sorted(temp):
                if not visited[i]:
                    visited[i] = True
                    dq.append(i)

        print(ans)

        return ans


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

    graph = GraphUndirectedListAdjMultiple(vertices)
    for u, v in sorted(edges):
        print(f"graph.insert_edge({u}, {v})")
        graph.insert_edge(u, v)
    print()
    print(f"graph:")

    for i in sorted(vertices):
        trace = graph.exploer(i)
        print(f"vertex[{i}]: path = [" + ", ".join(str(edge) for edge in trace) + "]")

    actions = graph.traverse(0)
    print(f"actions = [" + ", ".join(str(i) for i in actions) + "]")
