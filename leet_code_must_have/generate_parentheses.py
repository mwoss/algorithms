"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
from typing import List


class Solution:
    def generate_parenthesis(self, n: int) -> List[str]:
        result = []
        combinations = "("
        self.helper(n, 1, 0, combinations, result)
        return result

    def helper(self, n: int, open_pars: int, close_pars: int, combinations: str, res: list):
        # if we want use n as stop condition we cannot modify it during the recursion call chain
        # that's why we are not touching it and compare len of combinations with "n"
        if len(combinations) == n * 2:
            res.append(combinations)
            return

        if open_pars < n:
            self.helper(n, open_pars + 1, close_pars, combinations + "(", res)
        if open_pars > close_pars:
            self.helper(n, open_pars, close_pars + 1, combinations + ")", res)


if __name__ == '__main__':
    s = Solution()
    print(s.generate_parenthesis(3))
