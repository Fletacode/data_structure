def insert_sort(data):

    for i in range(1, len(data)):
        key = data[i]
        j = i

        while j - 1 >= 0 and key < data[j - 1]:
            j -= 1
        data.pop(i)
        data.insert(j, key)

    return data


if __name__ == "__main__":

    data = [8, 4, 6, 9, 2, 3, 1]
    print(insert_sort(data))
