"""
# Question: Accounts Merge
# Link: https://leetcode.com/problems/accounts-merge/

# Time Complexity: O(NK * log(NK))
# Space Complexity: O(NK)

# Algorithm:
# 1. Use Disjoint Set Union (DSU)
# 2. Merge accounts with common emails
# 3. Group emails by account owner
"""

from collections import defaultdict


class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1


class AccountMerge:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)
        dsu = DisjointSet(n)
        email_to_acc = {}

        # Build email to account mapping and union accounts
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_acc:
                    dsu.union(i, email_to_acc[email])
                email_to_acc[email] = i

        # Group emails by account owner
        merged = defaultdict(set)
        for i in range(n):
            parent = dsu.find(i)
            merged[parent].update(accounts[i][1:])

        # Format result
        return [[accounts[i][0]] + sorted(list(emails)) for i, emails in merged.items()]


def main():
    solution = AccountMerge()
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    print(solution.accountsMerge(accounts))


if __name__ == "__main__":
    main()
