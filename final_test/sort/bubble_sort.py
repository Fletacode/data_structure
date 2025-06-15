def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

    return arr


if __name__ == "__main__":
    data = [8, 4, 6, 9, 2, 3, 1]

    print(bubble_sort(data))
