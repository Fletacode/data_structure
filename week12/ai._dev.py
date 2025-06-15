from collections import deque
import math

class WinnerTree:
    def __init__(self, runs: list[deque[float]]) -> None:
        """
        Initializes the Winner Tree.

        Args:
            runs: A list of deques, where each deque represents a sorted run.
        """
        self.runs = runs
        self.size_runs = len(runs)
        # Use 1-based indexing for the tree for easier parent/child calculations.
        # Size is 2*n for n leaves.
        self.tree: list[int | None] = [None] * (2 * self.size_runs)

        # Initialize leaf nodes (indices size_runs to 2*size_runs - 1)
        # with the indices of the runs (0 to size_runs - 1).
        for i in range(self.size_runs):
            self.tree[self.size_runs + i] = i

        # Build the initial tree bottom-up
        # Start from the parent of the last leaf node and go up to the root (index 1)
        for i in range(self.size_runs - 1, 0, -1):
            left_child_idx = self.tree[2 * i]
            right_child_idx = self.tree[2 * i + 1]
            self.tree[i] = self.winner(left_child_idx, right_child_idx)
        
        print("tree:", self.tree)


    def value(self, run_idx: int) -> float:
        """
        Returns the current smallest value of the run at the given index.
        Returns infinity if the run is empty.

        Args:
            run_idx: The index of the run.

        Returns:
            The smallest value in the run, or float('inf') if the run is empty.
        """
        if run_idx is None or not self.runs[run_idx]:
            return float("inf")
        return self.runs[run_idx][0] # Peek at the front element


    def winner(self, left_run_idx: int | None, right_run_idx: int | None) -> int | None:
        """
        Compares the current smallest values of two runs and returns the index
        of the run with the smaller value (the winner).

        Args:
            left_run_idx: Index of the left run.
            right_run_idx: Index of the right run.

        Returns:
            The index of the winning run, or None if both are None.
        """
        if left_run_idx is None:
            return right_run_idx
        if right_run_idx is None:
            return left_run_idx

        left_val = self.value(left_run_idx)
        right_val = self.value(right_run_idx)

        # Return the index of the run with the smaller value
        if left_val <= right_val:
            return left_run_idx
        else:
            return right_run_idx


    def merge(self) -> float | None:
        """
        Extracts the smallest overall element from the runs using the winner tree,
        removes it from its run, and reconstructs the tree.

        Returns:
            The smallest element, or None if all runs are empty.
        """
        # The index of the winning run is at the root of the tree
        winner_run_idx = self.tree[1]

        if winner_run_idx is None: # Should not happen if initialized correctly unless runs is empty
             return None

        # Get the minimum value from the winning run
        min_val = self.value(winner_run_idx)

        # If min_val is infinity, all runs are exhausted
        if min_val == float("inf"):
            return None

        # Remove the minimum value from the winning run's deque
        self.runs[winner_run_idx].popleft()

        # Reconstruct the tree path from the leaf up to the root
        # Find the tree index corresponding to the winning run's leaf
        tree_idx = self.size_runs + winner_run_idx

        # Go up the tree, updating winners
        while tree_idx > 1:
            parent_idx = tree_idx // 2
            # Find the sibling index
            sibling_idx = tree_idx + 1 if tree_idx % 2 == 0 else tree_idx - 1

            # Get the run indices stored at the current node and its sibling in the tree
            # Note: These might have been updated in previous iterations if we came from that sibling
            # So we fetch the *stored* run indices from the tree nodes themselves
            left_child_node_idx = self.tree[parent_idx * 2]
            right_child_node_idx = self.tree[parent_idx * 2 + 1]

            # Determine the new winner for the parent node
            new_winner_idx = self.winner(left_child_node_idx, right_child_node_idx)

            # If the winner hasn't changed at this level, we still need to go further up
            # because the *value* of the winner might have changed, affecting higher levels.
            self.tree[parent_idx] = new_winner_idx
            tree_idx = parent_idx # Move up to the parent

        return min_val


if __name__ == "__main__":
    runs: list[deque[float]] = [
        deque([10, 15, 16]),      # Run 0
        deque([9, 20, 38]),       # Run 1
        deque([20, 20, 30]),      # Run 2
        deque([6, 15, 25, 28]),   # Run 3
        deque([8, 15, 50]),       # Run 4
        deque([9, 11, 16]),       # Run 5
        deque([90, 95, 99]),      # Run 6
        deque([17, 18, 20]),      # Run 7
    ]

    tree = WinnerTree(runs)

    merged = []
    while (val := tree.merge()) is not None:
        merged.append(val)

    # print(merged)
    #print(runs)
