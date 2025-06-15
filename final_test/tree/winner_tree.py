from collections import deque


class WinnerTree:

    def __init__(self, runs: list[deque[int]]):
        self.runs = runs
        self.run_size = len(runs)
        self.tree = [None] * (self.run_size * 2)

        for i in range(self.run_size):
            self.tree[self.run_size + i] = i

        for idx in range(self.run_size - 1, 0, -1):
            left = idx * 2
            right = idx * 2 + 1

            win_idx = self.winner(left, right)

            self.tree[idx] = win_idx

        print("inital_tree: ", self.tree)

    def value(self, idx):

        if not self.runs[idx]:
            return 1e9

        return self.runs[idx][0]

    def winner(self, idx1, idx2):

        idx1 = self.tree[idx1]
        idx2 = self.tree[idx2]

        val1 = self.value(idx1)
        val2 = self.value(idx2)

        if val1 < val2:
            return idx1
        else:
            return idx2

    def merge(self):

        min_idx = self.tree[1]
        min_val = self.value(min_idx)
        if min_val == 1e9:
            return None

        self.runs[min_idx].popleft()

        idx = min_idx + self.run_size

        while idx > 1:
            parent_idx = idx // 2

            left = parent_idx * 2
            right = parent_idx * 2 + 1

            win_idx = self.winner(left, right)

            self.tree[parent_idx] = win_idx

            idx = parent_idx

        return min_val


if __name__ == "__main__":
    runs: list[deque[float]] = [
        deque([10, 15, 16]),  # Run 0
        deque([9, 20, 38]),  # Run 1
        deque([20, 20, 30]),  # Run 2
        deque([6, 15, 25, 28]),  # Run 3
        deque([8, 15, 50]),  # Run 4
        deque([9, 11, 16]),  # Run 5
        deque([90, 95, 99]),  # Run 6
        deque([17, 18, 20]),  # Run 7
    ]

    merged = []

    tree = WinnerTree(runs)

    while (now := tree.merge()) is not None:
        merged.append(now)

    print(merged)
    print(runs)
