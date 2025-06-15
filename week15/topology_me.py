from collections import deque


class Vertex:
    def __init__(self, elem: int) -> None:
        self.elem = elem
        self.link: Vertex | None = None

    def __repr__(self) -> str:
        return f"{self.elem}"


class Head(Vertex):
    def __init__(self, id: int) -> None:
        super().__init__(id)
        self.indegree = 0

    def __repr__(self) -> str:
        return f"{self.elem}"


class GraphDirectedListAdj:

    def __init__(self, mat):
        self.arr = [Head(i) for i in range(len(mat))]
        print(self.arr)

        for idx, row in enumerate(mat):
            head = self.arr[idx]
            for j, val in enumerate(row):
                if val:
                    new_vertex = Vertex(j)
                    head.link = new_vertex
                    head = new_vertex
                    print(j)
                    self.arr[j].indegree += 1

    def __repr__(self):

        temp = ""

        for idx, head in enumerate(self.arr):
            temp += f"v[{idx}:{head.indegree}] = "
            vertex = head.link
            while vertex:
                temp += f"{vertex.elem}, "
                vertex = vertex.link
            temp = temp[:-2]
            temp += "\n"

        return temp

    def sort_topology(self):

        stack = []
        visited = [False for _ in range(len(self.arr))]
        path = deque()

        def go(now):
            vertex = self.arr[now].link
            visited[now] = True

            while vertex:
                if not visited[vertex.elem]:
                    stack.append(vertex.elem)
                    go(vertex.elem)
                vertex = vertex.link

            if stack:
                path.appendleft(stack.pop())

        for idx, head in enumerate(self.arr):
            if not visited[idx]:
                stack.append(head.elem)
                go(head.elem)

        return path


if __name__ == "__main__":
    mat = [
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    print("input matrix")
    print(mat)
    print()
    print("graph")
    graph = GraphDirectedListAdj(mat)
    print(graph)
    print()
    print("topology sort")
    topology = graph.sort_topology()
    print(topology)
