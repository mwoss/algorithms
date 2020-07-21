def find_leader(arr):
    stack_size = 0

    candidate = arr[0]
    for e in arr:
        if stack_size == 0:
            stack_size += 1
            candidate = e
        elif candidate != e:
            stack_size -= 1
        else:
            stack_size += 1

    if stack_size <= 0:
        return -1  # leader does not exist

    count = 0
    for e in arr:
        if e == candidate:
            count += 1

    if count > len(arr) // 2:
        return candidate

    return -1
