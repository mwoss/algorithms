def golden_max_slice(arr):
    max_ending = max_slice = 0
    for e in arr:
        max_ending = max(0, max_ending + e)
        max_slice = max(max_slice, max_ending)

    return max_slice


if __name__ == '__main__':
    print(golden_max_slice([5, -7, 3, 5, -2, 4, -1]))
