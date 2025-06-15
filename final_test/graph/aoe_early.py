class Vertex:

    def __init__(self, elem, cost=0):
        self.elem = elem
        self.cost = cost
        self.link = None


class Head(Vertex):
    def __init__(self, id):
        super().__init__(id)
        self.indegree = 0


class GraphAoe:
    def __init__(self, mat):
        self.arr = [Head(i) for i in range(len(mat))]

        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if val != 0:
                    new_vertex = Vertex(j, val)
                    vertex = self.arr[i]

                    self.arr[j].indegree += 1

                    while vertex.link:
                        vertex = vertex.link
                    vertex.link = new_vertex

    def calculate_est(self):
        visited = [0] * len(self.arr)

        def go(now):
            stack = []
            stack.append(now)
            print(f"output {now}", visited, stack)

            while stack:
                head = self.arr[stack.pop()]
                vertex = head.link

                while vertex:
                    self.arr[vertex.elem].indegree -= 1
                    if self.arr[vertex.elem].indegree == 0:
                        stack.append(vertex.elem)
                    visited[vertex.elem] = max(
                        visited[vertex.elem], vertex.cost + visited[head.elem]
                    )
                    vertex = vertex.link
                print(f"output {head.elem}", visited, stack)

        for i in range(len(self.arr)):
            if visited[i] == 0 and self.arr[i].indegree == 0:
                go(i)


if __name__ == "__main__":
    mat = [
        [0, 6, 4, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    print("graph")
    graph = GraphAoe(mat)
    print("earliest start time table:")
    graph.calculate_est()
