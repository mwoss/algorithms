def binary_search(arr, x):
    beg, end = 0, len(arr) - 1
    result = -1

    while beg <= end:
        mid = (beg + end) // 2
        if arr[mid] <= x:
            beg = mid + 1
            result = mid
        else:
            end = mid - 1

    return result  # we are returning the index of element
