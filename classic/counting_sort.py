def counting_sort(arr, k):  # k is the max value of the arr
    count = [0] * (k + 1)

    for e in arr:
        count[e] += 1

    result = []
    for i, e in enumerate(count):
        result += [i] * e

    return result


if __name__ == '__main__':
    arr = [5, 2, 1, 5, 10, 8, -5]
    arr = counting_sort(arr, 10)
    print(arr)