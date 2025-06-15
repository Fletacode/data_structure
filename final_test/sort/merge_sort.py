def merge_arr(left_arr, right_arr):

    l_idx, r_idx = 0, 0
    ret = []

    while l_idx < len(left_arr) and r_idx < len(right_arr):
        if left_arr[l_idx] < right_arr[r_idx]:
            ret.append(left_arr[l_idx])
            l_idx += 1
        else:
            ret.append(right_arr[r_idx])
            r_idx += 1

    ret.extend(left_arr[l_idx:])
    ret.extend(right_arr[r_idx:])

    return ret


def merge_sort(arr):

    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    return merge_arr(left_arr, right_arr)


if __name__ == "__main__":
    data = [8, 4, 6, 9, 2, 3, 1]
    print(merge_sort(data))
