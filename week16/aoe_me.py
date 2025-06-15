class Vertex:
    def __init__(self, elem: int = 0, duration: int = 0) -> None:
        self.elem = elem
        self.duration = duration
        self.link: Vertex | None = None

    def __repr__(self) -> str:
        return f"{self.elem, self.duration}"


class Head(Vertex):
    def __init__(self, id):
        super().__init__(id)
        self.indegree = 0

    def __repr__(self):
        return f"{self.elem}"


class GraphAoe:

    def __init__(self, mat):
        self.arr = [Head(i) for i in range(len(mat))]
        self.reverse_arr = [Head(i) for i in range(len(mat))]
        self.earliest = -1

        for i, row in enumerate(mat):
            head = self.arr[i]
            for j, val in enumerate(row):
                if val > 0:
                    new_vertex = Vertex(j, val)
                    head.link = new_vertex
                    head = new_vertex
                    self.arr[j].indegree += 1

        for i, row in enumerate(mat):
            for j, val in enumerate(row):

                if val > 0:

                    vertex = self.reverse_arr[j]

                    while vertex.link:
                        vertex = vertex.link

                    new_vertex = Vertex(i, val)
                    self.reverse_arr[i].indegree += 1
                    vertex.link = new_vertex

    def __repr__(self):

        ans = ""

        for i, head in enumerate(self.arr):
            ans += f"v[{i}: {head.indegree}] = "

            vertex = head.link
            while vertex:
                ans += str(vertex) + ", "
                vertex = vertex.link

            ans = ans[:-2]
            ans += "\n"

        return ans

    def print_reverse_arr(self):
        ans = ""

        for i, head in enumerate(self.reverse_arr):
            ans += f"v[{i}: {head.indegree}] = "

            vertex = head.link
            while vertex:
                ans += str(vertex) + ", "
                vertex = vertex.link

            ans = ans[:-2]
            ans += "\n"

        print(ans)

    # 작업을 가장 빨리 시작할 수 있는시간
    def calculate_est(self):
        stack = []
        path = [0 for _ in range(len(self.arr))]

        ans = ""
        stack.append(0)

        ans += str(path) + " : " + str(stack) + "\n"

        while stack:
            head = self.arr[stack.pop()]
            vertex = head.link

            while vertex:
                self.arr[vertex.elem].indegree -= 1
                path[vertex.elem] = max(
                    path[vertex.elem], vertex.duration + path[head.elem]
                )
                self.earliest = max(path[vertex.elem], self.earliest)

                if self.arr[vertex.elem].indegree == 0:
                    stack.append(vertex.elem)

                vertex = vertex.link
            ans += str(path) + ":" + str(stack) + "\n"

        return ans

    # 작업을 가장 여유롭게 시작할 수 있는 시간 (얼마까지 미룰 수 있음?)
    def calculate_lastest(self):
        # init
        path = [self.earliest for _ in range(len(self.arr))]

        stack = []

        stack.append(len(self.arr) - 1)

        print(f"{path} : {stack}")

        while stack:
            head = self.reverse_arr[stack.pop()]

            vertex = head.link

            while vertex:

                path[vertex.elem] = min(
                    path[vertex.elem], path[head.elem] - vertex.duration
                )
                self.reverse_arr[vertex.elem].indegree -= 1
                if self.reverse_arr[vertex.elem].indegree <= 0:
                    stack.append(vertex.elem)
                vertex = vertex.link

            print(f"{path} : {stack}")


if __name__ == "__main__":
    mat = matrix = [
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
    print("input matrix")
    print(mat)
    print()
    print("graph")
    graph = GraphAoe(mat)

    print("link list")
    print(graph)
    print()
    print("earliest")
    print(graph.calculate_est())

    print("reverse link list")
    graph.print_reverse_arr()
    print("lastest")
    graph.calculate_lastest()
