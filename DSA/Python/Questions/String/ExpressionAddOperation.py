"""
# Question: Expression Add Operators
# Link: https://leetcode.com/problems/expression-add-operators/

# Generate all possible expressions that evaluate to target

# Time Complexity: O(4^n)
# Space Complexity: O(n)

# Algorithm:
# 1. Use backtracking to generate expressions
# 2. Handle multiplication precedence
# 3. Track evaluation results
# 4. Avoid leading zeros

# Key Components:
# - add_operators(): Main implementation
# - helper(): Recursive backtracking
# - Expression evaluation tracking
"""


class ExpressionAddOperation:
    def add_operators(self, num: str, target: int) -> list[str]:
        if not num:
            return []

        result = []
        self.helper(result, "", num, target, 0, 0, 0)
        return result

    def helper(
        self,
        result: list[str],
        path: str,
        num: str,
        target: int,
        pos: int,
        eval: int,
        multed: int,
    ) -> None:
        if pos == len(num):
            if target == eval:
                result.append(path)
            return

        for i in range(pos, len(num)):
            if i != pos and num[pos] == "0":
                break

            cur = int(num[pos : i + 1])

            if pos == 0:
                self.helper(result, path + str(cur), num, target, i + 1, cur, cur)
            else:
                self.helper(
                    result, path + "+" + str(cur), num, target, i + 1, eval + cur, cur
                )
                self.helper(
                    result, path + "-" + str(cur), num, target, i + 1, eval - cur, -cur
                )
                self.helper(
                    result,
                    path + "*" + str(cur),
                    num,
                    target,
                    i + 1,
                    eval - multed + multed * cur,
                    multed * cur,
                )


def main():
    solution = ExpressionAddOperation()
    num = "123"
    target = 6
    print(solution.add_operators(num, target))


if __name__ == "__main__":
    main()
