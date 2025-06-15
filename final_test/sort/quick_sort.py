def quick_sort(data):

    stack = []
    stack.append((0, len(data) - 1))

    while stack:
        st, end = stack.pop()

        if st >= end:
            continue

        left = st
        right = end

        pivot = data[left]

        while left <= end and pivot > data[left]:
            left += 1

        while right >= st and pivot < data[right]:
            right -= 1

        if left <= right:
            data[left], data[right] = data[right], data[left]
            left += 1
            right -= 1

        if left < end:
            stack.append((left, end))

        if st < right:
            stack.append((st, right))

    return data


if __name__ == "__main__":
    data = [8, 4, 6, 9, 2, 3, 1]
    print(data)
    print(quick_sort(data))
