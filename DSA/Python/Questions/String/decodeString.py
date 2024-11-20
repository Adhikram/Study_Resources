"""
# Question: Decode String
# Convert numeric strings to alphabetic representation

# Time Complexity: O(2^n)
# Space Complexity: O(n)

# Algorithm:
# 1. Create alphabet mapping (1-26 to A-Z)
# 2. Recursively decode substrings
# 3. Track valid decodings
# 4. Handle edge cases

# Key Components:
# - create_alphabet_map(): Generate number to letter mapping
# - decode(): Recursive decoder implementation
"""


def create_alphabet_map() -> dict:
    mapping = {}
    for i in range(1, 27):
        letter = chr(ord("A") + i - 1)
        mapping[str(i)] = letter
    return mapping


def decode(s: str, store: dict) -> int:
    if not store:
        return 0

    result = 0
    if s in store:
        result = 1

    n = len(s)
    for part in range(1, n):
        left_part = s[:part]
        right_part = s[part:n]
        right_result = decode(right_part, store)
        result += right_result

    return result


def main():
    store = create_alphabet_map()
    print(decode("121", store))  # Expected: 3
    print(decode("1234", store))  # Expected: 3


if __name__ == "__main__":
    main()
