class MagicSquare:
    def __init__(self, size):
        self.size = size
        self.mat = [[0] * size for _ in range(size)]

    def move_coexter(self, row, col, count):
        r = (row - 1)
        c = (col - 1)

        if (r < 0 and c < 0):
            r += 2
            c += 1
        elif (r < 0):
            r += self.size
        elif (c < 0):
            c += self.size
        elif (self.mat[r][c] != 0):
            r += 2
            c += 1

        return r, c

    def build(self):
        count = 1
        r, c = 0, self.size // 2

        while count <= self.size * self.size:
            self.mat[r][c] = count
            count += 1
            r, c = self.move_coexter(r, c, count)

    def __str__(self):
        return '\n'.join([' '.join([f'{num:2}' for num in row]) for row in self.mat])


def main():
    SIZE = 7
    ms = MagicSquare(SIZE)
    ms.build()
    print(ms)


if __name__ == '__main__':
    main()
