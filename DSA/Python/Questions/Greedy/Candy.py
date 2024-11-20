"""
# Question: Candy Distribution
# Link: https://leetcode.com/problems/candy/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Algorithm:
# 1. Initialize candy array with 1 candy each
# 2. Forward pass: compare with left neighbor
# 3. Backward pass: compare with right neighbor
# 4. Return total candies needed
"""


class Candy:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # Forward pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Backward pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


def main():
    solution = Candy()
    ratings = [1, 0, 2]
    print(solution.candy(ratings))  # Expected: 5


if __name__ == "__main__":
    main()
