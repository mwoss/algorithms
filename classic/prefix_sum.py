def prefix_sum(arr):
    n = len(arr)
    res_arr = [0] * (n + 1)

    for i in range(1, n + 1):
        res_arr[i] = res_arr[i - 1] + arr[i - 1]

    return res_arr


def count_total(arr, x, y):
    return arr[y - 1] - arr[x]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    pref = prefix_sum(arr)

    print(f"Sum of the slice from 2nd to 4th elem is: ", count_total(pref, 2, 5))  # right hand side is exclusive
