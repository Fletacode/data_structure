class SetUnion:
    def __init__(self, size):
        self.size = size
        self.parent: list[int] = [-1 for i in range(size)]

    def find(self, node: int) -> int:           

        if self.parent[node] >= 0:
            self.parent[node] = self.find(self.parent[node])
            return self.parent[node]
            #return self.find(self.parent[node])
        else:
            return node

    def union(self, n1: int, n2: int) -> None:

        find_a = self.find(n1)
        find_b = self.find(n2)

        if self.parent[find_a] <= self.parent[find_b]:
            self.parent[find_a] += self.parent[find_b]
            self.parent[find_b] = find_a
        else:
            self.parent[find_b] += self.parent[find_a]
            self.parent[find_a] = find_b
    

if __name__ == "__main__":
    SIZE = 10
sets = SetUnion(SIZE)
print(f"parent = [{' ,'.join(f'{x:2d}' for x in sets.parent)}]")

sets.union(0, 1)
print(
    f"parent = [{' ,'.join(f'{x:2d}' for x in sets.parent)}], "
    f"find({1}) = {sets.find(1)}"
)

sets.union(1, 2)
print(
    f"parent = [{' ,'.join(f'{x:2d}' for x in sets.parent)}], "
    f"find({2}) = {sets.find(2)}"
)

sets.union(3, 4)
print(
    f"parent = [{' ,'.join(f'{x:2d}' for x in sets.parent)}], "
    f"find({4}) = {sets.find(4)}"
)

sets.union(2, 4)
print(
    f"parent = [{' ,'.join(f'{x:2d}' for x in sets.parent)}], "
    f"find({4}) = {sets.find(4)}"
)

sets.find(4)
print(
    f"parent = [{' ,'.join(f'{x:2d}' for x in sets.parent)}], "
    f"find({4}) = {sets.find(4)}"
)

    

