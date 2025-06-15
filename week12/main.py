from collections import deque


class WinnerTree:
    def __init__(self, runs: list[deque[float]]) -> None:
        self.runs = runs
        self.size_runs = len(runs)
        self.tree: list[int | None] = [None] * (2 * self.size_runs)

        for i in range(self.size_runs):
            self.tree[self.size_runs + i] = i

        for i in range(self.size_runs - 1, 0, -1):
            left_idx = self.tree[i * 2]
            right_idx = self.tree[i * 2 + 1]
            win_idx = self.winner(left_idx, right_idx)
            self.tree[i] = win_idx

        print("inital tree:", self.tree)

    def value(self, idx):

        if not self.runs[idx]:
            return 1e9

        return self.runs[idx][0]

    def winner(self, left_idx, right_idx):

        if left_idx is None or right_idx is None:
            return right_idx if left_idx is None else left_idx

        left_val = self.value(left_idx)
        right_val = self.value(right_idx)

        if left_val > right_val:
            return right_idx
        else:
            return left_idx

    def merge(self):

        min_idx = self.tree[1]

        if min_idx is None:
            return None

        min_val = self.value(min_idx)

        if min_val == 1e9:
            return None

        self.runs[min_idx].popleft()

        idx = self.size_runs + min_idx

        while idx > 1:
            parent_idx = idx // 2

            left_idx = self.tree[parent_idx * 2]
            right_idx = self.tree[parent_idx * 2 + 1]

            win_idx = self.winner(left_idx, right_idx)

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

    tree = WinnerTree(runs)

    merged = []

    while (now := tree.merge()) is not None:
        merged.append(now)

    print(merged)
