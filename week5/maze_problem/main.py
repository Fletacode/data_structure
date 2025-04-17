import copy
from typing import List, Optional, Tuple

import logging


class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.arr: List[Optional[int]] = [None] * capacity
        self.top = -1

    def __len__(self):
        return self.top + 1

    def empty(self) -> bool:
        if (self.top == -1):
            return True
        else:
            return False

    def full(self) -> bool:
        if (self.top == self.capacity - 1):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return str(self.arr[:self.top + 1])

    def push(self, num: Tuple[int, int]) -> None:
        if (self.full()):
            raise IndexError("push from full stack")
        self.top += 1
        self.arr[self.top] = num

    def peek(self) -> Optional[Tuple[int, int]]:
        if (self.empty()):
            raise IndexError("peek from empty stack")

        return self.arr[self.top]

    def pop(self) -> Optional[Tuple[int, int]]:
        if (self.empty()):
            raise IndexError("peek from empty stack")

        temp = self.arr[self.top]
        self.top -= 1
        return temp


class Maze:
    # N, NE, E, SE, S, SW, W, NW
    # dir_ = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    dir_ = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

    def __init__(self, map, ent, ext):
        self.maze = map
        self.ent = ent
        self.ext = ext
        self.rows, self.cols = len(self.maze), len(self.maze[0])
        self.stack = Stack(self.rows * self.cols)
        # 방문을 marking 하여 재방문을 피하기 위한 용도로 사용한다.
        self.mark = copy.deepcopy(self.maze)

    def __repr__(self):
        temp = f"Maze Problem: {self.ext[0]} x {self.ext[1]} \n"
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) == self.ent:
                    temp += "E "
                elif (i, j) == self.ext:
                    temp += "X "
                else:
                    temp += str(self.maze[i][j]) + " "
            temp += "\n"
        return temp

    def explore(self):
        stack = self.stack
        cnt = 0
        stack.push(self.ent)
        self.maze[self.ent[0]][self.ent[1]] = 1

        while not stack.empty():
            temp = stack.pop()
            self.mark[temp[0]][temp[1]] = cnt
            cnt += 1

            for (y, x) in Maze.dir_:
                my = temp[0] + y
                mx = temp[1] + x

                if my < 0 or my >= self.rows or mx < 0 or mx >= self.cols:
                    continue

                if self.mark[my][mx] != 0 or self.maze[my][mx] != 0:
                    continue

                stack.push((my, mx))
                self.maze[my][mx] = 1

                if (my, mx) == self.ext:
                    self.mark[my][mx] = cnt
                    return


def build_maze():
    grid = [
        ["E", 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
        [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, "X"],
    ]

    ent = ext = None
    rows = len(grid)
    cols = len(grid[0])
    for pos in range(rows * cols):
        row, col = pos // cols, pos % cols
        if grid[row][col] == "E":
            grid[row][col] = 0
            ent = row, col

        if grid[row][col] == "X":
            grid[row][col] = 0
            ext = row, col

    return grid, ent, ext


def print_maze(grid: List[List[int]]):
    for row in grid:
        for elem in row:
            print(elem, end=" ")
        print()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    map, ent, ext = build_maze()

    maze = Maze(map, ent, ext)
    print(maze)
    print(f"Entrance = {ent}, Exit = {ext}")
    maze.explore()
    print_maze(maze.mark)
