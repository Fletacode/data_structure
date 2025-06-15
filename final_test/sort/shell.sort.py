def shell_sort(arr):

    gap = len(arr) // 2

    while gap > 0:

        for i in range(gap, len(arr)):
            key = arr[i]
            idx = i
            while idx - gap >= 0 and arr[idx - gap] > key:
                arr[idx] = arr[idx - gap]
                idx -= gap
            arr[idx] = key

        gap //= 2

    return arr


if __name__ == "__main__":

    data = [8, 4, 6, 9, 2, 3, 1]
    print(data)
    print(shell_sort(data))
