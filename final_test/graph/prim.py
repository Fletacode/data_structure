from collections import deque


class Vertex:
    def __init__(self, data, w=0):
        self.data = data
        self.w = w
        self.link = None

    def __repr__(self):
        return f"({self.data}, {self.w})"

    def __iter__(self):
        yield self.data
        yield self.w


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __lt__(self, other):
        return self.w < other.w


class MinHeap:
    def __init__(self):
        self.arr: Vertex = deque()

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

            parent_vertex = self.arr[parent_idx]
            vertex = self.arr[idx]

            if parent_vertex.w > vertex.w:
                self.arr[parent_idx], self.arr[idx] = (
                    self.arr[idx],
                    self.arr[parent_idx],
                )

            idx = parent_idx

    def bubble_down(self):

        idx = 0

        while idx < len(self.arr):
            left_idx = self.left(idx)
            right_idx = self.right(idx)
            min_idx = idx

            if left_idx < len(self.arr) and self.arr[left_idx].w < self.arr[min_idx].w:
                min_idx = left_idx
            if (
                right_idx < len(self.arr)
                and self.arr[right_idx].w < self.arr[min_idx].w
            ):
                min_idx = right_idx

            if min_idx == idx:
                break

            self.arr[min_idx], self.arr[idx] = self.arr[idx], self.arr[min_idx]

            idx = min_idx

    def insert(self, vertex):

        if not self.arr:
            self.arr.append(vertex)
            return

        self.arr.append(vertex)
        self.bubble_up()

    def delete(self):

        if not self.arr:
            return
        if len(self.arr) == 1:
            return self.arr.popleft()

        delete_vertex = self.arr.popleft()
        self.arr.appendleft(self.arr.pop())
        self.bubble_down()

        return delete_vertex

    def __repr__(self):
        return str(self.arr)


class GraphUndirectedListAdj:

    def __init__(self, vertices):
        self.arr = [Vertex(i) for i in range(len(vertices))]

    def insert(self, u, v, w):
        new_vertex = Vertex(v, w)
        vertex = self.arr[u]
        while vertex.link:
            vertex = vertex.link

        vertex.link = new_vertex

        new_vertex = Vertex(u, w)
        vertex = self.arr[v]
        while vertex.link:
            vertex = vertex.link

        vertex.link = new_vertex

    def __repr__(self):
        temp = ""

        for idx, vertex in enumerate(self.arr):
            temp += f"v[{idx}] = "
            temp_arr = []
            vertex = vertex.link
            while vertex:
                temp_arr.append(vertex)
                vertex = vertex.link
            print(temp_arr)
            temp += ", ".join(f"({data}, {w})" for data, w in temp_arr)
            temp += "\n"

        return temp

    def prim(self, st):

        q = MinHeap()
        visited = [False] * len(self.arr)
        actions = []

        q.insert(self.arr[st])

        while q.arr:

            now: Vertex = self.arr[q.delete().data]
            next = now.link

            if visited[now.data]:
                continue

            visited[now.data] = True
            actions.append(now.data)

            while next:
                if not visited[next.data]:
                    q.insert(next)
                next = next.link

        return actions


if __name__ == "__main__":
    vertices: set[int] = {0, 1, 2, 3, 4, 5, 6}
    edges: set[tuple[int, int, int]] = {
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
        graph.insert(u, v, w)

    print(f"graph:\n{graph}")

    actions = graph.prim(0)

    for idx, edge in enumerate(actions):
        print(f"{idx}: ({edge})")
