class Vertex:
    def __init__(self, data):
        self.data = data
        self.link = None

    def __repr__(self):
        return str(self.data)


class Head(Vertex):
    def __init__(self, id: int):
        super().__init__(id)
        self.indegree = 0


class GraphDirectedListAdj:
    def __init__(self, mat):
        self.arr = [Head(i) for i in range(len(mat))]

        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if val != 0:
                    new_vertex = Vertex(j)
                    vertex = self.arr[i]

                    self.arr[j].indegree += 1

                    while vertex.link:
                        vertex = vertex.link
                    vertex.link = new_vertex

    def sort_topology(self):

        actions = []
        visited = [False for _ in range(len(self.arr))]

        def go(now):
            nonlocal actions

            stack = []
            stack.append(now)

            while stack:

                actions.append(stack[-1])
                visited[stack[-1]] = True
                vertex = self.arr[stack.pop()]
                vertex = vertex.link

                while vertex:
                    self.arr[vertex.data].indegree -= 1
                    if self.arr[vertex.data].indegree == 0 and not visited[vertex.data]:
                        stack.append(vertex.data)
                    vertex = vertex.link

        for idx, head in enumerate(self.arr):
            if head.indegree == 0 and not visited[idx]:
                go(idx)

        print(actions)


if __name__ == "__main__":
    mat = [
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    graph = GraphDirectedListAdj(mat)

    graph.sort_topology()
