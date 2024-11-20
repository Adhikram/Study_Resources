"""
# Question: Optimal Account Balancing
# Link: https://leetcode.com/problems/optimal-account-balancing/

# Find minimum number of transactions to settle all debts

# Time Complexity: O(2^n * N)
# Space Complexity: O(2^n)

# Algorithm:
# 1. Calculate net balance for each person
# 2. Use backtracking to try debt settlements
# 3. Track minimum transactions needed
# 4. Handle positive and negative balances

# Key Components:
# - min_transfers(): Main implementation
# - settle(): Recursive helper for debt settlement
# - Balance calculation and tracking
"""

from collections import defaultdict


class OptimalAccountBalancing:
    def min_transfers(self, transactions: list[list[int]]) -> int:
        # Calculate net balance for each person
        balance_map = defaultdict(int)
        for t in transactions:
            balance_map[t[0]] -= t[2]
            balance_map[t[1]] += t[2]

        # Create list of non-zero balances
        debt = [d for d in balance_map.values() if d != 0]

        def settle(start: int, debt: list) -> int:
            if start == len(debt):
                return 0

            curr = debt[start]
            if curr == 0:
                return settle(start + 1, debt)

            min_trans = float("inf")
            for i in range(start + 1, len(debt)):
                next_debt = debt[i]
                if curr * next_debt < 0:
                    debt[i] = curr + next_debt
                    min_trans = min(min_trans, 1 + settle(start + 1, debt))
                    debt[i] = next_debt

                    if curr + next_debt == 0:
                        break

            return min_trans

        return settle(0, debt)


def main():
    solution = OptimalAccountBalancing()
    print(solution.min_transfers([[0, 1, 10], [2, 0, 5]]))  # Expected: 2
    print(
        solution.min_transfers([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]])
    )  # Expected: 1


if __name__ == "__main__":
    main()
