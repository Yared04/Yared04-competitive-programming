class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        calculations = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b}
        operators = [idx for idx, ch in enumerate(expression) if ch in "+-*"]

        def dfs(start, end,operators):
            if (start, end) in memo:
                return memo[(start, end)]

            if len(operators) == 0:
                return [int(expression[start: end])]

            res = []

            for idx, opr in enumerate(operators):
                left = dfs(start, opr,operators[:idx])
                right = dfs(opr + 1, end,operators[idx + 1:])

                for l in left:
                    for r in right:
                        res.append(calculations[expression[opr]](l, r))

            memo[(start, end)] = res
            return res

        return dfs(0, len(expression),operators)