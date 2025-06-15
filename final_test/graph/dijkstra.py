from collections import deque
import math


class Vertex:
    def __init__(self, data, cost):
        self.data = data
        self.link = None
        self.cost = cost


class MinHeap:

    def __init__(self):
        self.arr = deque()

    def left(self, idx):
        return idx * 2 + 1

    def right(self, idx):
        return idx * 2 + 2

    def parent(self, idx):
        return idx // 2

    def bubble_up(self):

        idx = len(self.arr) - 1

        while idx > 0:
            parent_idx = self.parent(idx)

            if self.arr[parent_idx].cost > self.arr[idx].cost:
                self.arr[parent_idx], self.arr[idx] = (
                    self.arr[idx],
                    self.arr[parent_idx],
                )
            idx = parent_idx

    def insert(self, data, cost):

        if not self.arr:
            self.arr.append(Vertex(data, cost))
            return

        self.arr.append(Vertex(data, cost))
        self.bubble_up()

    def bubble_down(self):

        idx = 0

        while idx < len(self.arr):

            left_idx = self.left(idx)
            right_idx = self.right(idx)
            min_idx = idx
            if (
                left_idx < len(self.arr)
                and self.arr[left_idx].cost < self.arr[min_idx].cost
            ):
                min_idx = left_idx

            if (
                right_idx < len(self.arr)
                and self.arr[right_idx].cost < self.arr[min_idx].cost
            ):
                min_idx = right_idx

            if min_idx == idx:
                break

            self.arr[idx], self.arr[min_idx] = (
                self.arr[min_idx],
                self.arr[idx],
            )

            idx = min_idx

    def delete(self) -> Vertex:

        if not self.arr:
            return None

        if len(self.arr) == 1:
            return self.arr.pop()

        delete_vertex = self.arr.popleft()
        self.arr.appendleft(self.arr.pop())

        self.bubble_down()

        return delete_vertex


class GraphdirecdListAdj:

    def __init__(self, mat):
        self.arr = [Vertex(i, 0) for i in range(len(mat))]

        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if val != 0:
                    new_vertex = Vertex(j, val)

                    vertex = self.arr[i]

                    while vertex.link:
                        vertex = vertex.link

                    vertex.link = new_vertex

    def __repr__(self):
        temp = ""

        for idx, vertex in enumerate(self.arr):
            temp += f"v[{idx}] "
            temp_arr = []
            vertex = vertex.link
            while vertex:
                temp_arr.append(vertex)
                vertex = vertex.link
            temp += ", ".join(f"({v.data}, {v.cost})" for v in temp_arr)
            temp += "\n"

        return temp

    def dijkstra(self, st):

        pq = MinHeap()
        visited = [math.inf for _ in range(len(self.arr))]
        path = []
        info = [(math.inf, None) for _ in range(len(self.arr))]

        info[st] = (st, None)
        pq.insert(st, 0)
        visited[st] = 0

        print(path, visited, info)

        while pq.arr:
            now: Vertex = self.arr[pq.delete().data]
            path.append(now.data)
            next = now.link

            while next:
                if visited[now.data] + next.cost < visited[next.data]:
                    visited[next.data] = visited[now.data] + next.cost
                    pq.insert(next.data, next.cost)
                    info[next.data] = (visited[next.data], now.data)

                next = next.link

            print(path, visited, info)

        return st, info

    def print_info(self, st, info):

        path = deque()

        def go(now):
            nonlocal path
            if now != st:
                path.appendleft(now)
                go(info[now][1])
            else:
                path.appendleft(now)
                return

        for i in range(len(self.arr)):
            if i == st:
                continue
            path = deque()
            go(i)
            print(f"{st} {i} {path}")


if __name__ == "__main__":

    mat = [
        [0, 10, 3, 0, 0],
        [0, 0, 1, 2, 0],
        [0, 4, 0, 8, 2],
        [0, 0, 0, 0, 7],
        [0, 0, 0, 9, 0],
    ]

    print("graph:")
    graph = GraphdirecdListAdj(mat)
    print(graph)

    st, info = graph.dijkstra(0)

    graph.print_info(st, info)
