matching_parentheses = {
    "(": ")",
    "[": "]",
    "{": "}",
}


def is_valid(s: str) -> bool:
    stack = []

    for par in s:
        if par in matching_parentheses:
            stack.append(par)
        elif len(stack) != 0:
            match_par = stack.pop()
            if par != matching_parentheses[match_par]:
                return False

    return len(stack) == 0


def is_valid_2(s: str) -> bool:
    stack = []

    for par in s:
        if par in matching_parentheses:
            stack.append(matching_parentheses[par])
        elif len(stack) == 0 or stack.pop() != par:
            return False

    return len(stack) == 0


if __name__ == '__main__':
    print(is_valid("()"))
    print(is_valid("()[]{}"))
    print(is_valid("(]"))
    print(is_valid("]["))

    print(is_valid_2("()"))
    print(is_valid_2("()[]{}"))
    print(is_valid_2("(]"))
    print(is_valid_2("]["))
