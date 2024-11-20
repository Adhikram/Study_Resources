"""
# Question: Currency Exchange Groups
# Find groups of currencies that can be exchanged with each other

# Time Complexity: O(N * α(N)) for operations
# Space Complexity: O(N) for disjoint set storage

# Algorithm:
# 1. Use disjoint set to group currencies
# 2. Handle exchange rates
# 3. Track currency groups
"""


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.exchange_rate = [1.0] * n

    def find(self, x):
        if self.parent[x] != x:
            old_parent = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.exchange_rate[x] *= self.exchange_rate[old_parent]
        return self.parent[x]

    def union(self, x, y, rate):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
            rate = 1.0 / rate
        self.parent[py] = px
        self.exchange_rate[py] = rate * self.exchange_rate[x] / self.exchange_rate[y]
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1


class CurrencyExchange:
    def find_exchange_groups(
        self, n: int, exchanges: list[list[int]], rates: list[float]
    ) -> dict:
        dsu = DisjointSet(n)

        for (curr1, curr2), rate in zip(exchanges, rates):
            dsu.union(curr1, curr2, rate)

        groups = {}
        for i in range(n):
            parent = dsu.find(i)
            if parent not in groups:
                groups[parent] = []
            groups[parent].append((i, dsu.exchange_rate[i]))

        return groups


def main():
    solution = CurrencyExchange()
    exchanges = [[0, 1], [1, 2]]
    rates = [2.0, 3.0]
    print(solution.find_exchange_groups(3, exchanges, rates))


if __name__ == "__main__":
    main()
