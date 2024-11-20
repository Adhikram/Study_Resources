"""
# Question: Multiply Strings
# Link: https://leetcode.com/problems/multiply-strings/

# Time Complexity: O(m * n)
# Space Complexity: O(m + n)

# Algorithm:
# 1. Process digits from right to left
# 2. Store intermediate results
# 3. Handle carry values
# 4. Build final result string

# Key Components:
# - multiply(): Main implementation
# - Digit-by-digit multiplication
# - Result array management
"""


class MultiplyStrings:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Multiply each digit
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                p1, p2 = i + j, i + j + 1
                total = mul + result[p2]

                result[p1] += total // 10
                result[p2] = total % 10

        # Build result string
        final = []
        i = 0
        while i < len(result) and result[i] == 0:
            i += 1

        while i < len(result):
            final.append(str(result[i]))
            i += 1

        return "".join(final) if final else "0"


def main():
    solution = MultiplyStrings()
    print(solution.multiply("123", "456"))  # Expected: "56088"


if __name__ == "__main__":
    main()
