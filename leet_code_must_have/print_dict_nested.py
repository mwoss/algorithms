"""
Given the dictionary, for example:
{
    a: 1
    b: {
        c: 2
        d: 3
    }
}
Print the node in flat format like a: 1, b: c: 2, b: d: 3
"""


def print_dict_nested(d: dict, prefix: str = "") -> None:
    for key, val in d.items():
        if isinstance(val, dict):
            print_dict_nested(val, f"{prefix} {key}:")
        else:
            # print(f"{prefix} {key}: {val}", end=" ")
            print(f"{prefix} {key}: {val}")


if __name__ == '__main__':
    d1 = {"a": 1, "b": {"c": 2, "d": 3}}
    d2 = {"a": 1, "b": {"c": 2, "d": 3, "f": {"e": 4}}, "g": 5}
    print_dict_nested(d1)
    print_dict_nested(d2)
