def partition(arr, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if arr[i] <= arr[begin]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]

    arr[pivot], arr[begin] = arr[begin], arr[pivot]
    return pivot


def quicksort(arr, begin, end):
    if begin >= end:
        return

    pivot = partition(arr, begin, end)
    quicksort(arr, begin, pivot - 1)
    quicksort(arr, pivot + 1, end)


if __name__ == '__main__':
    arr = [5, 2, 1, 5, 10, 8, -5]
    quicksort(arr, 0, len(arr) - 1)
    print(arr)
