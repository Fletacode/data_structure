class SetUnion:
    def __init__(self, size):
        self.size = size
        self.parent: list[int] = [i for i in range(size)]

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
            return self.parent[node]
        else:
            return node

    def union(self, n1: int, n2: int) -> None:

        find_a = self.find(n1)
        find_b = self.find(n2)

        if find_a != find_b:
            self.parent[find_b] = find_a 
        

if __name__ == "__main__":
    SIZE = 10
    # set0
    sets = SetUnion(SIZE)
    print(f"init = {sets.parent}")

    sets.union(0, 6)
    sets.union(0, 7)
    sets.union(0, 8)
    print(f"parent = {sets.parent}, find({8}) = {sets.find(8)}")

    sets.union(4, 1)
    sets.union(4, 9)
    print(f"parent = {sets.parent}, find({9}) = {sets.find(9)}")

        # S3
    sets.union(2, 3)
    sets.union(2, 5)
    print(f"parent = {sets.parent}, find({5}) = {sets.find(5)}")



    

