"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
Note that division between two integers should truncate toward zero.
It is guaranteed that the given RPN expression is always valid.
That means the expression would always evaluate to a result, and there will not be any division by zero operation.
"""
from typing import List

from operator import add, truediv, mul, sub


class Solution:
    def eval_rpn(self, tokens: List[str]) -> int:
        operators = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": truediv

        }

        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                second, first = stack.pop(), stack.pop()
                op = operators[token]
                stack.append(int(op(first, second)))

        return stack.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.eval_rpn(["2", "1", "+", "3", "*"]))
    print(s.eval_rpn(["4", "13", "5", "/", "+"]))
    print(s.eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
