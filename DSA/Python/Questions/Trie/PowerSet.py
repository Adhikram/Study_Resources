"""
# Question: Power Set
# Generate all possible subsets of a string

# Time Complexity: O(2^n * n)
# Space Complexity: O(1)

# Algorithm:
# 1. Use bit manipulation for subset generation
# 2. Generate all possible combinations
# 3. Track and sort subsets
# 4. Implement backtracking solution

# Key Components:
# - all_possible_strings(): Bit manipulation approach
# - solve_backtracking(): Recursive backtracking approach
"""


def all_possible_strings(s: str) -> list[str]:
    n = len(s)
    ans = []

    # Generate all possible combinations using bit manipulation
    for num in range(1, 1 << n):
        sub = ""
        for i in range(n):
            if num & (1 << i):
                sub += s[i]
        ans.append(sub)

    ans.sort()
    return ans


def solve_backtracking(i: int, s: str, f: str) -> None:
    if i == len(s):
        print(f, end=" ")
        return

    # Include current character
    solve_backtracking(i + 1, s, f + s[i])
    # Exclude current character
    solve_backtracking(i + 1, s, f)


def main():
    s = "abc"
    ans = all_possible_strings(s)

    print("All possible subsequences are:")
    solve_backtracking(0, s, "")
    print()

    print("All possible subsets are:")
    for subset in ans:
        print(subset, end=" ")


if __name__ == "__main__":
    main()
