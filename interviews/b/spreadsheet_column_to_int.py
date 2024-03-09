"""
Having a string column representation ("A", "B", ... "AZ", ...) map it to its corresponding integer representation.
For example: A -> 0, B -> 1, C -> 2, Z -> 25, AA -> 26, ZA -> 676.

TBH It's just a base-26 numerical system.
"""


def column_to_int(column_repr: str) -> int:
    integer_repr, factor = 0, 1

    for char in reversed(column_repr):
        single_col_repr = (ord(char) - 64) * factor
        integer_repr += single_col_repr
        factor *= 26

    return integer_repr - 1


if __name__ == '__main__':
    print(column_to_int("A"))
    print(column_to_int("B"))
    print(column_to_int("Z"))
    print(column_to_int("AA"))
    print(column_to_int("AZ"))
    print(column_to_int("ZA"))
    print(column_to_int("ZZZ"))
