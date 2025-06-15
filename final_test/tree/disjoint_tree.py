# disjoint 트리 == 유니온 파인드


class SetUnion:

    def __init__(self, size):
        self.size = size
        self.parent = [-1] * size

    def find(self, a):
        if self.parent[a] < 0:
            return a
        else:
            self.parent[a] = self.find(self.parent[a])
            return self.parent[a]

    def union(self, a, b):

        find_a = self.find(a)
        find_b = self.find(b)

        if find_a > find_b:
            find_a, find_b = find_b, find_a

        self.parent[find_a] += self.parent[find_b]
        self.parent[find_b] = find_a


if __name__ == "__main__":

    SIZE = 10

    sets = SetUnion(SIZE)
    print(f"init = {sets.parent}")

    sets.union(0, 1)
    print(sets.parent, end="")
    print("find(1) = ", sets.find(1))

    sets.union(1, 2)
    print(sets.parent, end="")
    print("find(2) = ", sets.find(2))

    sets.union(3, 4)
    print(sets.parent, end="")
    print("find(4) = ", sets.find(4))

    sets.union(2, 4)
    print(sets.parent, end="")
    print("find(4) = ", sets.find(4))

    sets.find(4)
    print(sets.parent, end="")
    print("find(4) = ", sets.find(4))
