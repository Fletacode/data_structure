from collections import deque
import math


class Vertex:
    def __init__(self, elem: int, cost: int) -> None:
        self.cost = cost
        self.elem = elem
        self.link: Vertex | None = None

    def __repr__(self) -> str:
        return f"{self.elem, self.cost}"


class GraphDirectedListAdj:

    def __init__(self, mat):
        self.arr = [Vertex(i, 0) for i in range(len(mat))]

        for i, li in enumerate(mat):
            for j, val in enumerate(li):
                if val != 0:
                    new_vertex = Vertex(j, val)
                    new_vertex.link = self.arr[i].link
                    self.arr[i].link = new_vertex

    def __repr__(self):
        temp = ""
        for idx, vertex in enumerate(self.arr):

            temp += f"v[{idx}] "
            vertex = vertex.link
            while vertex:
                temp += f"({vertex.elem}, {vertex.cost}), "
                vertex = vertex.link
            temp = temp[:-2]
            temp += "\n"

        return temp

    def dijkstra(self, st):
        visited = [math.inf for _ in range(len(self.arr))]
        visited_detail = [
            (math.inf, None) for _ in range(len(self.arr))
        ]  # cost, before vertex
        q = deque()
        visited[st] = 0
        visited_detail[st] = (0, None)
        q.append(self.arr[st])

        cnt = 0

        print(f"{cnt}   {str(visited)}")

        while q:
            now = q.popleft()

            next = now.link
            while next:
                if visited[now.elem] + next.cost < visited[next.elem]:
                    visited[next.elem] = visited[now.elem] + next.cost
                    visited_detail[next.elem] = (visited[next.elem], now.elem)
                    q.append(self.arr[next.elem])

                next = next.link

            # print info_table
            print(f"{cnt}   {str(visited)}   {str(visited_detail)}")

        def print_path(now_idx):
            if visited_detail[now_idx][1] is not None:
                print_path(visited_detail[now_idx][1])
            print(now_idx, end=", ")

        # print path table
        print("path-table")
        print("from to path")
        for i in range(1, len(self.arr)):
            print(f"{st} {i}", end=" ")
            print_path(i)
            print()


if __name__ == "__main__":

    mat = [
        [0, 10, 3, 0, 0],
        [0, 0, 1, 2, 0],
        [0, 4, 0, 8, 2],
        [0, 0, 0, 0, 7],
        [0, 0, 0, 9, 0],
    ]
    print("input matrix")
    for i in mat:
        for j in i:
            print(j, end=" ")
        print()

    print()
    print("graph")
    graph = GraphDirectedListAdj(mat)
    print(graph)
    print()
    # v = 0
    # print("info-table:")
    graph.dijkstra(0)
    # print()
    # print("path-table:")
    # print_paths(v, dist, info)
