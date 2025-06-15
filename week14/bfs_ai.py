import collections


class Edge:
    def __init__(self, v1: int | None = None, v2: int | None = None) -> None:
        self.v1 = v1
        self.v2 = v2
        self.link_v1: Edge | None = None
        self.link_v2: Edge | None = None

    def __repr__(self) -> str:
        return f"({self.v1}, {self.v2})"


class GraphUndirectedListAdjMultiple:
    def __init__(self, vertices_arg: set[int]) -> None:
        self.active_vertices: set[int] = vertices_arg
        self.arr_size = 0
        if self.active_vertices:
            self.arr_size = max(self.active_vertices) + 1
        self.arr: list[Edge | None] = [None] * self.arr_size

    def insert_edge(self, u: int, v: int) -> None:
        if not (u in self.active_vertices and v in self.active_vertices):
            print(
                f"Warning: Vertex {u} or {v} not in active_vertices. Edge ({u},{v}) not added."
            )
            return

        edge = Edge(u, v)

        edge.link_v1 = self.arr[u]
        self.arr[u] = edge

        edge.link_v2 = self.arr[v]
        self.arr[v] = edge

    def explore(self, vertex_val: int) -> list[Edge]:
        if not (vertex_val in self.active_vertices):
            return []

        collected_edges = []
        current_edge = self.arr[vertex_val]

        while current_edge:
            collected_edges.append(current_edge)

            if current_edge.v1 == vertex_val:
                current_edge = current_edge.link_v1
            elif current_edge.v2 == vertex_val:
                current_edge = current_edge.link_v2
            else:
                break

        return list(reversed(collected_edges))

    def traverse(self, start_node_val: int) -> list[int]:
        if not (start_node_val in self.active_vertices):
            return []

        q = collections.deque()
        visited_nodes_order: list[int] = []
        visited_flags: dict[int, bool] = {
            v_val: False for v_val in self.active_vertices
        }

        q.append(start_node_val)
        if (
            start_node_val in visited_flags
        ):  # Check if start_node_val is an active vertex
            visited_flags[start_node_val] = True
        else:  # Should not happen if initial check passes, but defensive
            return []

        while q:
            curr_node_val = q.popleft()
            if curr_node_val is None:
                continue

            visited_nodes_order.append(curr_node_val)

            neighbors_of_curr_node = []
            temp_edge = self.arr[curr_node_val]
            while temp_edge:
                other_v = None
                next_link_in_list = None

                if temp_edge.v1 == curr_node_val and temp_edge.v2 == curr_node_val:
                    other_v = temp_edge.v1
                    next_link_in_list = temp_edge.link_v1
                elif temp_edge.v1 == curr_node_val:
                    other_v = temp_edge.v2
                    next_link_in_list = temp_edge.link_v1
                elif temp_edge.v2 == curr_node_val:
                    other_v = temp_edge.v1
                    next_link_in_list = temp_edge.link_v2
                else:
                    break

                if other_v is not None and other_v in self.active_vertices:
                    neighbors_of_curr_node.append(other_v)
                temp_edge = next_link_in_list

            for neighbor in sorted(list(set(neighbors_of_curr_node))):
                if neighbor in visited_flags and not visited_flags[neighbor]:
                    visited_flags[neighbor] = True
                    q.append(neighbor)

        return visited_nodes_order


if __name__ == "__main__":
    vertices: set[int] = {0, 1, 2, 3, 4, 5, 6, 7}

    edges_to_insert_for_output: list[tuple[int, int]] = [
        (0, 1),
        (1, 3),
        (1, 4),
        (2, 0),
        (2, 5),
        (2, 6),
        (4, 7),
        (5, 7),
        (6, 7),
        (7, 3),
    ]

    graph = GraphUndirectedListAdjMultiple(vertices)

    for u, v in edges_to_insert_for_output:
        print(f"graph.insert_edge({u}, {v})")
        graph.insert_edge(u, v)
    print()
    print("graph:")

    for i in sorted(list(graph.active_vertices)):
        path_edges = graph.explore(i)
        path_str = "[" + ", ".join([str(edge_obj) for edge_obj in path_edges]) + "]"
        print(f"vertex[{i}]: path = {path_str}")

    print()
    actions = graph.traverse(0)
    print(f"actions = {actions}")
    print()
