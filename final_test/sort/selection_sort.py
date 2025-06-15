import math


def selection_sort(data):

    for i in range(len(data)):
        min_val = math.inf
        min_idx = -1
        for j in range(i, len(data)):
            if min_val > data[j]:
                min_val = data[j]
                min_idx = j

        data[i], data[min_idx] = data[min_idx], data[i]

    return data


if __name__ == "__main__":
    data = [8, 4, 6, 9, 2, 3, 1]
    print(selection_sort(data))
