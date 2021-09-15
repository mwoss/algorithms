def prison(n, m, h, v):
    # Write your code here
    h.sort()
    v.sort()

    max_horizontal_subsequence = find_longest_subsequence(h)
    max_vertical_subsequence = find_longest_subsequence(v)

    return max_horizontal_subsequence * max_vertical_subsequence


def find_longest_subsequence(arr):
    """
    Find longest continuous subsequence, where next element only differ by 1.
    Example: arr -> [1, 4, 5, 6, 9], returns: 3
    """
    max_subsequence = 1
    current_subsequence = 1
    previous_value = -1  # we know that such value does not exist there

    for element in arr:
        if element == previous_value + 1:
            current_subsequence += 1
        else:
            current_subsequence = 1

        if max_subsequence < current_subsequence:
            max_subsequence = current_subsequence

        previous_value = element

    return max_subsequence + 1


if __name__ == '__main__':
    print(prison(3, 2, [1, 2, 3], [1, 2]))
