from typing import Iterable


class Matrix(Iterable):
    def __init__(self, data):
        self.arr = data
    def __getitem__(self, row):
        return self.arr[row]
    def __iter__(self):
        return iter(self.arr)

    def __str__(self):
        rows = ["[" + " ".join(f"{val:3}" for val in row) + "]" for row in self.arr]
        return "\n".join(rows)

    def build_sparse(self):
        temp_arr = []
        for i,val in enumerate(self.arr):
            for j,item in enumerate(val):
                if (item != 0):
                    temp_arr.append((i, j, item))

        return temp_arr

    def restore(self,sparseMat):
        temp_arr = [[0 for _ in range(len(self.arr[0]))]  for _ in range(len(self.arr))]
        for item in sparseMat:
            temp_arr[item[0]][item[1]] = item[2]

        return Matrix(temp_arr)
    def transpose(self):
        temp_arr = [ [0 for _ in range(len(self.arr))] for _ in range(len(self.arr[0])) ]

        for (i,item) in enumerate(self.arr):
            for j,val in enumerate(self.arr[i]):
                temp_arr[j][i] = val
        return Matrix(temp_arr)
class MatrixSparse(Iterable):
    def __init__(self, sparse_matrix):
        self.sparse = sparse_matrix

    def __iter__(self):
        return iter(self.sparse)

    def fastTranspose(self):
        temp_sparse = [0 for _ in range(len(self.sparse))]
        col_size = 0

        for i, j, val in self.sparse:
            col_size = max(col_size , j + 1)

        col_arr = [0 for _ in range(col_size)]
        start_point = [0 for _ in range(col_size)]

        for (i, j, val) in self.sparse:
            col_arr[j] += 1

        for i in range(1,col_size):
            start_point[i] = start_point[i-1] + col_arr[i-1]

        # print("col_size", col_size)
        print("col_arr: ", col_arr)
        print("start_point: ", start_point)

        for (i, j, val) in self.sparse:
            col = j
            pos = start_point[col]
            temp_sparse[pos] = (j,i,val)
            start_point[col] += 1

        return temp_sparse

    def __str__(self):
        return str(self.sparse)



matrix = Matrix(
    [[0, 4, 5,0],
    [3, 8, 0,0],
    [0, 0,0, 6]])

print("init")
print(matrix)

sparseMat = MatrixSparse(matrix.build_sparse())
print(sparseMat)
print("sparse")
for idx,row in enumerate(sparseMat):
    print(idx,row)

print("restore")
print(matrix.restore(sparseMat))

print("transpose")
print(matrix.transpose())

print("fast_transpose")
for idx,row in enumerate(sparseMat.fastTranspose()):
    print(idx,row)
